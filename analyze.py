"""
   read data from /raw
   analyze data
"""

import os, sys
exec(open('my_project.conf').read())
import pandas as pd
import utils as U






# load data
df = pd.read_csv(f"{data_raw_path}/loyers.csv")

# nb lines and columns
shape = df.shape
nb_lines = shape[0]
nb_columns = shape[1]
print(nb_lines, nb_columns, U.convert_size_bytes(df.size))

print(df.describe(include='object'))
print(df.describe(include='number'))

print(df.columns)
print(df.dtypes)

print(df['ville'].isnull())

grouped = df.groupby('ville')
for a,b in grouped:
   print (a)



exit(0)







# scan files
dirs = os.listdir(data_raw_path)

# This would print all the files and directories
for file in dirs:
   file_split = os.path.splitext(file)
   file_name = file_split[0]
   file_ext = file_split[1]
   print(file)
   if file_ext == '.csv':
      print('ok')
   elif file_ext == '.npz':
      print('special')
   else:
      print(f"Format {file_ext} not supported")



