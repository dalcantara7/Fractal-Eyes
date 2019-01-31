import feature_extraction_funcs as fe

def all_image_analysis():
    #FIXME: set up for loop for each type of image
    all_blob_feat, avg_area = fe.find_blob_feats()
    avg_color = fe.color_avg()
    lum_avg = fe.lum_avg()
    edges = fe.canny_edge_detect()

    #set up numpy array

    #plotting of data

    #mutual information classification