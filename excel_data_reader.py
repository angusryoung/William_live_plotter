from pylive import live_plotter
import pandas as pd
import numpy as np
import yaml

with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    column_name = data['column_name']
    excel_file_name = data['file_name']


df = pd.read_excel(excel_file_name, sheet_name=0) # can also index sheet by name or fetch all sheets
mylist = df[column_name].tolist() #'Data' is just the name of the column

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
#some annoying errors that you could look into if you want

size = len(mylist)
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = mylist

line1 = []
while True:
    rand_val = np.random.randn(1)
    y_vec[-1] = rand_val
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)