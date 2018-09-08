import numpy as np

a = np.array([[1,2,3,4,5,6,7],[5,6,7,8,9,10,11]])

print(a.shape)
print(a.shape[0])
print(a.shape[1])

print(a[0:1])
print(a[1,2:5])

b = a[a>6]
print(b)


#矩阵合并
a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[7,8]])

print(np.hstack([a1, a2]))
print(np.vstack((a1,a2)))

a3 = np.arange(5,20,2) #创建矩阵
print(a3)

