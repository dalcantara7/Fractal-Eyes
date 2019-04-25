import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D
import scipy.stats

def indiv_pair_plot(analyzed_image_data):
    #load all image data and appends the currently analyzed image
    data = np.loadtxt("excel_files/full_image_set_analysis.csv", delimiter = ',') 
    data = data.tolist()
    data.append(analyzed_image_data)
    data = np.asarray(data)

    #declares columns, colors, and labels to be used 
    columns = ["Number of Blobs", "Average Area of Blob", "Average Red", "Average Green", "Average Blue", "Average Luminosity", "Class"]
    colors = ['red', 'green', 'blue'] #mapping of colors is as follows: [0]->White Blood Cell [1]->Analyzed Image [2]->U2OS
    labels = ['White Blood Cell', 'U2OS Cell', 'Analyzed Image']

    #generates matplotlib legend elements
    white_blood_legend_elem = Line2D([0], [0], color='w', label=labels[0], marker='o', markerfacecolor=colors[0], markersize=7)
    u2os_legend_elem = Line2D([0], [0], color='w', label=labels[1], marker = 'o', markerfacecolor=colors[2], markersize=7)
    analyzed_legend_elem = Line2D([0], [0], color='w', label=labels[2], marker = 'o', markerfacecolor=colors[1], markersize=7)

    handles = [white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem]

    #density plots (these are the plots of features vs themselves, it is best to represent these as density plots rather than scatter plots)
    for i in range(0,6):
        plt.figure()
        sns.kdeplot(data[:365,i], shade=True, color=colors[0])
        sns.kdeplot(data[-365:,i], shade=True, color=colors[2])
        plt.xlabel(columns[i])
        plt.ylabel('Density')
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1) + '_' + str(i + 1) + '.png')

    plt.close('all')

    #all of the below are the generation of the scatter plots
    #the naming convention is set up so as to generate a pair plot like shape in the final GUI


    #diagonal immediately below histograms
    for i in range(0,5):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+1], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+1])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 1) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,4):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+2], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+2])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 2) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,3):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+3], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+3])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 3) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,2):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+4], c=data[:,6], cmap=mpl.colors.ListedColormap(colors))
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+4])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 4) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,1):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+5], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+5])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 5) + '_' + str(i + 1) + '.png')

    plt.close('all')

    # # diagonal immediately above histograms
    for i in range(1,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-1], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-1])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 1) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (2,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-2], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-2])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 2) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (3,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-3], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-3])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 3) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (4,6):
        plt.figure()    
        plt.scatter(data[:,i], data[:,i-4], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-4])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 4) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (5,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-5], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-5])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 5) + '_' + str(i + 1) + '.png')

    plt.close('all')

def indiv_pair_plot_four_class(analyzed_image_data): #comments here are the same as above but the function is restructured to handle four classes
    data = np.loadtxt("excel_files/full_image_set_analysis_four_class.csv", delimiter = ',') 
    data = data.tolist()
    data.append(analyzed_image_data)
    data = np.asarray(data)

    columns = ["Number of Blobs", "Average Area of Blob", "Average Red", "Average Green", "Average Blue", "Average Luminosity", "Class"]
    colors = ['red', 'green', 'blue', 'purple', 'yellow'] #mapping of colors is as follows: [0]->Eosinophil [1]->Lymphocyte [2]->Monocyte [3]->Neutrophil [4]->Analyzed Image
    labels = ['Eosinophil', 'Lymphocyte', 'Monocyte', 'Neutrophil', 'Analyzed Image']

    eosinophil_legend_elem = Line2D([0], [0], color='w', label=labels[0], marker='o', markerfacecolor=colors[0], markersize=7)
    lymphocyte_legend_elem = Line2D([0], [0], color='w', label=labels[1], marker = 'o', markerfacecolor=colors[1], markersize=7)
    monocyte_legend_elem = Line2D([0], [0], color='w', label=labels[2], marker = 'o', markerfacecolor=colors[2], markersize=7)
    neutrophil_legend_elem = Line2D([0], [0], color='w', label=labels[3], marker = 'o', markerfacecolor=colors[3], markersize=7)
    analyzed_legend_elem = Line2D([0], [0], color='w', label=labels[4], marker = 'o', markerfacecolor=colors[4], markersize=7)

    handles = [eosinophil_legend_elem, lymphocyte_legend_elem, monocyte_legend_elem, neutrophil_legend_elem, analyzed_legend_elem]

    #density plots
    for i in range(0,6):
        plt.figure()
        sns.kdeplot(data[:619,i], shade=True, color=colors[0])
        sns.kdeplot(data[619:1238,i], shade=True, color=colors[1])
        sns.kdeplot(data[1238:1857,i], shade=True, color=colors[2])
        sns.kdeplot(data[-619:,i], shade=True, color=colors[3])
        plt.xlabel(columns[i])
        plt.ylabel('Density')
        plt.legend(handles=handles[:-1])
        plt.savefig('pair_plots/' + str(i + 1) + '_' + str(i + 1) + '.png')

    plt.close('all')

    #diagonal immediately below histograms
    for i in range(0,5):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+1], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+1])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 1) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,4):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+2], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+2])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 2) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,3):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+3], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+3])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 3) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,2):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+4], c=data[:,6], cmap=mpl.colors.ListedColormap(colors))
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+4])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 4) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (0,1):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+5], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+5])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 + 5) + '_' + str(i + 1) + '.png')

    plt.close('all')

    # # diagonal immediately above histograms
    for i in range(1,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-1], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-1])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 1) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (2,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-2], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-2])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 2) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (3,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-3], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-3])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 3) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (4,6):
        plt.figure()    
        plt.scatter(data[:,i], data[:,i-4], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-4])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 4) + '_' + str(i + 1) + '.png')

    plt.close('all')

    for i in range (5,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-5], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-5])
        plt.legend(handles=handles)
        plt.savefig('pair_plots/' + str(i + 1 - 5) + '_' + str(i + 1) + '.png')

    plt.close('all')