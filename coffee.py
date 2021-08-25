import pandas as pd
import plotly.express as pe
import csv
import numpy as np
def getpath(path):
     
    with open(path) as cf:
        df=csv.DictReader(cf)  
        graph=pe.scatter(df,x="Marks In Percentage",y="Days Present")
        graph.show()
def getdata(path):
    marks=[]
    day=[]
    with open(path) as cf:
        df=csv.DictReader(cf)
        for i in df:
           marks.append(float(i["Marks In Percentage"]))
           day.append(float(i["Days Present"]))
    return{"x":marks,"y":day}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation  is",corelation[0,1])    
def setup():
    path="studentinfo.csv" 
    dataSource=getdata(path)
    findcorelation(dataSource)
    getpath(path)
setup()    