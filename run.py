#python 

#Import the required library
import sys
import os
import tkinter as tk
import subprocess, sys
from tkinter import messagebox
from tkinter import *

#Create an instance of tkinter frame
ws= Tk()
ws.title('Event Checker')
#Define geometry of the window
ws.geometry("450x350")


def hell():
    os.system("start EXCEL.exe C:\cevent\critical.csv")


def sub1():
    
    os.system(r'python C:\cevent\4624.py')
    os.system(r'python C:\cevent\4625.py')
    os.system(r'python C:\cevent\sub1.py')
    



def helloCallBack():
    os.system(r'python C:\cevent\sub.py')
    return messagebox.showinfo('Event Checker',' Wait Till the Data Gets Exported')


def close_window(): 
    ws.destroy()

def sub():
    return messagebox.showinfo('Event Checker','MONITORING  WINDOWS  SECURITY EVENTS \n \n \n By Midhun')

#Define a function to close the popup window
def close_win(top):
   top.destroy()
   ws.destroy()

#Define a function to open the Popup Dialogue
def popupwin():
   #withdraw the main window
   ws.withdraw()
   #Create a Toplevel window
   top= Toplevel(ws)
   top.geometry("350x250")
   
   #Create an Entry Widget in the Toplevel window
   
   #Create a Button Widget in the Toplevel Window	
   button= Button(top, text="Analyze Complete Log", borderwidth=3, relief="raised", padx=5, pady=5,command=helloCallBack,font=('arial bold', 16))
   button.pack(pady=5, side= TOP)
   button= Button(top, text="View Data", command=hell)
   button.pack(pady=5, side= TOP)
   button= Button(top, text="Analyze Separately", command=sub1)
   button.pack(pady=5)	
   button= Button(top, text="Quit", command=close_window)
   button.pack(pady=5, side= BOTTOM)
	

#Create a Label
label= Label(ws, text="Welcome to Simple Critical Event Checker", font= ('Helvetica 15 bold'))
label.pack(pady=20)
#Create a Button
button= Button(ws, text= "Start!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
Button(ws, text="Quit", borderwidth=3, relief="raised", padx=5, pady=5,command=close_window, bg="red",font=('arial bold', 8)).pack(padx=5, pady=5,side= BOTTOM)
Button(ws, text="FAQ", command=sub).pack(pady=20,)

ws.mainloop()