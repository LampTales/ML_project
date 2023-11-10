#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH --partition=gpulab02
#SBATCH -J pytorch_job_1
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1
#SBATCH --qos=gpulab02

source activate ML
python demo.py -cfgfile ./cfg/yolov4.cfg -weightfile ./weights/yolov4.pth -imgfile ./data/dog.jpg