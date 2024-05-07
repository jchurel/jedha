"""
   read .npz file
   transform into an unziped .csv file
"""

import os, sys
import pathlib
import pandas as pd
import numpy as np
import utils
exec(open('my_project.conf').read())

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
      arrays = dict(np.load(data_raw_path+file))
      data = {k: [s.decode("utf-8") for s in v.tobytes().split(b"\x00")] if v.dtype == np.uint8 else v for k, v in arrays.items()}
      df = pd.DataFrame.from_dict(data)
      df.to_csv(f"{data_raw_path}{file_name}.csv")
      file_size = len(df)
      print(f"{file_size} lines extracted in file {{data_raw_path}{file_name}.csv}")
   else:
      print(f"Format {file_ext} not supported")
