import os
import pandas as pd
from cv2 import cv2

 # 将数据集从YOLOv5的xywh转换为xyxy

labels = './runs/detect/exp/labels/'
images = './data/lighters/test/'

with open('./runs/result.txt', 'w') as f:
    for r, d, filelist in os.walk(labels, topdown=False):
        for filename in filelist:
            data = pd.read_csv(labels + filename, sep=' ', header=None, names=['class','x','y','w','h', 'confidence'])
            name = filename.split('.')[0]
            img = cv2.imread(images + name + '.jpg')
            height, width, _ = img.shape

            for i, row in data.iterrows():
                x, y, w, h, confidence = row['x'], row['y'], row['w'], row['h'], row['confidence']
                if confidence >= 0.01:
                    line = '%s %.3f %.1f %.1f %.1f %.1f\n' % (
                        name, confidence,
                        width * (x - w / 2), 
                        height * (y - h / 2), 
                        width * (x + w / 2),
                        height * (y + h / 2)
                    )

                    f.write(line)
