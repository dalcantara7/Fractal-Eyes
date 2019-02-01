import cv2
from matplotlib import pyplot as plt
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from skimage.io import imread
from math import sqrt
from math import pow
import matplotlib.pyplot as plt


def color_avg(filename):
    image = cv2.imread(filename)

    #Find average value of each color channel (RGB)
    redAvg = image[:,:,0].mean()
    greenAvg = image[:,:,1].mean()
    blueAvg = image[:,:,2].mean()
    
    #Display each color channel
    plt.imshow(image[:,:,0],cmap='gray')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    
    plt.imshow(image[:,:,1],cmap='gray')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    
    plt.imshow(image[:,:,2],cmap='gray')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    
    return redAvg,greenAvg,blueAvg


def lum_avg(filename):
    """
    In RGB images, image "brightness" is calculated as luminance. The weights in the 
    luminance calculation are correlated to the photopic response of the eye, or how 
    strongly the human eye perceives each color.
    Luminance = (0.2126*R + 0.7152*G + 0.0722*B)
    """
    image = cv2.imread(filename)
    
    redAvg = image[:,:,0].mean()
    greenAvg = image[:,:,1].mean()
    blueAvg = image[:,:,2].mean()
    
    #Luminance Calculation
    lumMat = 0.2126*image[:,:,0] + 0.7152*image[:,:,1] + 0.0722*image[:,:,2]
    plt.imshow(lumMat,cmap='gray')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    
    lumAvg = 0.2126*redAvg + 0.7152*greenAvg + 0.0722*blueAvg

    return lumAvg


def canny_edge_detect(filename):
    """
    The three most common types of edge detection algorithms are: Sobel, Laplacian, 
    and Canny edge detections. Sobel detection relies on the first derivative,
    Laplacian relies on the second derivative, and Canny edge detection is by 
    intensity gradient.    
    """
    image = cv2.imread(filename)
    edges = cv2.Canny(image,10,200)
    
#    #Display edge detection
#    plt.subplot(121),plt.imshow(img,cmap = 'gray')
#    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#    plt.show()

    return 

def find_blob_feats(filename):
    image = imread(filename)

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
    # plt.show() //FIXME: send plots to GUI

    return blobs_list, avg_area