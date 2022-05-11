import os
import random
from pathlib import Path
import shutil

folder_paths = "/Convert-video-to-jpg-file-by-class-name/images/D61_1_3-2.mp4/"

count = 0
directCount = 0
for f in os.listdir(folder_paths):
    Path("klasor__"+ str(directCount)+"/").mkdir(parents=True, exist_ok=True,mode=0o755)
    des = "/Convert-video-to-jpg-file-by-class-name/klasor__"+ str(directCount)+"/"+str(f)
    old_path = folder_paths+str(f)
    if f.endswith('.jpg'):
            print(f)
            if count %551 != 0: ### bölmek istediğimiz dosya sayısı
              shutil.move(old_path, str(des))
            else:
              directCount +=1 
              
    count +=1
    print(count)
    print(directCount)
