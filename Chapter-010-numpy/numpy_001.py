# coding=utf-8

import numpy as np

if __name__ == '__main__':
    ## 数组
    a=np.array([1,2,3])
    print(type(a))
    print(a.shape)
    print(a[0], a[1], a[2])
    a[0]=5
    print(a)

    b=np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    print(b.shape)
    print(b[0, 0], b[1, 1])

    print(np.zeros((2, 3)))
    print(np.ones((2, 3)))
    print(np.eye(2))
    print(np.full((3, 3,), 2))
    print(np.random.random((3, 4)))

    ## 访问数组
    a=np.random.random((3,4))
    print(a)
    print(a[:2, 1:3])

    # 切片
    row_1=a[1, :]
    row_2=a[1:2, :]
    print(row_1)
    print(row_1.shape)
    print(row_2)
    print(row_2.shape)

    # 列表
    a=np.random.random((4, 2))
    print(a)
    print(a[[0, 1, 3], [0, 1, 0]])
    print(a[[0, 1], [0, 1]])

    a=np.array([1,2])
    print(a.dtype)
    b=np.array([1.0, 2.3])
    print(b.dtype)
    c=np.array([1,2], dtype=np.float64)
    print(c)
    print(c.dtype)

    ## 数学计算
    x=np.array([[1,2],[3,4]], dtype=np.float64)
    y=np.array([[5,6],[7,8]], dtype=np.float64)
    print(x)
    print(y)
    print(x+y)
    print(np.add(x, y))
    print(x-y)
    print(np.subtract(x, y))
    print(x/y)
    print(np.divide(x, y))
    print(np.sqrt(x))
    # 点乘运算
    print(x * y)
    print(np.multiply(x, y))
    # 矩阵乘法
    print(x.dot(y))
    print(np.dot(x,y))

    ## 广播机制