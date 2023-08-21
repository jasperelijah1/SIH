import tkinter as tk
import sys
import os
import cv2
import numpy as np
from tkinter import messagebox
from tkinter import filedialog
import base64
import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer)""")

class popupWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        
        self.l1=tk.Label(top,text="Enter First name:")
        self.l1.pack()
        self.e1=tk.Entry(top)
        self.e1.pack()
        
        self.l2=tk.Label(top,text="Enter last name:")
        self.l2.pack()
        self.e2=tk.Entry(top)
        self.e2.pack()
        
        self.l=tk.Label(top,text="Enter Account Number")
        self.l.pack()
        self.e=tk.Entry(top)
        self.e.pack()
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        root = tk.Tk()
    def insert_emp(self):
        with conn:
            c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': self.e1, 'last': self.e2, 'pay': self.e, ,'data': self.e3})   
    def cleanup(self):
        root = tk.Tk()
        answer1 = filedialog.askopenfilename(parent=root,
                                    initialdir=os.getcwd(),
                                    title="Please select a genuine signature image file")
        root.destroy()
        
        image = open(answer,'rb')
        image_read = image.read()
        
        self.e3 = base64.encodestring(image_read)
        self.value=self.e.get()
        insert_emp(self)
        conn.close()
        self.top.destroy()
        
        root.des()

class verifyWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        self.l4=tk.Label(top,text="Enter First name:")
        self.l4.pack()
        self.e4=tk.Entry(top)
        self.e4.pack()
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        root = tk.Tk()
    def get_emps_by_name(lastname):
        c.execute("SELECT * FROM employees WHERE last=:last",{'last': lastname})
        return c.fetchall()
    def cleanup(self):
        get_emps_by_name(lastname)
        self.value=self.e.get()
        self.top.destroy()
        
        root.des()
        
class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=tk.Button(master,text="Update user info",command=self.popup)
        self.b.pack()
        self.b2=tk.Button(master,text="Verify user info",command=self.verify)
        self.b2.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.w.value


if __name__ == "__main__":
    root=tk.Tk()
    m=mainWindow(root)
    root.mainloop()