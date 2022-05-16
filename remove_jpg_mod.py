import os
import random

folder_paths = "Convert-video-to-jpg-file-by-class-name/images/D61_1_3-2.mp4/"
count = 0      
for f in os.listdir(folder_paths):
   if count %2 != 0:
      os.remove(os.path.join(folder_paths, f))
      print(f)
   count +=1
   print(count)
