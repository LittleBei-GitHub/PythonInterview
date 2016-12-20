# coding=utf-8

## 一般递归与尾递归 ##
## 一般递归
# 一般递归,
# 每一级递归都需要调用函数,
# 会创建新的栈,
# 随着递归深度的增加,
# 创建的栈越来越多,
# 造成爆栈
def normal_recursion(n):
    if n==1:
        return 1
    else:
        return n+normal_recursion(n-1)

## 尾递归
# 尾递归基于函数的尾调用,
# 每一级调用直接返回函数的返回值更新调用栈,
# 而不用创建新的调用栈,
# 类似迭代的实现,
# 时间和空间上均优化了一般递归!

# 存在的问题
# 虽然尾递归优化很好, 但python 不支持尾递归，递归深度超过1000时会报错

def tail_recursion(n, sum=0):
    if n==0:
        return sum
    else:
        return tail_recursion(n-1,sum+n)


if __name__=="__main__":
    print(normal_recursion(100))
    print(tail_recursion(100))