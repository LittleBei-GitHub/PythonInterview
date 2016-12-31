# coding=utf-8


if __name__ == '__main__':
    ## lambda
    fun1=lambda : 123
    fun2=lambda x: x
    fun3=lambda x, y: x+y
    print(fun1())
    print(fun2(2))
    print(fun3(1, 2))

    ## map
    print(map(lambda s:s*2, [1, 2, 3]))
    print(map(lambda x, y: x+y, [1, 2, 3], [2, 3, 4]))
    print(map(None, [1, 2, 3]))
    print(map(None, [1, 2, 3], [4, 5, 6]))
    print(map(None, [1, 2, 3, 4], [5, 6, 7]))

    ## reduce
    print(reduce(lambda x, y: x+y, [1, 2, 3]))
    print(reduce(lambda x, y: x+y, [1, 2, 3], 10))

    ## filter
    #filter 有且仅有两个参数
    print(filter(lambda x: x%2, [1, 2, 3, 4]))