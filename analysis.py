import feature_extraction_funcs as fe
import numpy as np



def all_image_analysis():
    num_blobs_list = []
    avg_area_list = []
    avg_color_list = []
    lum_avg_list = []
    edges_list = []

    for i in range(0, 365):
        white_blood_cell_filename = "master_white_blood_cell/JPEGImages/" + str(i) + ".jpg"
        all_blob_feat, avg_area = fe.find_blob_feats(white_blood_cell_filename, False)
        num_blobs = len(all_blob_feat)
        avg_color = fe.color_avg(white_blood_cell_filename)
        lum_avg = fe.lum_avg(white_blood_cell_filename)
        # edges = fe.canny_edge_detect(white_blood_cell_filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)
        
        # edges_list.append(edges)

    for i in range(0, 365):
        human_cell_filename = "human_cell_dataset/" + str(i) + ".jpg"
        all_blob_feat, avg_area = fe.find_blob_feats(white_blood_cell_filename, True)
        num_blobs = len(all_blob_feat)
        avg_color = fe.color_avg(white_blood_cell_filename)
        lum_avg = fe.lum_avg(white_blood_cell_filename)
        # edges = fe.canny_edge_detect(white_blood_cell_filename)
        
        num_blobs_list.append(num_blobs)
        avg_area_list.append(avg_area)
        avg_color_list.append(avg_color)
        lum_avg_list.append(lum_avg)
        # edges_list.append(edges)
    
    #set up numpy array
    labels = np.zeros(732)
    for y in range (366, 731):
        labels[y] = 1
    
    num_blobs_list = np.asarray(num_blobs_list)
    avg_area_list = np.asarray(avg_area_list)
    avg_color_list = np.asarray(avg_color_list)
    lum_avg_list = np.asarray(lum_avg)
    
    numpy_array_features = np.column_stack((num_blobs_list,avg_area_list,avg_color_list,lum_avg_list,labels))
    
    np.savetxt("full_image_set_analysis.csv", numpy_array_features, delimiter=",")
    
    #plotting of data

    #mutual information classification

all_image_analysis()