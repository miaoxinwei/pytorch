import torch

x = torch.FloatTensor(5, 3)  # 构造一个未初始化的5*3的矩阵
print(x)
x = torch.rand(5, 3)  # 构造一个随机初始化的矩阵
print(x)
print(x.size())
# NOTE: torch.Size 事实上是一个tuple, 所以其支持相关的操作*
y = torch.rand(5, 3)

# 此处 将两个同形矩阵相加有两种语法结构
print(x + y)  # 语法一
print(torch.add(x, y))  # 语法二

# 另外输出tensor也有两种写法
result = torch.Tensor(5, 3)  # 语法一
torch.add(x, y, out=result)  # 语法二
print(result)
y.add_(x)  # 将y与x相加
print(y)
# 特别注明：任何可以改变tensor内容的操作都会在方法名后加一个下划线'_''
# 例如：x.copy_(y), x.t_(), 这俩都会改变x的值。

#另外python中的切片操作也是支持的。
print(y[:,0]) #这一操作会输出x矩阵的第一列的所有值


z = torch.FloatTensor([[1, 2, 3], [4, 5, 6]])
print(z)
z[0][1] = 8
print(z)