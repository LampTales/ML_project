import json
import os
import yaml

yaml_path = 'names.yaml'
id2name = yaml.safe_load(open(yaml_path, 'r'))['names']


json_path = '../../data/TT100K/yolov5/annotations.json'
annos = json.load(open(json_path, 'r'))['imgs']

anno_names = []
ori_names = []


def get_anno():
    for img_id, anno in annos.items():
        for obj in anno['objects']:
            category = obj['category']
            if category not in anno_names:
                anno_names.append(category)
    

def get_ori():
    for i, name in id2name.items():
        n = id2name[i]
        if n not in ori_names:
            ori_names.append(n)


def check_anno_equ_ori():
    print('In anno but not in ori:')
    for name in anno_names:
        if name not in ori_names:
            print(name)
    print('In ori but not in anno:')
    for name in ori_names:
        if name not in anno_names:
            print(name)


test_path = '../../data/TT100K/yolov5/labels/train/'

def count_files(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            count += 1
    return count

def main():
    # get_anno()
    # get_ori()
    # print(anno_names)
    # print(ori_names)
    # check_anno_equ_ori()
    # print("-----------------------")
    # print(len(anno_names))
    # print(len(ori_names))
    # print(len(id2name))
    print(count_files(test_path))


if __name__ == '__main__':
    main()