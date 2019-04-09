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
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
        
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.label = tk.Label(self, text = "")
        self.label.grid(row = 21, column = 0, columnspan = 10)
        self.filenamebrowse = "images/Screen Shot 2019-02-04 at 11.54.25 AM.png"
        self.UAlogo = "images/dwnld_ua_horiz_rgb.png"
        
        self.startPhoto = "images/start.png"
        self.stopPhoto = "images/stop.jpg"
        self.savePhoto = "images/save.jpg"
    
        self.importButton = tk.Button(self, text = "Import Image", fg = "black",command = self.importwindow)
        self.importButton.config(fg="black", pady = 10)
        self.importButton.grid(row = 0, column = 0)
        
        self.startIcon = Image.open(self.startPhoto)
        self.startIcon = self.startIcon.resize((35,35), Image.ANTIALIAS)
        self.startImg =  ImageTk.PhotoImage(self.startIcon)
        self.startButton = tk.Button(self, image=self.startImg, fg = "black",command = self.startprocessing)
        self.startButton.photo = self.startImg
        self.startButton.grid(row = 0, column = 1)
        
        self.stopIcon = Image.open(self.stopPhoto)
        self.stopIcon = self.stopIcon.resize((35,35), Image.ANTIALIAS)
        self.stopImg =  ImageTk.PhotoImage(self.stopIcon)
        self.stopButton = tk.Button(self, image=self.stopImg, fg = "black",command = self.startprocessing)
        self.stopButton.photo = self.stopImg
        self.stopButton.grid(row = 0, column = 2)

        self.saveIcon = Image.open(self.savePhoto)
        self.saveIcon = self.saveIcon.resize((35,35), Image.ANTIALIAS)
        self.saveImg =  ImageTk.PhotoImage(self.saveIcon)
        self.startButton = tk.Button(self, image=self.saveImg, fg = "black",command = self.startprocessing)
        self.startButton.photo = self.saveImg
        self.startButton.grid(row = 0, column = 3)             

        self.diagButton = tk.Button(self, text = "Diagnosis", fg = "black", command = self.diagButtonFunc)
        self.diagButton.config(padx = 33, pady = 10)
        self.diagButton.grid(row = 3, column = 7, columnspan = 2)
        
        self.featconButton = tk.Button(self, text = "Feature Constraints", fg = "black", command = self.featconButtonFunc)
        self.featconButton.config(pady = 10)
        self.featconButton.grid(row = 5, column = 7, columnspan = 2)
        
        self.quit = tk.Button(self, text = "QUIT", fg = "red", command = self.closewindow, padx = 31)
        self.quit.config(pady = 10, padx = 48)
        self.quit.grid(row = 10, column = 7, columnspan = 2)
        
        self.goButton = tk.Button(self, text = "Go", command = self.dataMenu)
        self.goButton.config(padx = 15, pady = 10)
        self.goButton.grid(row = 0, column = 7, columnspan = 2)
        
        self.gopage3 = tk.Button(self, text = "Page 2", command=lambda: master.switch_frame(PageOne))
        self.gopage3.config(padx = 42, pady = 10)
        self.gopage3.grid(row = 11, column = 7, columnspan = 2) 
        
        self.gopage2 = tk.Button(self, text = "Page 3", command=lambda: master.switch_frame(PageTwo))
        self.gopage2.config(padx = 42, pady = 10)
        self.gopage2.grid(row = 12, column = 7, columnspan = 2)
        """
        self.UAphoto = Image.open(self.UAlogo)
        self.UAphoto = self.UAphoto.resize((200,50), Image.ANTIALIAS)
        self.UAphotoImg =  ImageTk.PhotoImage(self.UAphoto)
        self.imageshown = tk.Label(self, image=self.UAphotoImg, height=500, width=500)
        self.imageshown.config(padx = 42, pady = 10)
        self.imageshown.photo = self.UAphotoImg
        self.imageshown.grid(row = 25, column = 6, columnspan = 1)
        """
        self.buildimage()
        
        self.progress = ttk.Progressbar(self, orient="horizontal",length=400, mode="determinate")
        self.progress.grid(row = 53, column = 1, columnspan = 4)

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
        
    def importwindow(self):
        
        top1 = tk.Toplevel()
        
        self.titleLabel = tk.Label(top1, text = "Import Image Tool", pady = 10)
        self.titleLabel.grid(row = 0, column = 1)
            
        self.filepathLabel = tk.Label(top1, text = "File Path: " + self.filenamebrowse)
        self.filepathLabel.grid(row = 1, pady = 0, columnspan = 3)
            
        self.rightslection = tk.Button(top1, text = "Import Image", command = self.browse)
        self.rightslection.grid(row = 2, column = 0)
        
        self.wrongselection = tk.Button(top1, text = "Select Another Image")
        self.wrongselection.grid(row = 2, column = 2)

    def browse(self):
        self.filenamebrowse =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.after(0, self.changelabel)
    
    def changelabel(self):
        self.label = tk.Label(self, text = self.filenamebrowse)
        self.label.grid(row = 55, column = 0, columnspan = 10)
        self.buildimage()        
        
    def buildimage(self):
        self.photo = Image.open(self.filenamebrowse)
        self.photo = self.photo.resize((750,750), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.photo)
        self.imageshown = tk.Label(self, image=self.photoImg, height=500, width=500)
        self.imageshown.config(padx = 42, pady = 10)
        self.imageshown.photo = self.photoImg
        self.imageshown.grid(row = 2, column = 0, columnspan = 6, rowspan = 50)
      
    def startButtonFunc(self):
        print("Start Clicking Working")
        an.single_image_analysis(self.filenamebrowse)
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
    
    def nextwindow(self):
        print("nextwindow Clicking Working")
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

