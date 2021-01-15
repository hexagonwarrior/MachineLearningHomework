import os
import shutil
from PIL import Image

# 将数据集从xyxy坐标转换为YOLOv5的xywh

def findAllFile(dirname):
    for root, ds, fs in os.walk(dirname):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname # 迭代器

if __name__ == '__main__':
    label_dirname = 'labels'
    image_dirname = 'images'
    for label in findAllFile(label_dirname):
        base = label.split('/')[1].split('.')[0]
        image = image_dirname + '/' + base + '.jpg'
        newline = ''
        with open(label, 'r') as f:
            img = Image.open(image)
            width = img.size[0]
            height = img.size[1]
            for line in f.readlines():
                s = line.split(' ')
                cl = s[0]
                x1 = float(s[2])
                y1 = float(s[3])
                x2 = float(s[4])
                y2 = float(s[5])
                newline = newline + '0 %.6f %.6f %.6f %.6f\n' % (
                    (x1 + x2) / (2 * width), (y1 + y2) / (2 * height), 
                    (x2 - x1) / width, (y2 - y1) / height)
            print newline
        with open (label, 'w') as f:
            f.write(newline)
