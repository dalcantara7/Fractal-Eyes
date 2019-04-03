import feature_extraction_funcs as fe
import indiv_pair_plot as pp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import CNNPredicter as cnn
import mutual_information as mi

num_samples = 365
num_samples_four_class = 619

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
    
    np.savetxt("excel_files/full_image_set_analysis.csv", numpy_array_features, delimiter=",")

def all_image_analysis_four_class():
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
    
    np.savetxt("excel_files/full_image_set_analysis2.csv", numpy_array_features, delimiter=",")

def single_image_analysis(filename):
    class_label = cnn.predicter(filename)
    if(class_label == 0):
        num_blobs, avg_area = fe.find_blob_feats(filename, False)
    else:
        num_blobs, avg_area = fe.find_blob_feats(filename, True)
    avg_color = fe.color_avg(filename)
    lum_avg = fe.lum_avg(filename)

    data_array = [num_blobs, avg_area, avg_color[0], avg_color[1], avg_color[2], lum_avg, 0.5] #0.5 is passed in as the last argument so that plotting can highlight that as the image in the plots
    
    # plotting of data
    pp.indiv_pair_plot(data_array)

    class_labels = ["White Blood Cell", "U2OS Cell"]
    feature_names = ["Number of Features", "Average Area", "Average Red", "Average Green", "Average Blue", "Average Lum", "Class"]

    data = np.loadtxt("excel_files/full_image_set_analysis.csv", delimiter = ',') 
    dataframe = pd.DataFrame(data, columns=["Num Feats", "Avg Area", "Avg Red", "Avg Green", "Avg Blue", "Avg Lum", "Class"])

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

    natural_language_explanation(top_n_features, mi_features_list, top_feat_pairs, feature_names, class_labels, class_label, 5)

def single_image_analysis_four_class(filename):
    class_label = cnn.predicter(filename)
    num_blobs, avg_area = fe.find_blob_feats(filename, False)
    avg_color = fe.color_avg(filename)
    lum_avg = fe.lum_avg(filename)

    data_array = [num_blobs, avg_area, avg_color[0], avg_color[1], avg_color[2], lum_avg, 0.5] #0.5 is passed in as the last argument so that plotting can highlight that as the image in the plots
    
    # plotting of data
    pp.indiv_pair_plot(data_array)

    class_labels = ["Eosinophil", "Lymphocyte", "Monoctye", "Neutrophil"]
    feature_names = ["Number of Features", "Average Area", "Average Red", "Average Green", "Average Blue", "Average Lum", "Class"]

    data = np.loadtxt("excel_files/full_image_set_analysis_four_class.csv", delimiter = ',') 
    dataframe = pd.DataFrame(data, columns=["Num Feats", "Avg Area", "Avg Red", "Avg Green", "Avg Blue", "Avg Lum", "Class"])

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

    # natural_language_explanation(top_n_features, mi_features_list, top_feat_pairs, feature_names, class_labels, class_label, 5)

def sort_mi(mi_matrix, n):
    top_n = sorted(range(len(mi_matrix)), key=lambda i: mi_matrix[i], reverse=True)[:int(n)]

    return top_n

def takeSecond(elem):
    return elem[1]

def sort_mi_feats(mi_features_matrix):
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

def natural_language_explanation(top_feats, mi_feat_for_class_label, top_feat_pairs, feat_names, class_labels, class_label, num_pairs):
    print("The image is a", class_labels[class_label])
    print("Feature most relevant to class:")
    for i in range(0, len(top_feats)):
        print(str(i+1) + " - " + str(feat_names[top_feats[i]]) + " with mutual information score: " + str(mi_feat_for_class_label[i]))

    print("")

    print("Features most related to each other:")
    for i in range(0, num_pairs):
        print(str(i+1) + " - " + str(feat_names[top_feat_pairs[i][0][0]]) + " and " + str(feat_names[top_feat_pairs[i][0][1]]) + " with mutual information score: " + str(top_feat_pairs[i][1]))


# all_image_analysis()
# plot_data()
# mutual_information()
# single_image_analysis("human_cell_dataset/400.jpg")
# single_image_analysis(r'C:\Users\andre\Desktop\Repo498\fractal-eyes\human_cell_dataset\400.jpg')
