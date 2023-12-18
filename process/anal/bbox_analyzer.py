import json
import matplotlib.pyplot as plt
import numpy as np
json_file='/home/ouyl/ML_project/data/TT100K/data/annotations.json'
with open(json_file) as f:
    data = json.load(f)
x_sizes = np.zeros(len(data))
y_sizes = np.zeros(len(data))
data = data['imgs']
for img in data:
    img = data[img]
    for obj in img['objects']:
        x_size = obj['bbox']['xmax'] - obj['bbox']['xmin']
        y_size = obj['bbox']['ymax'] - obj['bbox']['ymin']
        x_sizes = np.append(x_sizes, x_size)
        y_sizes = np.append(y_sizes, y_size)
plt.scatter(x_sizes, y_sizes, s=0.25)
plt.xlim(0, 400)
plt.ylim(0, 400)
plt.xlabel('X Sizes')
plt.ylabel('Y Sizes')
plt.title('Bounding Box Sizes')
plt.show()
#output the image as a file
plt.savefig('bbox_sizes.png')

tmp = np.logical_and(x_sizes < 30, y_sizes < 30)
print(len(np.where(tmp == True)[0]) / len(x_sizes))
