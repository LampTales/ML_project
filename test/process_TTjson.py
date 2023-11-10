import json
import os
train_text_path = '../data/TT100K/train.txt'
if os.path.exists(train_text_path):
    os.remove(train_text_path)
test_text_path = '../data/TT100K/test.txt'
if os.path.exists(test_text_path):
    os.remove(test_text_path)
other_text_path = '../data/TT100K/other.txt'
if os.path.exists(other_text_path):
    os.remove(other_text_path)
train_txt = open('../data/TT100K/train.txt', 'w')
test_txt = open('../data/TT100K/test.txt', 'w')
other_txt = open('../data/TT100K/other.txt', 'w')


# Load the JSON data
with open('../data/TT100K/data/annotations.json') as json_file:
    data = json.load(json_file)

# Extract the required information
imgs = data['imgs']

pre_path = '../data/TT100K/data'
# Open the output text file and write the information
for img_id, img_data in imgs.items():
    path = img_data['path']
    belong = path.split('/')[0]
    if belong == 'train':
        dis_txt = train_txt
    elif belong == 'test':
        dis_txt = test_txt
    else:
        dis_txt = other_txt
    # dis_txt.write(f'{pre_path}/{path} ')
    dis_txt.write(path.split('/')[1] + ' ')
    for obj in img_data['objects']:
        id = obj['category']
        bbox = obj['bbox']
        x1 = bbox['xmin']
        y1 = bbox['ymin']
        x2 = bbox['xmax']
        y2 = bbox['ymax']
        dis_txt.write(f'{x1},{y1},{x2},{y2},{id} ')
    dis_txt.write('\n')