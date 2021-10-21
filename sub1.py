from tkinter import * 
import sys
import os
import tkinter as tk
import subprocess, sys
from tkinter import messagebox
from tkinter import *  
  
top = Tk()   
top.geometry("750x700")
top.title('Event Checker')

def hell():
    os.system("start EXCEL.exe C:\cevent\cr4624.csv")


def hella():
    os.system("start EXCEL.exe C:\cevent\cr4625.csv")


def hellb():
    os.system("start EXCEL.exe C:\cevent\cr4634.csv")

def hellc():
    os.system("start EXCEL.exe C:\cevent\cr4648.csv")

def helld():
    os.system("start EXCEL.exe C:\cevent\cr4719.csv")

def helle():
    os.system("start EXCEL.exe C:\cevent\cr4964.csv")

def hellf():
    os.system("start EXCEL.exe C:\cevent\cr1102.csv")      

def hellg():
    os.system("start EXCEL.exe C:\cevent\cr4720.csv") 

def hellh():
    os.system("start EXCEL.exe C:\cevent\cr4722.csv")



#4624,4625,4634,4648,4719,4964,1102,4720,4722,






















 
# the label for user_name 
name = Label(top, 
                  text = "Successful account log on").place(x = 40,
                                           y = 60)    
    
submit_button = Button(top, 
                       text = "check",command=hell).place(x = 40,
                                              y = 90)


name = Label(top, 
                  text = "Failed account log on").place(x = 240,
                                           y = 60)    
    
submit_button = Button(top, 
                       text = "check",command=hella).place(x = 240,
                                              y = 90)




name = Label(top, 
                  text = "An account logged off").place(x = 440,
                                           y = 60)    
    
submit_button = Button(top, 
                       text = "check",command=hellb).place(x = 440,
                                              y = 90)


name = Label(top, 
                  text = "A logon attempt  with explicit credentials").place(x = 40,
                                           y = 260)    
    
submit_button = Button(top, 
                       text = "check",command=hellc).place(x = 40,
                                              y = 290)


name = Label(top, 
                  text = "System audit policy was changed.").place(x = 240,
                                           y = 260)    
    
submit_button = Button(top, 
                       text = "check",command=helld).place(x = 240,
                                              y = 290)




name = Label(top, 
                  text = "A special group has been assigned to a new log on").place(x = 440,
                                           y = 260)    
    
submit_button = Button(top, 
                       text = "check",command=helle).place(x = 440,
                                              y = 290)









name = Label(top, 
                  text = "Audit log was cleared. ").place(x = 40,
                                           y = 460)    
    
submit_button = Button(top, 
                       text = "check",command=hellf).place(x = 40,
                                              y = 490)

name = Label(top, 
                  text = "A user account was created").place(x = 240,
                                           y = 460)    
    
submit_button = Button(top, 
                       text = "check",command=hellg).place(x =240,
                                              y = 490)


name = Label(top, 
                  text = "A user account was enabled").place(x = 440,
                                           y = 460)    
    
submit_button = Button(top, 
                       text = "check",command=hellh).place(x =440,
                                              y = 490)





      
top.mainloop() 