#!/bin/bash
#SBATCH -o test/zjob.%j.log
#SBATCH --partition=gpulab02
#SBATCH -J pytorch_test
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1
#SBATCH --qos=gpulab02

echo "the job"