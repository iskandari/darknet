
import sys
import os
import glob
#import re

print("processing images from " + sys.argv[1])
#jpgRegex = re.compile(r'^.+(.jpg)$')

dirname = sys.argv[1]
# os.chdir(dirname)

arr =  glob.glob(f"{dirname}/*.jpg")

for i in arr:
    bscript = './darknet detect /home/ubuntu/darknet/AlexeyAB/darknet/build/darknet/x64/cfg/yolo-obj.cfg' + ' ' + \
    '/home/ubuntu/darknet/AlexeyAB/darknet/build/darknet/x64/backup/yolo-obj_final.weights' + ' ' + i

    os.system(bscript)
    os.system(f'python ./result_img/rename.py')
