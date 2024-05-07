"""
   read data from /raw
   transform data
   write data in /transformed
"""

import os, sys
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
      print('special')
   else:
      print(f"Format {file_ext} not supported")



