# coding=utf-8
def hello():
    return 'hello world'

##
# 事实上，makeitalic 就是一个装饰器（decorator），
# 它“装饰”了函数 hello，
# 并返回一个函数，将其赋给 hello。
##
def makeitalic(func):
    def wrapped():
        return '<i>'+func()+'</i>'
    return wrapped

##
# 一般情况下，我们使用装饰器提供的@语法糖（Syntactic Sugar），来简化上面的写法
##
##
# 可以动态修改函数（或类）功能的函数就是装饰器。
# 本质上，它是一个高阶函数，以被装饰的函数（比如上面的 hello）为参数，
# 并返回一个包装后的函数（比如上面的 wrapped）给被装饰函数（hello）。
##
@makeitalic
def hello2():
    return 'hello little bei'

##
# 装饰器的使用形式
##

# ## 1.装饰器的一般适使用形式
# @decorator
# def func():
#     pass
# ## 1.等价于下面的形式
# def func():
#     pass
#
# func=decorator(func)

# ## 2.装饰器可以定义多个，离函数定义最近的装饰器会先被调用
# @decorator_two
# @decorator_one
# def func():
#     pass
# ## 2.等价于下面的形式
# def func():
#     pass
#
# func=decorator_two(decorator_one(func))


# ## 3.装饰器还可以带参数
# @decorator(arg1, arg2)
# def func():
#     pass
# ## 3.等价于下面的形式
# def func():
#     pass
# func=decorator(arg1, arg2)(func)


## 对带参函数进行装饰
def makeitalic2(func):
    def wrapped(*arg, **kwargs):
        ret=func(*arg, **kwargs)
        return '<i>'+ret+'</i>'
    return wrapped

@makeitalic2
def hello3(name):
    return 'hello %s'%name

@makeitalic2
def hello4(name1, name2):
    return 'hello %s, %s'%(name1, name2)


## 带参数的装饰器
def wrap_in_tag(tag):
    def decorator(func):
        def wrapped(*args, **kwargs):
            return '<'+tag+'>'+func(*args, **kwargs)+'</'+tag+'>'
        return wrapped
    return decorator

@wrap_in_tag('h')
def hello5(name):
    return 'hello %s'%name

## 多个装饰器
def makebold(fun):
    def wrapped():
        return '<b>'+fun()+'</b>'
    return wrapped

def makeitalic3(func):
    def wrapped():
        return '<i>'+func()+'</i>'
    return wrapped

@makebold
@makeitalic3
def hello6():
    return 'hello iva'

## 基于类的装饰器
# __init__()：它接受一个函数作为参数，也就是装饰的函数
# __call__()：让类对象可调用，就像函数调用一样，在调用被装饰函数时被调用
class Bold():
    def __init__(self, func):
        self.func=func

    def __call__(self, *args, **kwargs):
        return '<b>'+self.func(*args, **kwargs)+'</b>'

@Bold
def hello7():
    return 'hello ben'

# 还可以让类装饰器带参数
class Tag:
    def __init__(self, tag):
        self.tag=tag

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            return '<{tag}>{res}</{tag}>'.format(
                res=func(*args, **kwargs),
                tag=self.tag
            )
        return wrapped

@Tag('b')
def hello8():
    return 'hello iva'


## 装饰器的副作用
# 被装饰的函数，它的函数名已经不是原来的名称了
# 为了消除这样的副作用，python中的functool包提供了一个wraps的装饰器
from functools import wraps

def makeitalic4(func):
    @wraps(func)       # 加上 wraps 装饰器
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeitalic4
def hello9():
    return 'hello world'


if __name__ == '__main__':
    print(hello())

    # 返回一个函数将其赋值给hello
    hello=makeitalic(hello)
    print(hello())
    print(hello.__name__)

    # 返回一个被语法糖简化后的包装函数
    print(hello2)
    print(hello2())
    print(hello2.__name__)

    # 返回带参数的函数的装饰
    print(hello3('ben'))
    print(hello4('ben', 'iva'))

    # 返回带有参数的装饰器
    print(hello5('iva'))

    # 返回多个装饰器
    print(hello6())

    # 返回类装饰器
    print(hello7())

    # 返回带参数的类装饰器
    print(hello8())

    # 使装饰过的函数名不变
    print(hello9())
    print(hello9.__name__)