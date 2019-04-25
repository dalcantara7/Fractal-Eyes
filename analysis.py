import feature_extraction_funcs as fe
import indiv_pair_plot as pp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import CNNPredicter as cnn
import mutual_information as mi
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

num_samples = 365 #for two class problem
num_samples_four_class = 619

def all_image_analysis():
    num_blobs_list = []
    avg_area_list = []
    avg_color_list = []
    lum_avg_list = []
    edges_list = []

    #calculates all features for all samples
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
    
    #saves as csv for use in later functions (reduces run time by not needing to calculate all features for all images each time the program is run)
    np.savetxt("excel_files/full_image_set_analysis.csv", numpy_array_features, delimiter=",")

def all_image_analysis_four_class(): #comments here are the same as the above function but the function restructred for more classes
    num_blobs_list = []
    avg_area_list = []
    avg_color_list = []
    lum_avg_list = []
    edges_list = []

    for i in range(1, (num_samples_four_class)+1):
        filename = "white_blood_cell_by_class/images/TEST/EOSINOPHIL/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
        avg_color = fe.color_avg(filename)
        lum_avg = fe.lum_avg(filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)

    for i in range(1, (num_samples_four_class)+1):
        filename = "white_blood_cell_by_class/images/TEST/LYMPHOCYTE/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
        avg_color = fe.color_avg(filename)
        lum_avg = fe.lum_avg(filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)    
        
    for i in range(1, (num_samples_four_class)+1):
        filename = "white_blood_cell_by_class/images/TEST/MONOCYTE/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
        avg_color = fe.color_avg(filename)
        lum_avg = fe.lum_avg(filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)
    
    for i in range(1, (num_samples_four_class)+1):
        filename = "white_blood_cell_by_class/images/TEST/NEUTROPHIL/" + str(i) + ".jpg"
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
        avg_color = fe.color_avg(filename)
        lum_avg = fe.lum_avg(filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)

    #set up numpy array
    labels = np.zeros((num_samples_four_class) * 4) #all samples
    for y in range (num_samples_four_class, (num_samples_four_class) * 2):
        labels[y] = 1
    
    for k in range ((num_samples_four_class)*2, (num_samples_four_class) * 3):
        labels[k] = 2
        
    for j in range ((num_samples_four_class)*3, (num_samples_four_class)* 4):
        labels[j] = 3
    
    num_blobs_list = np.asarray(num_blobs_list)
    avg_area_list = np.asarray(avg_area_list)
    avg_color_list = np.asarray(avg_color_list)
    lum_avg_list = np.asarray(lum_avg_list) 
    
    numpy_array_features = np.column_stack((num_blobs_list, avg_area_list, avg_color_list, lum_avg_list, labels))
    
    np.savetxt("excel_files/full_image_set_analysis_four_class.csv", numpy_array_features, delimiter=",")

def single_image_analysis(filename):
    class_label = cnn.predicter(filename) #gets class label
    
    #conditional for applying correct blob parameters
    if(class_label == 0): 
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
    else:
        num_blobs, avg_area = fe.find_blob_feats(filename, True)
    avg_color = fe.color_avg(filename)
    lum_avg = fe.lum_avg(filename)

    #creates a data array in the same form as the csv to compare against full dataset
    data_array = [num_blobs, avg_area, avg_color[0], avg_color[1], avg_color[2], lum_avg, 0.5] #0.5 is passed in as the last argument so that plotting can highlight that as the image in the plots
    
    #generates plots of data
    pp.indiv_pair_plot(data_array)

    #set up labels
    class_labels = ["White Blood Cell", "U2OS Cell"]
    feature_names = ["Number of Features", "Average Area", "Average Red", "Average Green", "Average Blue", "Average Lum", "Class"]

    data = np.loadtxt("excel_files/full_image_set_analysis.csv", delimiter = ',') 
    dataframe = pd.DataFrame(data, columns=["Number of Features", "Average Area", "Average Red", "Average Green", "Average Blue", "Average Luminance", "Class"])

    mi_features_list = list()
    feature_names = list(dataframe)

    #calculates mutual information for class label
    mi_features_list = mi.mutualInformationScores(data)
    mi_features_list = mi_features_list.tolist()

    #gets top n features for natural language explanation
    top_n_features = sort_mi(mi_features_list, 3)

    for i in feature_names:
        mi_features_list.append(mi.mutualInformationFeatures(dataframe, i, "Class"))
    
    for j in range(len(mi_features_list)):
        mi_features_list[j] = np.asarray(mi_features_list[j])
        
    mi_features_matrix = np.column_stack((mi_features_list[0], mi_features_list[1], mi_features_list[2], mi_features_list[3], mi_features_list[4], mi_features_list[5]))
    top_feat_pairs = sort_mi_feats(mi_features_matrix)

    nle = natural_language_explanation(top_n_features, mi_features_list, top_feat_pairs, feature_names, class_labels, class_label, 5)

    return nle

