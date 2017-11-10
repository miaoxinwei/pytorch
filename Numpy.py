import torch
import numpy as np

# 此处演示tensor和numpy数据结构的相互转换
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
print('############################')
# 此处演示当修改tensor之后,与之相关联的numpy也会相应的被修改
a.add_(10)
print(a)
print(b)
print('############################')
# 将numpy的Array转换为torch的Tensor
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)
