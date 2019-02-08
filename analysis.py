import feature_extraction_funcs as fe
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif

num_samples = 365

def all_image_analysis():
    num_blobs_list = []
    avg_area_list = []
    avg_color_list = []
    lum_avg_list = []
    edges_list = []

    for i in range(0, num_samples):
        white_blood_cell_filename = "master_white_blood_cell/JPEGImages/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(white_blood_cell_filename, False)
        avg_color = fe.color_avg(white_blood_cell_filename)
        lum_avg = fe.lum_avg(white_blood_cell_filename)
        # edges = fe.canny_edge_detect(white_blood_cell_filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)
        # edges_list.append(edges)

    for i in range(0, num_samples):
        human_cell_filename = "human_cell_dataset/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(human_cell_filename, True)
        avg_color = fe.color_avg(human_cell_filename)
        lum_avg = fe.lum_avg(human_cell_filename)
        # edges = fe.canny_edge_detect(human_cell_filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)
        # edges_list.append(edges)
    
    #set up numpy array
    labels = np.zeros((num_samples) * 2) #all 732 samples
    for y in range (num_samples, (num_samples) * 2):
        labels[y] = 1
    
    num_blobs_list = np.asarray(num_blobs_list)
    avg_area_list = np.asarray(avg_area_list)
    avg_color_list = np.asarray(avg_color_list)
    lum_avg_list = np.asarray(lum_avg_list) 
    
    numpy_array_features = np.column_stack((num_blobs_list, avg_area_list, avg_color_list, lum_avg_list, labels))
    
    np.savetxt("full_image_set_analysis.csv", numpy_array_features, delimiter=",")

def plot_data():
    data = np.genfromtxt("small_full_image_set_analysis.csv", delimiter=',') #FIXME: change to full_image_set_analysis.csv once testing is completed
    data = data.tolist()
    data = pd.DataFrame(data, index=None, columns=["Num Feats", "Avg Area", "Avg Red", "Avg Green", "Avg Blue", "Avg Lum", "Class"])

    vector = data.loc[:, 'Class']
    vector = vector.tolist()
    new_vector = list()
    for i in vector:
        if i == 0:
            new_vector.append('Black')
        elif i == 1:
            new_vector.append('Blood')
    data['Class'] = new_vector
    
    # print(data)
    plot = sns.pairplot(data, hue="Class", palette="husl")
    plt.show()

def mutual_information():    
    pass


# all_image_analysis()
plot_data()