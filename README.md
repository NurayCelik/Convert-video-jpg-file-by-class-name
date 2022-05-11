# Convert video to jpg file by class name

Convert video to jpg file by extracting unwanted images - OpenCV - yolov4 

We download the Yolo Coco Dataset Model (cfg and weight files) from https://pjreddie.com/darknet/yolo/.

We add 80 class names of this model as labels.

Within these classes, we have converted the frames that we want to convert to jpg file - for example, here the frames with people in the video - into jpg file.

Give jpg files videoname + datetime + incremental number.


To separate the jpg files we created into folder -> sseparate_jpg_file_folder.py
