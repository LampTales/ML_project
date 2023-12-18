dd#!/bin/bash
#SBATCH -o jobs/job.%j.log
#SBATCH --partition=gpulab02
#SBATCH -J pytorch_job_1
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1
#SBATCH --qos=gpulab02
#SBATCH --nodelist=gpu030

source ~/.bashrc
source activate yolo5
python -m torch.distributed.run --nproc_per_node 4 train.py --data TT100K.yaml --img 1280 --epochs 300 --weights 'runs/train/exp19/weights/best.pt' --device 2,3
python detect.py --weights runs/train/exp13/weights/best.pt --source ../../data/test/mytest.jpg --device cpu
scp -P 22000 ouyl@10.16.88.247:/home/ouyl/ML_project/models/yolov5/runs/detect/exp8/v1.mp4 C:\Users\Wiman\Desktop\receive

0.85      0.464       0.54      0.435