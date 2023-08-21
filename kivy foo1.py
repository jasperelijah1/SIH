import tkinter as tk
import sys
import os
from tkinter import messagebox


class demandWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        
        
        self.l1=tk.Label(top,text="Enter the day:")
        self.l1.pack()
        self.e1=tk.Entry(top)
        self.e1.pack()
        
        
        self.l2=tk.Label(top,text="Enter the time:")
        self.l2.pack()
        self.e2=tk.Entry(top)
        #print(self.e2)
        self.e2.pack()
        
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
        
        a= self.e1
        pathipu(a)
        
        root = tk.Tk()
        

    
    def cleanup(self):
        
       # self.value=self.e.get()
        self.top.destroy()
        
        #root.des() 
    def pathipu(a):
        print(a)
    
class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=tk.Button(master,text="Update user info",command=self.demand)
        self.b.pack()

    def demand(self):
        self.w=demandWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.w.value

  
#print(demandWindow.e1)
#print(demandWindow.e2)
    
if __name__ == "__main__":
    root=tk.Tk()
    m=mainWindow(root)
    root.mainloop()
 