class PageOne(tk.Frame):                                #f2
    def __init__(self, master):

        tk.Frame.__init__(self, master)

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
        
        self.frame_buttons = tk.Frame(self.canvas, bg="gray91")
        self.canvas.create_window((0,0), window=self.frame_buttons, anchor='nw')
        
        self.filename = ""
        self.filename_2 = ""
        self.buttons = [[tk.Button() for j in range(6)] for i in range(6)]
        for i in range(6):
            for j in range(6):
                self.filename = "pair_plots/" + str(i+1) + "_" + str(j+1) + ".png"
                self.image_1 = Image.open(self.filename)
                self.image_1 = self.image_1.resize((250, 250), Image.ANTIALIAS)
                self.photo_1 = ImageTk.PhotoImage(self.image_1)
                self.buttons[i][j] = tk.Button(self.frame_buttons, image = self.photo_1, height = 250, width = 250)
                self.buttons[i][j].image = self.photo_1
                self.buttons[i][j].grid(row = i+1, column = j+1, padx = 5, pady = 5)
        
        
        self.label_1 = tk.Label(self.frame_buttons, text = "Number Of Features")
        self.label_1.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.label_2 = tk.Label(self.frame_buttons, text = "Average Area")
        self.label_2.grid(row = 0, column = 2, padx = 5, pady = 5)
        self.label_3 = tk.Label(self.frame_buttons, text = "Average Red")
        self.label_3.grid(row = 0, column = 3, padx = 5, pady = 5)
        self.label_4 = tk.Label(self.frame_buttons, text = "Average Green")
        self.label_4.grid(row = 0, column = 4, padx = 5, pady = 5)
        self.label_5 = tk.Label(self.frame_buttons, text = "Average Blue")
        self.label_5.grid(row = 0, column = 5, padx = 5, pady = 5)
        self.label_6 = tk.Label(self.frame_buttons, text = "Average Luminosity")
        self.label_6.grid(row = 0, column = 6, padx = 5, pady = 5)
        self.label_7 = tk.Label(self.frame_buttons, text = "Number Of Features")
        self.label_7.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.label_8 = tk.Label(self.frame_buttons, text = "Average Area")
        self.label_8.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.label_9 = tk.Label(self.frame_buttons, text = "Average Red")
        self.label_9.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.label_10 = tk.Label(self.frame_buttons, text = "Average Green")
        self.label_10.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.label_11 = tk.Label(self.frame_buttons, text = "Average Blue")
        self.label_11.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.label_12 = tk.Label(self.frame_buttons, text = "Average Luminosity")
        self.label_12.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.label_13 = tk.Label(self.frame_buttons, text = "Feature by Feature plots", font=("Helvetica", 16, "bold"))
        self.label_13.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        
        self.frame_buttons.update_idletasks()

        self.frame_canvas.config(width= 950, height= 650)
        self.frame_canvas.bind('<Configure>')
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        """
        def show_filename(self,i,j,self.filename):
            text = ""
            text_2 = ""
            text_3 = ""
            if i == 0:
                text_2 = "Num of features"
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
                text_3 = "Num of features"
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
            self.v.set("Select features")
            self.v_2.set(text)
            self.feature_display = tk.Label(f3, textvariable = v_2, bg = 'gray85')
            self.feature_display.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)
            self.image_2 = Image.open(self.filename)
            self.image_2 = image_2.resize((600, 600), Image.ANTIALIAS)
            self.photo_2 = ImageTk.PhotoImage(self.image_2)
            self.image_display = tk.Label(f3, image = self.photo_2, width = 600, height = 600, bg = 'gray85')
            self.image_display.image = self.photo_2
            self.image_display.grid(row = 1, column = 2, padx = 5, pady = 5, rowspan = 100, sticky = W+E+N+S)
            self.image = tk.Button(f3, text = "Image", command = image_switch, height = 2, width = 8)#button for swithing to image
            self.image.grid(row = 40, column = 3, padx = 5, pady = 5, sticky = E)
            self.graph = tk.Button(f3, text = "Graph", command = lambda: graph_switch(self.filename), height = 2, width = 8)#button for swithing to plot
            self.graph.grid(row = 41, column = 3, padx = 5, pady = 5, sticky = E)    
            return
            """
        self.back_first = tk.Button(self, text = "Back", command=self.switchfromcanvas, height = 2, width = 8)
        self.back_first.grid(row = 2, column = 0, padx = 5, pady = 5)
            
    def switchfromcanvas(self):
        self.canvas.delete("all")
        self.master.switch_frame(StartPage)
        

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

