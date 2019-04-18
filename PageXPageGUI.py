#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:36:22 2019

@author: pedroalcaraz
"""

import matplotlib
matplotlib.use('TkAgg')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import tkinter as tk
import analysis as an
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        
        self.filepath = "images/Screen Shot 2019-02-04 at 11.54.25 AM.png"
        self.v = tk.StringVar()
        self.v_2 = tk.StringVar()
        self.pp_filename = ""

        self.switch_frame(StartPage, self.filepath, self.v, self.v_2, self.pp_filename)
                
    def switch_frame(self, frame_class, filepath, v, v_2, pp_filename):
        self.filepath = filepath
        self.v = (v)
        self.v_2 = (v_2)
        self.pp_filename = pp_filename

        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self, self.filepath, self.v, self.v_2, self.pp_filename)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
        
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

class StartPage(tk.Frame):
    def __init__(self, master, filepath, v, v_2, pp_filename):
        tk.Frame.__init__(self, master)
        
        self.filepath = filepath
        self.v = v
        self.v_2 = v_2
        self.pp_filename = pp_filename
        
        self.radio_button_var = tk.StringVar()
        self.radio_button_var.set("Leukocytes")
        
        
        self.UAlogo = "Images/arizona_logo.png"
        self.startPhoto = "Images/start.png"
        self.stopPhoto = "Images/stop.png"
        self.savePhoto = "Images/save.jpg"
        
        self.welcomelabel = tk.Label(self, text = "Fractal Eyes Image Analysis Tool", font=("Times New Roman", 40, "bold"))
        self.welcomelabel.grid(row = 0, column = 0, columnspan = 6)
        self.welcomelabel.config(pady = 20)
    
        self.importButton = tk.Button(self, text = "Import Image", font=("Arial", 14),command =lambda: self.importwindow(self.filepath))
        self.importButton.config(pady = 19, padx = 10)
        self.importButton.grid(row = 1, column = 0)
        
        self.startIcon = Image.open(self.startPhoto)
        self.startIcon = self.startIcon.resize((35,35), Image.ANTIALIAS)
        self.startImg =  ImageTk.PhotoImage(self.startIcon)
        
        self.startButton = tk.Button(self, text = "   Start Processing", font=("Arial", 14),image=self.startImg,command = self.startprocessing, compound="left")
        self.startButton.photo = self.startImg
        self.startButton.config(pady = 10, padx = 10)
        self.startButton.grid(row = 1, column = 1)
        
        self.stopIcon = Image.open(self.stopPhoto)
        self.stopIcon = self.stopIcon.resize((40,35), Image.ANTIALIAS)
        self.stopImg =  ImageTk.PhotoImage(self.stopIcon)
        
        self.stopButton = tk.Button(self, image=self.stopImg, fg = "black",command = self.startprocessing, text = "   Stop Processing", compound="left", font=("Arial", 14,))
        self.stopButton.photo = self.stopImg
        self.stopButton.config(pady = 10, padx = 10)
        self.stopButton.grid(row = 1, column = 2)

        self.saveIcon = Image.open(self.savePhoto)
        self.saveIcon = self.saveIcon.resize((35,35), Image.ANTIALIAS)
        self.saveImg =  ImageTk.PhotoImage(self.saveIcon)
        
        self.SaveButton = tk.Button(self, image=self.saveImg, fg = "black",command = self.startprocessing, text = "   Save Data", compound="left", font=("Arial", 14))
        self.SaveButton.photo = self.saveImg
        self.SaveButton.config(pady = 10, padx = 10)
        self.SaveButton.grid(row = 1, column = 3)           
        
        self.quit = tk.Button(self, text = "QUIT", fg = "red", font=("Arial", 14,),command = self.closewindow, padx = 31)
        self.quit.config(pady = 10, padx = 48)
        self.quit.grid(row = 25, column = 7, columnspan = 2)
        
        self.gopage3 = tk.Button(self, text = "Page 2", font=("Arial", 14,), command=lambda: master.switch_frame(PageOne, self.filepath, self.v, self.v_2, self.pp_filename))
        self.gopage3.config(padx = 42, pady = 10)
        self.gopage3.grid(row = 24, column = 7, columnspan = 2)
        
        self.typeofanalysis = tk.Button(self, text="Type of Analysis", font=("Arial", 14), bg = "gray95", command = lambda: self.typeofanalysisFUNC())
        self.typeofanalysis.grid(row = 21, column = 7, columnspan = 2)
        self.typeofanalysis.config(padx = 13, pady = 11)
        
        self.typeofanalysis = tk.Radiobutton(self, text="U20S",font=("Arial", 14,), variable=self.radio_button_var, value=1)
        self.typeofanalysis.grid(row = 22, column = 7, columnspan = 2)
        self.typeofanalysis = tk.Radiobutton(self, text="Leukocytes",font=("Arial", 14,), variable=self.radio_button_var, value=2)
        self.typeofanalysis.grid(row = 23, column = 7, columnspan = 2)
        self.typeofanalysis.config(anchor="w")
        
        
        self.UAphoto = Image.open(self.UAlogo)
        self.UAphoto = self.UAphoto.resize((100,90), Image.ANTIALIAS)
        self.UAphotoImg =  ImageTk.PhotoImage(self.UAphoto)
        self.imageshown = tk.Label(self, image=self.UAphotoImg)
        self.imageshown.config(padx = 42, pady = 10)
        self.imageshown.photo = self.UAphotoImg
        self.imageshown.grid(row = 45, column = 7, columnspan = 2, rowspan = 10)
        
        self.buildimage(self.filepath)
        self.changelabel(self.filepath)
        
        self.progress = ttk.Progressbar(self, orient="horizontal",length=400, mode="determinate")
        self.progress.grid(row = 54, column = 0, columnspan = 6)
        

        self.bytes = 0
        self.maxbytes = 0

    def startprocessing(self):
        self.startButtonFunc()
        """
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()
        """

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
        
    def importwindow(self, filepath):
        
        self.filepath = filepath
        top1 = tk.Toplevel()
        top1.geometry('250x200')
        
        self.filepathvar = tk.StringVar()
        self.filepathvar.set(self.filepath)
        
        self.titleLabel = tk.Label(top1, text = "Import Image Tool", pady = 10, font=("Arial", 20,"bold"))
        self.titleLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "w"+"e")
            
        self.filepathLabel = tk.Label(top1, text = "File Path: " + self.filepathvar.get())
        self.filepathLabel.grid(row = 1, pady = 0, columnspan = 3)
        self.filepathLabel.config(wraplength = 250, pady = 20)
            
        self.rightslection = tk.Button(top1, text = "Import Image", command = lambda: [self.browse(self.filepath),top1.destroy()])
        self.rightslection.grid(row = 2, column = 0, columnspan = 3)
        
        
    def typeofanalysisFUNC (self):
        
        top1 = tk.Toplevel()
        top1.geometry('250x200')
        
        self.titleLabel = tk.Label(top1, text = "Type of Analysis Explanation", pady = 10, font=("Arial", 14,"bold"))
        self.titleLabel.grid(row = 0, column = 1)
            
        self.filepathLabel = tk.Label(top1, text = "There are two image data sets that can be used in analysis. Our neural network has been trained to classify your image given that you provide the type of image it is. Please select either the U2OS button or the Leukocyte button prior to initiating analysis.")
        self.filepathLabel.grid(row = 1, pady = 0, columnspan = 3)
        self.filepathLabel.config(wraplength = 250, anchor = "w")


    def browse(self, filepath):
        self.filepath = filepath
        self.filepath =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.changelabel(self.filepath)
        self.buildimage(self.filepath)
        
    def changelabel(self, filepath):
        self.filepath = filepath
        self.label = tk.Label(self, text = "Current Image Filepath: " + self.filepath, bg = "gray95",font=("Arial", 14,"italic"))
        self.label.grid(row = 56, column = 0, columnspan = 6)
        self.label.config(pady = 5, wraplength = 575)
        
    def buildimage(self, filepath):
        self.filepath = filepath
        self.photo = Image.open(self.filepath)
        self.photo = self.photo.resize((600,540), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.photo)
        self.imageshown = tk.Label(self, image=self.photoImg, height=535, width=535, bg = 'gray95')
        self.imageshown.config(padx = 42, pady = 10)
        self.imageshown.photo = self.photoImg
        self.imageshown.grid(row = 3, column = 0, columnspan = 6, rowspan = 50)
      
    def startButtonFunc(self):
        print("Start Clicking Working")
        an.single_image_analysis(self.filepath)
        print("DONE")
    def stopButtonFunc(self):
        print("Stop Clicking Working")
        self.progress.stop()
    def saveButtonFunc(self):
        print("Save Clicking Working")
    def diagButtonFunc(self):
        print("Diagnosis Clicking Working")
    def segmButtonFunc(self):
        print("Segmentation Clicking Working")
    def featconButtonFunc(self):
        print("Feature Constraints Clicking Working")
    def dataMenu(self):
        print ("value is", self.var.get())
    def closewindow(self):
        print("closewindow Clicking Working")
        self.window2()
        
    def window2(self):
        
        top2 = tk.Toplevel()
        
        self.Home = Button(top2, text = "Home", fg = "black")
        self.Home.config(fg="black", pady = 10)
        self.Home.grid(row = 0, column = 1)
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

class PageOne(tk.Frame):                                #f2
    def __init__(self, master, filepath, v, v_2, pp_filename):
        tk.Frame.__init__(self, master)
        
        self.master = master
        
        self.filepath = filepath
        self.v = v
        self.v_2 = v_2
        self.pp_filename = pp_filename
        
        self.back_first = tk.Button(self, text = "Back", command=lambda: master.switch_frame(StartPage, self.filepath, self.v, self.v_2, self.pp_filename), height = 2, width = 8)
        self.back_first.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.frame_canvas = tk.Frame(self)
        self.frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw', rowspan = 2)
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        self.frame_canvas.grid_propagate(False)
        
        # Add a canvas in that frame
        self.canvas = tk.Canvas(self.frame_canvas, bg="white")
        self.canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        self.vsb = tk.Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row = 0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.hor = tk.Scrollbar(self.frame_canvas, orient = "horizontal", command = self.canvas.xview)
        self.hor.grid(row = 1, column = 0, columnspan = 2)
        self.canvas.configure(xscrollcommand=self.hor.set)
        
        self.frame_buttons = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0,0), window=self.frame_buttons, anchor='nw')
        
        self.buttons = [[tk.Button() for j in range(6)] for i in range(6)]
        for i in range(6):
            for j in range(6):
                self.gen_filename = "pair_plots/" + str(i+1) + "_" + str(j+1) + ".png"
                self.image_1 = Image.open(self.gen_filename)
                self.image_1 = self.image_1.resize((250, 250), Image.ANTIALIAS)
                self.photo_1 = ImageTk.PhotoImage(self.image_1)
                self.buttons[i][j] = tk.Button(self.frame_buttons, command = lambda i=i, j=j: self.show_filename(i,j), image = self.photo_1, height = 250, width = 250)
                self.buttons[i][j].image = self.photo_1
                self.buttons[i][j].grid(row = i+1, column = j+1, padx = 5, pady = 5)
        
        self.frame_buttons.update_idletasks()

        self.frame_canvas.config(width= 950, height= 650)
        self.frame_canvas.bind('<Configure>')
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        

    def show_filename(self,i,j):
        
        self.selection_filename = ("pair_plots/" + str(i+1) + "_" + str(j+1) + ".png")
        text = ""
        text_2 = ""
        text_3 = ""
        if i == 0:
            text_2 = "Num of Features"
        elif i == 1:
            text_2 = "Ave Area"
        elif i == 2:
            text_2 = "Ave Red"
        elif i == 3:
            text_2 = "Ave Green"
        elif i == 4:
            text_2 = "Ave Blue"
        else:
            text_2 = "Ave Luminosity"
        if j == 0:
            text_3 = "Num of Features"
        elif j == 1:
            text_3 = "Ave Area"
        elif j == 2:
            text_3 = "Ave Red"
        elif j == 3:
            text_3 = "Ave Green"
        elif j == 4:
            text_3 = "Ave Blue"
        else:
            text_3 = "Ave Luminosity"
        
        text = text_2 + " - " + text_3
        
        self.v = "Select Features"
        self.v_2 = (text)
        
        self.master.switch_frame(PageTwo, self.filepath, self.v, self.v_2, self.selection_filename)
        return
        
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

class PageTwo(tk.Frame):                                #f3
    def __init__(self, master, filepath, v, v_2, pp_filename):
        tk.Frame.__init__(self, master)
        
        self.filepath = filepath
        self.pp_filename = pp_filename
        self.v = v
        self.v_2 = v_2
        #initialieze strings for tk.option menu
        self.vSV = tk.StringVar()
        self.v_2SV = tk.StringVar()
        #set-up stringVar for tk.option menu
        self.vSV.set(self.v)
        self.v_2SV.set(self.v_2)
        
        self.UAlogo = "Images/arizona_logo.png"
        self.buildimage(self.UAlogo)
        
        #FILENAME 2 IS THE IMPORTANT PAIR PLOTS PATH
        print (self.v_2)
        print ("3 " + self.pp_filename)
        self.graph_switch(self.pp_filename)
        
        
        list_1 = [ "Num of Features - Num of Features", "Num of Features - Ave Area", "Num of Features - Ave Red", "Num of Features - Ave Green", "Num of Features - Ave Blue", "Num of Features - Ave Luminosity", "Ave Area - Num of features", "Ave Area - Ave Area", "Ave Area - Ave Red", "Ave Area - Ave Green", "Ave Area - Ave Blue", "Ave Area - Ave Luminosity", "Ave Red - Num of features", "Ave Red - Ave Area", "Ave Red - Ave Red", "Ave Red - Ave Green", "Ave Red - Ave Blue", "Ave Red - Ave Luminosity", "Ave Green - Num of features", "Ave Green - Ave Area", "Ave Green - Ave Red", "Ave Green - Ave Green", "Ave Green - Ave Blue", "Ave Green - Ave Luminosity", "Ave Blue - Num of features", "Ave Blue - Ave Area", "Ave Blue - Ave Red", "Ave Blue - Ave Green", "Ave Blue - Ave Blue", "Ave Blue - Ave Luminosity", "Ave Luminosity - Num of features", "Ave Luminosity - Ave Area", "Ave Luminosity - Ave Red", "Ave Luminosity - Ave Green", "Ave Luminosity - Ave Blue", "Ave Luminosity - Ave Luminosity"]
        self.feature = tk.OptionMenu(self, self.vSV, *list_1)
        self.feature.grid(row = 3, column = 3, padx = 5, pady = 5, columnspan = 1)
        self.feature_analysis_select = self.image = tk.Button(self, text = "Select", command = lambda: self.new_feature_analysis(self.vSV))
        self.feature_analysis_select.grid(row = 3, column = 4, padx = 5, pady = 5, columnspan = 1)
        
        
        self.displaylabel(self.v_2SV)

        
        self.text = tk.Label(self, height = 7, width = 67, bg = 'gray85', text = "Correlative Data (Statistics)",font=("Helvetica", 16, "bold"))
        self.text.grid(row = 102, column = 2, padx = 5, pady = 5)
        
        self.image = tk.Button(self, text = "Image", command = self.image_switch, height = 2, width = 8)#button for swithing to image
        self.image.grid(row = 50, column = 3, padx = 5, pady = 5, columnspan = 2)
        
        self.graph = tk.Button(self, text = "Graph", command = lambda: self.graph_switch(self.pp_filename), height = 2, width = 8)#button for swithing to plot
        self.graph.grid(row = 51, column = 3, padx = 5, pady = 5, columnspan = 2) 
        
        self.back = tk.Button(self, text = "Back", command = lambda:master.switch_frame(PageOne, self.filepath, self.v, self.v_2, self.pp_filename) , height = 2, width = 8)
        self.back.grid(row = 100, column = 3, padx = 5, pady = 5, columnspan = 2)

        
    def image_switch(self):#swith to image
        self.image_2 = Image.open(self.filepath)
        self.image_2 = self.image_2.resize((600, 600), Image.ANTIALIAS)
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        self.image_display = tk.Label(self, image = self.photo_2, width = 600, height = 600, bg = 'gray85')
        self.image_display.image = self.photo_2
        self.image_display.grid(row = 1, column = 2, padx = 5, pady = 5, rowspan = 100)
        return
    
    def graph_switch(self, filename):#swith to graph
        self.image_2 = Image.open(filename)
        self.image_2 = self.image_2.resize((600, 600), Image.ANTIALIAS)
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        self.image_display = tk.Label(self, image = self.photo_2, width = 600, height = 600, bg = 'gray85')
        self.image_display.image = self.photo_2
        self.image_display.grid(row = 1, column = 2, padx = 5, pady = 5, rowspan = 100)
        return
          
    def new_feature_analysis(self, v):
       
        self.feature_selected_SV = v
        self.feature_selected = self.feature_selected_SV.get()

        if self.feature_selected == "Num of Features - Num of Features":
            self.pp_shown = "1_1.png"
        elif self.feature_selected == "Num of Features - Ave Area":
            self.pp_shown = "1_2.png"
        elif self.feature_selected == "Num of Features - Ave Red":
            self.pp_shown = "1_3.png"
        elif self.feature_selected == "Num of Features - Ave Green":
            self.pp_shown = "1_4.png"
        elif self.feature_selected == "Num of Features - Ave Blue":
            self.pp_shown = "1_5.png"     
        elif self.feature_selected == "Num of Features - Ave Luminosity":
            self.pp_shown = "1_6.png"
        elif self.feature_selected == "Ave Area - Num of Features":
            self.pp_shown = "2_1.png"
        elif self.feature_selected == "Ave Area - Ave Area":
            self.pp_shown = "2_2.png"
        elif self.feature_selected == "Ave Area - Ave Red":
            self.pp_shown = "2_3.png"
        elif self.feature_selected == "Ave Area - Ave Green":
            self.pp_shown = "2_4.png"
        elif self.feature_selected == "Ave Area - Ave Blue":
            self.pp_shown = "2_5.png"
        elif self.feature_selected == "Ave Area - Ave Luminosity":
            self.pp_shown = "2_6.png"
        elif self.feature_selected == "Ave Red - Num of Features":
            self.pp_shown = "3_1.png"
        elif self.feature_selected == "Ave Red - Ave Area":
            self.pp_shown = "3_2.png"
        elif self.feature_selected == "Ave Red - Ave Red":
            self.pp_shown = "3_3.png"
        elif self.feature_selected == "Ave Red - Ave Green":
            self.pp_shown = "3_4.png"
        elif self.feature_selected == "Ave Red - Ave Blue":
            self.pp_shown = "3_5.png"
        elif self.feature_selected == "Ave Red - Ave Luminosity":
            self.pp_shown = "3_6.png"
        elif self.feature_selected == "Ave Green - Num of Features":
            self.pp_shown = "4_1.png"
        elif self.feature_selected == "Ave Green - Ave Area":
            self.pp_shown = "4_2.png"
        elif self.feature_selected == "Ave Green - Ave Red":
            self.pp_shown = "4_3.png"
        elif self.feature_selected == "Ave Green - Ave Green":
            self.pp_shown = "4_4.png"
        elif self.feature_selected == "Ave Green - Ave Blue":
            self.pp_shown = "4_5.png"
        elif self.feature_selected == "Ave Green - Ave Luminosity":
            self.pp_shown = "4_6.png"
        elif self.feature_selected == "Ave Blue - Num of Features":
            self.pp_shown = "5_1.png"
        elif self.feature_selected == "Ave Blue - Ave Area":
            self.pp_shown = "5_2.png"
        elif self.feature_selected == "Ave Blue - Ave Red":
            self.pp_shown = "5_3.png"
        elif self.feature_selected == "Ave Blue - Ave Green":
            self.pp_shown = "5_4.png"
        elif self.feature_selected == "Ave Blue - Ave Blue":
            self.pp_shown = "5_5.png"
        elif self.feature_selected == "Ave Blue - Ave Luminosity":
            self.pp_shown = "5_6.png"
        elif self.feature_selected == "Ave Luminosity - Num of Features":
            self.pp_shown = "6_1.png"
        elif self.feature_selected == "Ave Luminosity - Ave Area":
            self.pp_shown = "6_2.png"
        elif self.feature_selected == "Ave Luminosity - Ave Red":
            self.pp_shown = "6_3.png"
        elif self.feature_selected == "Ave Luminosity - Ave Green":
            self.pp_shown = "6_4.png"
        elif self.feature_selected == "Ave Luminosity - Ave Blue":
            self.pp_shown = "6_5.png"
        else:
            self.pp_shown = "6_6.png"
        
        self.pp_filename = "pair_plots/" + self.pp_shown
        self.graph_switch(self.pp_filename)
        self.displaylabel(v)
        
        return
        
    def displaylabel (self, variable):
        self.current_feature_analysis_label = tk.Label(self, text = variable.get(), bg = "gray85")
        self.current_feature_analysis_label.grid(row = 4, column = 3, padx = 5, pady = 5, columnspan = 2)
        
    def buildimage(self, filepath):
        self.photo = Image.open(filepath)
        self.photo = self.photo.resize((100,90), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.photo)
        self.imageshown = tk.Label(self, image=self.photoImg)
        self.imageshown.config(padx = 42, pady = 10)
        self.imageshown.photo = self.photoImg
        self.imageshown.grid(row = 102, column = 3, columnspan = 2)

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

if __name__ == "__main__":

    app = SampleApp()
    app.mainloop()