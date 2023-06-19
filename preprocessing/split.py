'''
import os
from os.path import join
import shutil
path = "/home/ihclserver3/Desktop/guang-jie/DL_hw4/VOC 2007"
train_path= os.path.join(path, "VOCtrain")
val_path= os.path.join(path, "VOCval")

with open("train.txt", "r") as f:
    lines = f.readlines()

annotations = os.listdir("Annotations")
for line in lines:
    line = line.strip()
    train_annot = line + ".xml"
    if os.path.exists(train_annot):
        shutil.copy()
'''

import os
import shutil

# 訓練集檔案路徑
train_file = "val.txt"
# annotations 檔案所在目錄路徑
annotations_dir = "Annotations"
# 儲存訓練集檔案的目錄路徑
path = "/home/ihclserver3/Desktop/guang-jie/DL_hw4/VOC 2007/VOCval"
train_set_dir = os.path.join(path, annotations_dir)

# 建立儲存訓練集檔案的目錄
os.makedirs(train_set_dir, exist_ok=True)

# 讀取 train.txt 中的訓練集檔案名稱
with open(train_file, "r") as f:
    train_files = [line.strip() + ".xml" for line in f.readlines()]
print(len(train_files))

# 將訓練集檔案從 annotations 目錄複製到 train_set 目錄
for file in train_files:
    src_path = os.path.join(annotations_dir, file)
    dest_path = os.path.join(train_set_dir, file)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)

print("訓練集檔案已挑出並儲存於 train_set 目錄中。")


