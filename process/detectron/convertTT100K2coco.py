import os
import sys
import cv2
import json
import time

# read the env var
strattime = time.time()
TT100K_DATA_PATH = os.environ.get('TT100K_DATA_PATH')
print('TT100K_DATA_PATH = {}'.format(TT100K_DATA_PATH))
DETECTRON2_PATH = os.environ.get('DETECTRON2_PATH')
print('DETECTRON_PATH = {}'.format(DETECTRON2_PATH))


with open(os.path.join(TT100K_DATA_PATH,'annotations.json')) as origin_json:
    origin_dict = json.load(origin_json)
    classes = origin_dict['types']
    print("Successfully load the annotations.json file of TT100K dataset!")

train_dataset = {'info':{},'licenses':[],'categories': [],'images': [] , 'annotations': []}
val_dataset = {'info':{},'licenses':[],'categories': [],'images': [] , 'annotations': []}
test_dataset = {'info':{},'licenses':[],'categories': [],'images': [] , 'annotations': []}
label={}

info={
    "year":2021,
    "version":'1.0',
    "description":"TT100k_to_coco", 
    "contributor":"Tecent&Tsinghua",
    "url":'https://cg.cs.tsinghua.edu.cn/traffic-sign/',
    "date_created":2021-1-15
}
licenses={
    "id" :1,
    "name" :"null",
    "url" :"null",
}

train_dataset['info']=info
val_dataset['info']=info
test_dataset['info']=info
train_dataset['licenses']=licenses
val_dataset['licenses']=licenses
test_dataset['licenses']=licenses

for i, cls in enumerate(classes):
    train_dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'traffic_sign'})
    val_dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'traffic_sign'})
    test_dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'traffic_sign'})
    label[cls]=i

images_dic = origin_dict['imgs']

obj_id=1

print("Start to convert the annotations.json file of TT100K dataset to coco format!")
print("Total images: {}".format(len(images_dic)))
for image_id in images_dic:
    image_element=images_dic[image_id]
    image_path=image_element['path']
    image_path = os.path.join(TT100K_DATA_PATH, image_path)
    # im = cv2.imread(image_path)
    # print(image_path)
    # H, W, _ = im.shape
    H, W = 2048, 2048

    if 'train' in image_path:
            dataset = train_dataset
    elif 'test' in image_path:
            dataset = val_dataset
    else:
        dataset = test_dataset
    
    image_path=image_path.split('/')[-1]
    dataset['images'].append({'file_name': image_path,
                                'id': image_id,
                                'width': W,
                                'height': H})
    obj_list=image_element['objects']

    for anno_dic in obj_list:
        
        x=anno_dic['bbox']['xmin']
        y=anno_dic['bbox']['ymin']
        width=anno_dic['bbox']['xmax']-anno_dic['bbox']['xmin']
        height=anno_dic['bbox']['ymax']-anno_dic['bbox']['ymin']
        label_key=anno_dic['category']
        
        dataset['annotations'].append({
                                    'area': width * height,
                                    'bbox': [x, y, width, height],
                                    'category_id':label[label_key],
                                    'id': obj_id,
                                    'image_id': image_id,
                                    'iscrowd': 0,
                                    'segmentation': [[x, y, x+width, y, x+width, y+height, x, y+height]]
                                })
        obj_id+=1
    

# for phase in ['train','val','test']:
#     json_name = os.path.join('/home/ouyl/ML_project/TK100K/detectron2/annotations/{}.json'.format(phase))
#     with open(json_name, 'w') as f:
#         if phase == 'train':
#             json.dump(train_dataset, f,ensure_ascii=False,indent=1)
#         if phase == 'val':
#             json.dump(val_dataset, f,ensure_ascii=False,indent=1)
#         if phase == 'test':
#             json.dump(test_dataset, f,ensure_ascii=False,indent=1)
            
with open('/home/ouyl/ML_project/data/TT100K/detectron2/annotations/label.json', 'w') as f:
    f.write("[")
    for i, cls in enumerate(label):
        f.write('"'+cls+'"')
        if i!=len(classes)-1:
            f.write(',')
    f.write("]")

print("Successfully convert the annotations.json file of TT100K dataset to coco format!")
print("Time cost: {}s".format(time.time()-strattime))