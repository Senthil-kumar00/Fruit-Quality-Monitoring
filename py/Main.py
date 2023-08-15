import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import createDataset as cd
import SVMALG as SVM
import PredictFromImage as PI


bgcolor="#F9FAF7"
bgcolor1="#B7C526"
fgcolor="black"


def clear():
    print("Clear1")
    txt.delete(0, 'end')
    txt1.delete(0, 'end')
    txt2.delete(0, 'end')



window = tk.Tk()
window.title("FRUIT QUALITY DETECTION")

 
window.geometry('1280x720')
window.configure(background=bgcolor)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message1 = tk.Label(window, text="RMD ENGINEERING COLLEGE" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=20)

lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=100, y=200)
	
txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=400, y=215)

lbl1 = tk.Label(window, text="Select Image",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=100, y=300)
	
txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt1.place(x=400, y=315)
lbl = tk.Label(window, text="Rishikanth V R",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=20, y=500)
lbl = tk.Label(window, text="Naveen sankar M",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=20, y=540)
lbl = tk.Label(window, text="Lakshminarayanan E",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=20, y=580)
lbl = tk.Label(window, text="Guided by",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold underline') ) 
lbl.place(x=20, y=620)
lbl = tk.Label(window, text="Dr.C.s.Anita",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=20, y=660)


def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.delete(0, 'end')
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")	

def browse1():
	path=filedialog.askopenfilename()
	print(path)
	txt1.delete(0, 'end')
	txt1.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Image File")	

def cdprocess():
	cd.process()
	tm.showinfo("Input", "DataBase Created Successfully Finished")

def SVMprocess():
	sym=txt.get()
	if sym != "" :
		SVM.process(sym)
		tm.showinfo("Input", "SVM Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")

def PredictImage():
	sym=txt.get()
	sym1=txt1.get()
	if sym1!="" and sym!="":
		PI.process(sym,sym1)
	else:
		tm.showinfo("Input error", "Select dataset and image file")




browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=650, y=200)

browse1 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
browse1.place(x=650, y=300)

clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=200)
	 
proc = tk.Button(window, text="CreateDateSet", command=cdprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
proc.place(x=450, y=600)
	
LRbutton = tk.Button(window, text="SVM", command=SVMprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
LRbutton.place(x=650, y=600)

Xbutton = tk.Button(window, text="PredictImage", command=PredictImage  ,fg=fgcolor   ,bg=bgcolor1 ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
Xbutton.place(x=850, y=600)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1050, y=600)

window.mainloop()

