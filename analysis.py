import feature_extraction_funcs as fe
import indiv_pair_plot as pp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import CNNPredicter as cnn
import mutual_information as mi
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

def single_image_analysis(filename):
    class_label = cnn.predicter(filename)
    if(class_label == 0):
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
    else:
        num_blobs, avg_area = fe.find_blob_feats(filename, True)
    avg_color = fe.color_avg(filename)
    lum_avg = fe.lum_avg(filename)

    data_array = [num_blobs, avg_area, avg_color[0], avg_color[1], avg_color[2], lum_avg, 2] #two is passed in as the last argument so that plotting can highlight that as the image in the plots
    
    #plotting of data
    pp.indiv_pair_plot(data_array)

    data = np.loadtxt("full_image_set_analysis.csv", delimiter = ',') 
    dataframe = pd.DataFrame(data, columns=["Num Feats", "Avg Area", "Avg Red", "Avg Green", "Avg Blue", "Avg Lum", "Class"])

    mi_features_list = list()
    feature_names = list(data)

    mi_features_list = mi.mutualInformationScores(data)
    mi_features_list = mi_features_list.tolist()

    top_n_features = sort_mi(mi_features_list, 5)
    print(top_n_features)

    for i in feature_names:
        mi_features_list.append(mi.mutualInformationFeatures(dataframe, i, "Class"))
    
    for j in range(len(mi_features_list)):
        mi_features_list[j] = np.asarray(mi_features_list[j])
        
    mi_features_matrix = np.column_stack((mi_features_list[0], mi_features_list[1], mi_features_list[2], mi_features_list[3], mi_features_list[4], mi_features_list[5]))
    sort_mi_feats(mi_features_matrix)

    #FIXME: generate natural language explanation

def sort_mi(mi_matrix, n):
    top_n = sorted(range(len(mi_matrix)), key=lambda i: mi_matrix[i], reverse=True)[:int(n)]

    return top_n

def takeSecond(elem):
    return elem[1]

def sort_mi_feats(mi_features_matrix):
    data = np.loadtxt('Mutual_Information_Features.csv', delimiter = ',') #FIXME: change to use mi_features_matrix
    dims = data.shape
    triUp = np.triu(data)

    dataTri = [index for index in np.ndenumerate(triUp)]

    noDiag = []
    for i in range(len(dataTri)):
        if (dataTri[i][0][0] != dataTri[i][0][1]):
                noDiag.append(dataTri[i])

    ascendVals = sorted(noDiag, key = takeSecond)
    descendVals = ascendVals[::-1] #First n values are n biggest

def natural_language_explanation():
    pass


# all_image_analysis()
# plot_data()
# mutual_information()
single_image_analysis("human_cell_dataset/400.jpg")
# single_image_analysis(r'C:\Users\andre\Desktop\Repo498\fractal-eyes\human_cell_dataset\400.jpg')
