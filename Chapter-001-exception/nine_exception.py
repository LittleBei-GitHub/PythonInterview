# coding=utf-8

if __name__=='__main__':
    ## 1.变量名或函数名拼写错误：NameError
    # 访问一个不存在的变量,比如你打印一个从来没有定义过的变量或者你把函数名写错了
    # language='python'
    # print('Welcome to study:'+Language)
    #
    # price=ruond(4.2)
    # print(price)

    ## 2.方法名拼写错误：AttributeError
    # 访问一些未知的对象属性，比如字符串里面一些内置函数名拼错了
    # line='Python id easy'
    # print(line.upperr())

    ## 3.列表越界：IndexError
    # 如当我们访问list时，索引超过了列表的最大索引值
    # names=['a', 'b', 'c']
    # print(names[3])

    ## 4.忘记在if/for/while/def 声明末尾添加‘：’：SyntaxError
    # score=95
    # if score>90
    #     print('very good')

    ## 5.在循环语句中忘记调用len():TypeError
    # 有时想通过索引来迭代一个list内额元素，for循环中我们经常使用range()，
    # 但是要记得加入len()而不是直接返回这个列表
    # companies=['Google', 'Apple', 'Facebook']
    # for i in range(companies):
    #     print i

    ## 6.尝试把非字符串值和字符串值连接：TypeError
    # 有时想把字符串和数值连接一起输出，但是会有问题
    # score=82
    # print('Jack score is:'+score)

    ## 7.访问一个未初始化得本地变量：UnboundLocalError
    # 在变量使用得时候特别是在函数内部和外部用相同的变量名，经常会犯的错
    # x=10
    # def func():
    #     print(x)
    #     #x=1
    # func()
    # print('value of x is:',x)

    # 注意：在函数func()中x是局部变量，
    # 因为在函数内部又对x进行了赋值1，这样全局的x和func()中x就不是一个变量，
    # 要么改个名字或者x=1删掉，要么就得加上global，表示func()中x是用的全局x
    x=10
    def func():
        global x
        print(x)
        x=1
    func()
    print('value of x is:',x)

    ## 8.打开一个不存在的文件：IOError
    # 有时我们会访问一个文件或者定义函数去传入一个文件名，
    # 然后去读取，很可能这个文件名根本不存在
    # f=open('price.txt')

    ## 9.除数为0：ZeroDivisionError
    # 在运算一些数值的时候，可能会去引入除数是0的情况
    # 比如传入一个列表，有可能这个列表中含有0，
    # 那么在除的时候就会出错
    # nums=[10, 20, 0, 30]
    # for n in nums:
    #     print(100/n)