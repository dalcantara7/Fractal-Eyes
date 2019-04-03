import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D
import scipy.stats

def indiv_pair_plot(analyzed_image_data):
    data = np.loadtxt("excel_files/full_image_set_analysis.csv", delimiter = ',') 
    data = data.tolist()
    data.append(analyzed_image_data)
    data = np.asarray(data)

    columns = ["Number of Blobs", "Average Area of Blob", "Average Red", "Average Green", "Average Blue", "Average Lumosity", "Class"]
    colors = ['red', 'green', 'blue'] #mapping of colors is as follows: [0]->White Blood Cell [1]->Analyzed Image [2]->U2OS
    labels = ['White Blood Cell', 'U2OS Cell', 'Analyzed Image']

    white_blood_legend_elem = Line2D([0], [0], color='w', label=labels[0], marker='o', markerfacecolor=colors[0], markersize=7)
    u2os_legend_elem = Line2D([0], [0], color='w', label=labels[1], marker = 'o', markerfacecolor=colors[2], markersize=7)
    analyzed_legend_elem = Line2D([0], [0], color='w', label=labels[2], marker = 'o', markerfacecolor=colors[1], markersize=7)

    #density plots
    for i in range(0,6):
        plt.figure()
        sns.kdeplot(data[:365,i], shade=True, color=colors[0])
        sns.kdeplot(data[-365:,i], shade=True, color=colors[2])
        plt.xlabel(columns[i])
        plt.ylabel('Density')
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1) + '_' + str(i + 1) + '.png')

    #diagonal immediately below histograms
    for i in range(0,5):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+1], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+1])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 + 1) + '_' + str(i + 1) + '.png')

    for i in range (0,4):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+2], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+2])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 + 2) + '_' + str(i + 1) + '.png')

    for i in range (0,3):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+3], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+3])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 + 3) + '_' + str(i + 1) + '.png')

    for i in range (0,2):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+4], c=data[:,6], cmap=mpl.colors.ListedColormap(colors))
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+4])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 + 4) + '_' + str(i + 1) + '.png')

    for i in range (0,1):
        plt.figure()
        plt.scatter(data[:,i], data[:,i+5], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i+5])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 + 5) + '_' + str(i + 1) + '.png')

    # # diagonal immediately above histograms
    for i in range(1,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-1], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-1])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 - 1) + '_' + str(i + 1) + '.png')

    for i in range (2,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-2], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-2])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 - 2) + '_' + str(i + 1) + '.png')

    for i in range (3,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-3], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-3])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 - 3) + '_' + str(i + 1) + '.png')

    for i in range (4,6):
        plt.figure()    
        plt.scatter(data[:,i], data[:,i-4], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-4])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 - 4) + '_' + str(i + 1) + '.png')

    for i in range (5,6):
        plt.figure()
        plt.scatter(data[:,i], data[:,i-5], c=data[:,6], cmap=mpl.colors.ListedColormap(colors), label=colors)
        plt.xlabel(columns[i])
        plt.ylabel(columns[i-5])
        plt.legend(handles=[white_blood_legend_elem, u2os_legend_elem, analyzed_legend_elem])
        plt.savefig('pair_plots/' + str(i + 1 - 5) + '_' + str(i + 1) + '.png')