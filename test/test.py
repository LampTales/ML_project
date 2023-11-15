import torch
import numpy as np
import os
import torch.utils.cpp_extension
def print_cuda_devices():
    print("Number of CUDA devices:", torch.cuda.device_count())
    for device in range(torch.cuda.device_count()):
        print("Device", device, ":", torch.cuda.get_device_name(device))
        print("Memory Total:", round(torch.cuda.get_device_properties(device).total_memory / 1024 ** 2), "MB")
        print("Memory Usage:", round(torch.cuda.memory_allocated(device) / 1024 ** 2), "MB")
        print("Memory remaining:", (torch.cuda.memory_reserved(device) / 1024 ** 2), "MB")

print(torch.__file__)
print("Version: ")
print(torch.__version__)
print("CUDA: ")
print(torch.cuda.is_available())
print(torch.version.cuda)
print("CUDA_HOME", torch.utils.cpp_extension._find_cuda_home())
torch.cuda.empty_cache()
torch.cuda.memory_summary()
print_cuda_devices()
x = np.zeros((10000, 10000))
y = torch.from_numpy(x)
y = y.cuda()
print_cuda_devices()
# print(torch.cuda.memory_summary(device=None, abbreviated=False))
# print(torch.cuda.mem_get_info(device=None))