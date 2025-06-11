from tkinter import*
from tkinter import ttk 
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector


class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title('Hospital Management System')
        self.root.geometry('1540*800+0+0')

root = Tk()
ob=hospital(root)
root.mainloop()