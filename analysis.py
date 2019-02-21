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
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)

    for i in range(0, num_samples):
        human_cell_filename = "human_cell_dataset/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(human_cell_filename, True)
        avg_color = fe.color_avg(human_cell_filename)
        lum_avg = fe.lum_avg(human_cell_filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)
    
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

def plot_data(class_label, image_data):
    data = np.genfromtxt("full_image_set_analysis.csv", delimiter=',') #FIXME: change to full_image_set_analysis.csv once testing is completed
    data = data.tolist()
    data.append(image_data)
    data = pd.DataFrame(data, index=None, columns=["Num Feats", "Avg Area", "Avg Red", "Avg Green", "Avg Blue", "Avg Lum", "Class"])

    vector = data.loc[:, 'Class']
    vector = vector.tolist()
    new_vector = list()
    for i in vector:
        if i == 0:
            new_vector.append('Black')
        elif i == 1:
            new_vector.append('Blood')
        elif i == 2:
            new_vector.append("Analyzed Image")
    data['Class'] = new_vector
    
    plot = sns.pairplot(data, hue="Class", palette="husl")
    plt.show()

def mutual_information(dataframe, featureName, labels):    
    pass

def single_image_analysis(filename):
    #FIXME: call neural network return class label
    class_label = 1
    if(class_label == 0):
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
    else:
        num_blobs, avg_area = fe.find_blob_feats(filename, True)
    avg_color = fe.color_avg(filename)
    lum_avg = fe.lum_avg(filename)

    data_array = [num_blobs, avg_area, avg_color[0], avg_color[1], avg_color[2], lum_avg, 2] #two is passed in as the last argument so that plotting can highlight that as the image in the plots

    plot_data(class_label, data_array) 

    #FIXME: call mutual information
    #FIXME: generate natural language explanation


# all_image_analysis()
# plot_data()
# mutual_information()
single_image_analysis("human_cell_dataset/400.jpg")