#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=gpulab02
#SBATCH -J pytorch_job_1
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1
#SBATCH --qos=gpulab02

source activate ML
python train.py -g 0 -pretrained ./weights/yolov4.conv.137.pth -classes 221 -dir ./../../data/TT100K/data/train/ -train_label_path ./../../data/TT100K/train.txt -val_label_path ./../../data/TT100K/val.txt