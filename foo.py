import tkinter as tk
#import sys
#import os
from tkinter import messagebox
#from tkinter import filedialog

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#str d

class popupWindow(object):
    #import numpy as np
    #import pandas as pd
    #import matplotlib.pyplot as plt
    
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        
        self.l1=tk.Label(top,text="ENTER THE DAY:")
        self.l1.pack()
        self.e1=tk.Entry(top)
        self.e1.pack()
        d = self.e1
        return(self.e1)
        
        self.l2=tk.Label(top,text="ENTER THE TIME:")
        self.l2.pack()
        self.e2=tk.Entry(top)
        self.e2.pack()
        h=self.e2
        return(self.e2)
        
        #self.l=tk.Label(top,text="PREDICTED CYCLE COUNT:")
        #self.l=tk.Label(top,text= val)
        
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b=tk.Button(top,text='Ok',command=self.predict)
        self.b.pack()
        
        root = tk.Tk()
    def cleanup(self):
        root = tk.Tk()
        root.destroy()
         
        self.top.destroy()
        
        root.des()
        
    def predict(self):
        datas=pd.read_csv('G://Projects//SIH%s.csv'%self.e1)
        X = datas.iloc[:,0:1].values 
        y = datas.iloc[:,1].values
        from sklearn.linear_model import LinearRegression  
        from sklearn.preprocessing import PolynomialFeatures
        #from sklearn.metrics import r2_score
        poly = PolynomialFeatures(degree=8) 
        X_poly = poly.fit_transform(X) 
        
        poly.fit(X_poly, y) 
        lin = LinearRegression() 
        lin.fit(X_poly, y) 
        plt.scatter(X, y, color = 'blue') 
        
        plt.plot(X, lin.predict(poly.fit_transform(X)), color = 'red') 
        plt.title('Polynomial Regression') 
        plt.xlabel('hour') 
        plt.ylabel('count')
        plt.show()
    
        self.val=lin.predict(poly.fit_transform([[self.e2]]))
        #r2=r2_score(y,val)
        #return(r2)
        #return(val)
        if(self.val < 0):
            return(0)
        else:
            return(self.val)
            #print("%0.3f"%r)
        messagebox.showinfo("PREDICTED VALUE", self.val)
    
class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=tk.Button(master,text="Update user info",command=self.popup)
        self.b.pack()
        #self.b2=tk.Button(master,text="Verify user info",command=self.verify)
        #self.b2.pack()

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