def single_image_analysis_four_class(filename): #comments here are the same as the above function but the funciton restructured for more classes (first conditional is also removed since the blob analysis is the same for all for classes)
    class_label = cnn.predicter(filename)
    num_blobs, avg_area = fe.find_blob_feats(filename, False)
    avg_color = fe.color_avg(filename)
    lum_avg = fe.lum_avg(filename)

    data_array = [num_blobs, avg_area, avg_color[0], avg_color[1], avg_color[2], lum_avg, 4] #4 is passed in as the last argument so that plotting can highlight that as the image in the plots
    
    # plotting of data
    pp.indiv_pair_plot_four_class(data_array)

    class_labels = ["Eosinophil", "Lymphocyte", "Monoctye", "Neutrophil"]
    feature_names = ["Number of Features", "Average Area", "Average Red", "Average Green", "Average Blue", "Average Luminance", "Class"]

    data = np.loadtxt("excel_files/full_image_set_analysis_four_class.csv", delimiter = ',') 
    dataframe = pd.DataFrame(data, columns=["Number of Features", "Average Area", "Average Red", "Average Green", "Average Blue", "Average Luminance", "Class"])

    mi_features_list = list()
    feature_names = list(dataframe)

    mi_features_list = mi.mutualInformationScores(data)
    mi_features_list = mi_features_list.tolist()

    top_n_features = sort_mi(mi_features_list, 3)

    for i in feature_names:
        mi_features_list.append(mi.mutualInformationFeatures(dataframe, i, "Class"))
    
    for j in range(len(mi_features_list)):
        mi_features_list[j] = np.asarray(mi_features_list[j])
        
    mi_features_matrix = np.column_stack((mi_features_list[0], mi_features_list[1], mi_features_list[2], mi_features_list[3], mi_features_list[4], mi_features_list[5]))
    top_feat_pairs = sort_mi_feats(mi_features_matrix)

    nle = natural_language_explanation(top_n_features, mi_features_list, top_feat_pairs, feature_names, class_labels, class_label, 5)

    return nle #returned to GUI to display on GUI

def sort_mi(mi_matrix, n): #sorts mutual information scores for class label
    top_n = sorted(range(len(mi_matrix)), key=lambda i: mi_matrix[i], reverse=True)[:int(n)]

    return top_n

def sort_mi_feats(mi_features_matrix): #sorts mutual information scores for features
    data = np.loadtxt('excel_files/Mutual_Information_Features.csv', delimiter = ',')
    triUp = np.triu(data)

    dataTri = [index for index in np.ndenumerate(triUp)]

    noDiag = []
    for i in range(len(dataTri)):
        if (dataTri[i][0][0] != dataTri[i][0][1]):
                noDiag.append(dataTri[i])

    ascendVals = sorted(noDiag, key = takeSecond)
    descendVals = ascendVals[::-1] #First n values are n biggest

    return descendVals

def takeSecond(elem): #function used in sort_mi_feats above
    return elem[1]

def natural_language_explanation(top_feats, mi_feat_for_class_label, top_feat_pairs, feat_names, class_labels, class_label, num_pairs): #generates natural language explanation for GUI and saved report (should be expanded upon)
    data_str = list()

    #formatting data string into a list in order to build string that will be displayed in GUI
    data_str.append(("The image is a " + str(class_labels[class_label]) + "\n\nFeature most relevant to class:\n"))
    for i in range(0, len(top_feats)):
        data_str.append((str(i+1) + " - " + str(feat_names[top_feats[i]]) + " with mutual information score: " + str(mi_feat_for_class_label[i]) + "\n"))

    data_str.append(str("\n"))

    data_str.append("Features most related to each other:\n")
    for i in range(0, num_pairs):
        data_str.append(str(i+1) + " - " + str(feat_names[top_feat_pairs[i][0][0]]) + " and " + str(feat_names[top_feat_pairs[i][0][1]]) + " with mutual information score: " + str(top_feat_pairs[i][1]) + "\n")

    final_str = ""
    for i in range(0, len(data_str)):
        final_str+= data_str[i]

    return final_str

# all_image_analysis_four_class()
# plot_data()
# mutual_information()
single_image_analysis_four_class("white_blood_cell_by_class/images/TEST/LYMPHOCYTE/300.jpg")
# single_image_analysis("white_blood_cell_by_class/images/TEST/LYMPHOCYTE/300.jpg")
