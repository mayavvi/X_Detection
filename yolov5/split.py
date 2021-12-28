import sys
import os
import numpy as np
import shutil
import argparse

def parse_opt():
    parse = argparse.ArgumentParser()
    parse.add_argument('--train_size',type=float, default=0.9)
    return parse.parse_args()

def main(opt):
    train_path = os.path.join(os.path.dirname('D:\yolo_924\datasets\mydata\images'),'images','train')
    valid_path = os.path.join(os.path.dirname('D:\yolo_924\datasets\mydata\images'),'images','val')

    all_file = [x.split('.')[0] for x in os.listdir(train_path) + os.listdir(valid_path)]
    train_names = np.random.choice(all_file, size = int(len(all_file)*opt.train_size), replace=False)

    for file_name in os.listdir(train_path):
        if file_name.split('.')[0] not in train_names:
            shutil.move(os.path.join(train_path, file_name), os.path.join(valid_path, file_name))
    for file_name in os.listdir(valid_path):
        if file_name.split('.')[0] in train_names:
            shutil.move(os.path.join(valid_path, file_name), os.path.join(train_path, file_name))


    train_path = os.path.join(os.path.dirname('D:\yolo_924\datasets\mydata\labels'),'labels','train')
    valid_path = os.path.join(os.path.dirname('D:\yolo_924\datasets\mydata\labels'),'labels','val')

    for file_name in os.listdir(train_path):
        if file_name.split('.')[0] not in train_names:
            shutil.move(os.path.join(train_path, file_name), os.path.join(valid_path, file_name))
    for file_name in os.listdir(valid_path):
        if file_name.split('.')[0] in train_names:
            shutil.move(os.path.join(valid_path, file_name), os.path.join(train_path, file_name))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)

#cd 当前文件夹 python split.py --train_size 0.9


    