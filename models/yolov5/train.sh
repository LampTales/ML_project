#!/bin/bash
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
python -m torch.distributed.run --nproc_per_node 4 train.py --img 1280 --data TT100K.yaml --epochs 500 --weights 'models/pts/yolov5n.pt' --device 0,1,2,3