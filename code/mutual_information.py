# -*- coding: utf-8 -*-

#Created on Sat Feb  9 21:55:55 2019

#@author: andre


import numpy as np
from sklearn import preprocessing
from sklearn.feature_selection import mutual_info_classif, mutual_info_regression
import pandas as pd



#Pass in data in the format of a numpy matrix/array


def mutualInformationScores(data):
    
    X = data[:,:-1].copy()
    y = data[:,-1].copy()
    
    #standardize the data
    scaler = preprocessing.StandardScaler()
    scaler = scaler.fit(X)
    scaled_data = scaler.transform(X)
    
    X = scaled_data.copy()
    
    mi_scores = mutual_info_classif(X,y, n_neighbors = 4)
    
    return mi_scores


#This function takes the following as input:

#pandas dataframe of the entire feature space plus labels

#featureName in the format of a string which is the feature to be measured against

#labels column of your dataframe which is in the format of a string

#This finds I(x1;x2), I(x3;x2), I(xm;xt) where m is the index of the features
#and t is the target feature index.



def mutualInformationFeatures(dataframe,featureName,labels):
    
    data = dataframe
   
    feature = data.loc[:, featureName]
    
    #data = dataframe.drop(columns = [featureName,labels])
    data = dataframe.drop(columns = labels)
  
    
    data = data.values
    feature = feature.values
    
    scaler = preprocessing.StandardScaler()
    scaler = scaler.fit(data)
    scaled_data = scaler.transform(data)
    
    X = scaled_data.copy()
    
    mi_scores = mutual_info_regression(X,feature,n_neighbors = 4)
    
    return mi_scores
    
    
    
    

#here is a small test you can run
#for the Mutual information between the features and the class label


   
#filename = yourfilename
#data = np.loadtxt(yourfilename, delimiter = ',')
#scores = mutualInformationScores(data)


#This is for getting the mutual Information between features

#The resulting csv is of the format [feature1_MIscores, #feature2_MIscores...feature6_MIscores]
#the order of the scores in each column are numeric starting at the lowest feature number #value 
#i.e. feature 1 MI score vector is [MIfeature2,MIfeature3...MIfeature6]
#feature 3 MI score vector is [MIfeature1,MIfeature2,MIfeature4...MIfeature6]


#data = np.loadtxt(r'C:\Users\andre\Desktop\Repo498\fractal-#eyes\full_image_set_analysis2.csv', delimiter = ',')  
#dataframe = pd.DataFrame(data, columns = #['feature0','feature1','feature2','feature3','feature4','feature5','labels'])
#MI_1 = mutualInformationFeatures(dataframe,'feature0','labels')
#print(MI_1)

#MI_2 = mutualInformationFeatures(dataframe,'feature1','labels')
#print(MI_2)
#MI_3 = mutualInformationFeatures(dataframe,'feature2','labels')
#print(MI_3)
#MI_4 = mutualInformationFeatures(dataframe,'feature3','labels')
#print(MI_4)
#MI_5 = mutualInformationFeatures(dataframe,'feature4','labels')
#print(MI_5)
#MI_6 = mutualInformationFeatures(dataframe,'feature5','labels')
#print(MI_6)

#final = np.column_stack((MI_1,MI_2,MI_3,MI_4,MI_5,MI_6))

# saveFile = r'C:\Users\andre\Desktop\Repo498\fractal-eyes\Mutual_Information_Features.csv'
# np.savetxt(saveFile,final,delimiter = ',')