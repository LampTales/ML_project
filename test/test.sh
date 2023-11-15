#!/bin/bash
#SBATCH -o jobs/job.%j.log
#SBATCH --partition=gpulab02
#SBATCH -J pytorch_test
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1
#SBATCH --qos=gpulab02
#SBATCH --nodelist=gpu029

source activate caffe
nvidia-smi
python test.py