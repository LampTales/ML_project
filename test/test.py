import torch
def print_cuda_devices():
    print("Number of CUDA devices:", torch.cuda.device_count())
    for device in range(torch.cuda.device_count()):
        print("Device", device, ":", torch.cuda.get_device_name(device))
        print("Memory Total:", round(torch.cuda.get_device_properties(device).total_memory / 1024 ** 2), "MB")
        print("Memory Usage:", round(torch.cuda.memory_allocated(device) / 1024 ** 2), "MB")
        print("Memory remaining:", (torch.cuda.memory_reserved(device) / 1024 ** 2), "MB")

print("Version: ")
print(torch.__version__)
print("CUDA: ")
print(torch.cuda.is_available())
torch.cuda.empty_cache()
torch.cuda.memory_summary()
print_cuda_devices()
# print(torch.cuda.memory_summary(device=None, abbreviated=False))
# print(torch.cuda.mem_get_info(device=None))