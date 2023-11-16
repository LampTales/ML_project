import json
import os
import yaml

img_size = 2048

train_imgs_path = '../../data/TT100K/yolov5/images/train'
train_labels_path = '../../data/TT100K/yolov5/labels/train'

test_imgs_path = '../../data/TT100K/yolov5/images/test'
test_labels_path = '../../data/TT100K/yolov5/labels/test'

yaml_path = 'names.yaml'
id2name = yaml.safe_load(open(yaml_path, 'r'))['names']
name2id = {}
for i, name in id2name.items():
    name2id[name] = i

# print(id2name)
# print(name2id)

json_path = '../../data/TT100K/yolov5/annotations.json'
annos = json.load(open(json_path, 'r'))['imgs']


test_path = '../../process'


def truncate_dir(dir_path):
    for file in os.listdir(dir_path):
        os.remove(os.path.join(dir_path, file))

def generate_all():
    for img_id, anno in annos.items():
        img_group = anno['path'].split('/')[0]
        if img_group == 'train':
            root_path = train_labels_path
        elif img_group == 'test':
            root_path = test_labels_path
        else:
            continue
        label_path = os.path.join(root_path, img_id + '.txt')
        label_file = open(label_path, 'w')
        for obj in anno['objects']:
            category = obj['category']
            bbox = obj['bbox']
            x_mid = (bbox['xmin'] + bbox['xmax']) / 2
            y_mid = (bbox['ymin'] + bbox['ymax']) / 2
            x_len = bbox['xmax'] - bbox['xmin']
            y_len = bbox['ymax'] - bbox['ymin']
            x_mid /= img_size
            y_mid /= img_size
            x_len /= img_size
            y_len /= img_size
            label_file.write(f'{name2id[category]} {x_mid} {y_mid} {x_len} {y_len}\n')


# may be dangerous
def truncate_and_generate_all():
    truncate_dir(train_labels_path)
    truncate_dir(test_labels_path)
    generate_all()

def main():
    truncate_and_generate_all()

if __name__ == '__main__':
    main()
