import json
import os
import yaml
from PIL import Image
from process_TTjson import truncate_dir
import argparse

window_size = 1024
overlap = 0.5

ori_train_img_path = '../../data/TT100K/yolov5/images/train'
ori_test_img_path = '../../data/TT100K/yolov5/images/test'

train_img_path = '../../data/TT100K/yolov5_slide_split/images/train'
test_img_path = '../../data/TT100K/yolov5_slide_split/images/test'

train_label_path = '../../data/TT100K/yolov5_slide_split/labels/train'
test_label_path = '../../data/TT100K/yolov5_slide_split/labels/test'


def truncate_dir(dir_path):
    for file in os.listdir(dir_path):
        os.remove(os.path.join(dir_path, file))


def get_iter(path):
    file_names = os.listdir(path)
    ids = []
    for name in file_names:
        split_name = name.split('.')
        if split_name[1] == 'jpg':
            ids.append(split_name[0])
    ids.sort(key=lambda x: int(x))
    return iter(ids)


def sub_img_and_save(img_id, window_size, overlap, type='train'):
    if type == 'train':
        save_path = train_img_path
    elif type == 'test':
        save_path = test_img_path
    else:
        raise Exception('type error: No such img type')
    
    slide_size = window_size * overlap

    path = os.path.join(ori_train_img_path, img_id + '.jpg')
    img = Image.open(path)

    x = 0
    y = 0
    count = 0
    # print(f'img_id: {img_id}, img_size: {img.size}')
    while(x + window_size <= img.size[0]):
        while (y + window_size <= img.size[1]):
            sub_img = img.crop((x, y, x + window_size, y + window_size))
            sub_img.save(os.path.join(save_path, img_id + f'_{count}.jpg'))
            y += slide_size
            count += 1
        x += slide_size
        y = 0




def main():
    truncate_dir(train_img_path)

    names = get_iter(ori_train_img_path)
    for i in range(20):
        sub_img_and_save(next(names), window_size, overlap, 'train')

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ws', type=int, default=1024)
    parser.add_argument('--overlap', type=float, default=0.5)

    args = parser.parse_args()
    window_size = args.ws
    overlap = args.overlap

    main()
