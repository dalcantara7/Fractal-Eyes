from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage.io import imread
from math import sqrt
from math import pow
import matplotlib.pyplot as plt
import cv2
import numpy as np

def find_blob_feats():
    image = imread('human_cells_dataset/IXMtest_A01_s2_w3A597237B-C3D7-43AE-8399-83E76DA1532D.tif')

    #convert image to gray scale for analysis
    image_gray = rgb2gray(image)

    blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.001)

    # Compute radii in the 3rd column.
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

    blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.01)
    blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

    blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.001)

    blobs_list = [blobs_log, blobs_dog, blobs_doh]
    colors = ['yellow', 'lime', 'red']
    titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
            'Determinant of Hessian']
    sequence = zip(blobs_list, colors, titles)

    fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
    ax = axes.ravel()

    radii_squared = 0
    sum_radii_squared = 0

    #creates blobs to plot over image
    for idx, (blobs, color, title) in enumerate(sequence):
        ax[idx].set_title(title)
        ax[idx].imshow(image, interpolation='nearest')
        for blob in blobs:
            y, x, r = blob
            c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
            ax[idx].add_patch(c)
            radii_squared = pow(r,2) #create running total of radii for computing avg area of features 
            sum_radii_squared+= radii_squared
        ax[idx].set_axis_off()

    avg_area = sum_radii_squared / len(blobs_list[0]) + len(blobs_list[1]) + len(blobs_list[2]) #computation avg area of features (ingoring pi as it is a constant) units in pixels

    #plots blobs on image
    plt.tight_layout()
    plt.show()

    return blobs_list, avg_area

def find_corner_feat():
    image = cv2.imread('human_cells_dataset/IXMtest_A01_s2_w3A597237B-C3D7-43AE-8399-83E76DA1532D.tif')

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(image_gray)
    dst = cv2.cornerHarris(gray, 200, 3, 0.04)
    dst=cv2.dilate(dst, None)

    image[dst>0.01*dst.max()] = [0,0,255]

    print(dst)

    cv2.imshow('dst', image)

find_corner_feat()
# blobs_list, avg_area = find_blob_feats()
total_features = len(blobs_list[0]) + len(blobs_list[1]) + len(blobs_list[2]) #FIXME: add Harris Laplace
total_dog_features = len(blobs_list[0]) + len(blobs_list[1]) + len(blobs_list[2]) 
print(total_features)
print(total_dog_features)
print(avg_area)