class PageTwo(tk.Frame):                                #f3
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        """ADD COMAND FOR SAVE"""
        
        list_1 = [ "Num of features - Num of features", "Num of features - Ave Area", "Num of features - Ave Red", "Num of features - Ave Green", "Num of features - Ave Blue", "Num of features - Ave Luminosity", "Ave Area - Num of features", "Ave Area - Ave Area", "Ave Area - Ave Red", "Ave Area - Ave Green", "Ave Area - Ave Blue", "Ave Area - Ave Luminosity", "Ave Red - Num of features", "Ave Red - Ave Area", "Ave Red - Ave Red", "Ave Red - Ave Green", "Ave Red - Ave Blue", "Ave Red - Ave Luminosity", "Ave Green - Num of features", "Ave Green - Ave Area", "Ave Green - Ave Red", "Ave Green - Ave Green", "Ave Green - Ave Blue", "Ave Green - Ave Luminosity", "Ave Blue - Num of features", "Ave Blue - Ave Area", "Ave Blue - Ave Red", "Ave Blue - Ave Green", "Ave Blue - Ave Blue", "Ave Blue - Ave Luminosity", "Ave Luminosity - Num of features", "Ave Luminosity - Ave Area", "Ave Luminosity - Ave Red", "Ave Luminosity - Ave Green", "Ave Luminosity - Ave Blue", "Ave Luminosity - Ave Luminosity"]
        self.home = tk.Button(self, text = "Home",command = self.switchfromcanvas, height = 2, width = 8)#button for homepage
        self.home.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.save = tk.Button(self, text = "Save", height = 2, width = 8)#button for saving data
        self.save.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.v = tk.StringVar(master)
        self.v_2 = tk.StringVar()
        self.feature = tk.OptionMenu(self, self.v, *list_1)                                                           
        self.feature.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)
        self.feature_display = tk.Label(self, textvariable = self.v_2, bg = 'gray85')
        self.feature_display.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)


        self.text = tk.Label(self, height = 7, width = 70, bg = 'gray85', text = "Correlative Data (Statistics)",font=("Helvetica", 16, "bold"))
        self.text.grid(row = 102, column = 2, padx = 5, pady = 5)


        self.back = tk.Button(self, text = "Back", command=lambda: master.switch_frame(PageOne), height = 2, width = 8)
        self.back.grid(row = 102, column = 3, padx = 5, pady = 5)
        
        self.image = tk.Button(self, text = "Image", height = 2, width = 8)#button for swithing to image
        self.image.grid(row = 40, column = 3, padx = 5, pady = 5)   
        
        """add command = switch"""

        self.graph = tk.Button(self, text = "Graph", height = 2, width = 8)#button for swithing to plot
        self.graph.grid(row = 41, column = 3, padx = 5, pady = 5)
        
        """add command = switch"""
        
    def switchfromcanvas(self):
        """self.canvas.delete("all")"""
        self.master.switch_frame(StartPage)

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()