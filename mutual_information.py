# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:55:55 2019

@author: andre
"""

import numpy as np
from sklearn import preprocessing
from sklearn.feature_selection import mutual_info_classif


"""
Pass in data in the format of a numpy matrix/array

"""

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
    
"""
here is a small test you can run

"""
   
#filename = yourfilename
#data = np.loadtxt(yourfilename, delimiter = ',')
#scores = mutualInformationScores(data)
  
    
    