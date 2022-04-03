from pylive import live_plotter
import pandas as pd
import numpy as np
import yaml


column_name = "Start"
excel_file_name = "live_data_example.xlsx"


df = pd.read_excel(excel_file_name, sheet_name=0) # can also index sheet by name or fetch all sheets
mylist = df[column_name].tolist()[0:49] #'Data' is just the name of the column
datalist = df["Data"].tolist()

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
#some annoying errors that you could look into if you want

size = len(mylist)
print(mylist)
print(size)
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = mylist

line1 = []

for data in datalist:
    y_vec[-1] = data
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)


while True:
    rand_val = np.random.randn(1)
    y_vec[-1] = rand_val
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)