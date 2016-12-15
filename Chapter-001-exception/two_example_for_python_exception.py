# coding=utf-8

##
# 通过2个小例子来看Python是如何做异常处理的
##

##
# 基本的语法介绍
# try-except语句:
# try:
#	 do something
# except Exception, e:
#	 handle error
# else:
#	 pass
#
# try-except-finally语句:
# try:
#    do something
# except Exception:
#    handle error
# finally:
#    do finally
# 其实finally语句是表示无论是否检测到异常，都会执行finally代码，
# 因此一般我们都会把一些清理的工作,比如关闭文件或者释放资源,放在finally里面.
#
##

import random

##
# 猜数字的游戏 处理单个异常
##
def example1():
    num = random.randint(1, 10)
    while True:
        try:
            guess = int(raw_input("enter 1~10:"))
            if guess > num:
                print("guess bigger", guess)
            elif guess < num:
                print("guess smaller", guess)
            elif guess == num:
                print("great, you guess correct")
                break
        except Exception, e:
            print("input error! please enter the num 1~10!")
            continue


##
# 文件读取，处理多个异常
##

## 假如我们当前目录下没有123.txt文件，然后执行下面的代码
def example2():
    try:
        f = open("./data/123.txt")
        line = f.read()
        num = int(line)
        print('read num=%d'%num)
    except IOError, e:
        print('we catch IOError:', e)
    finally:
        print('close file')
        f.close()

## 我们把123.txt里面的100改成字符串'aa',加入多个异常处理
def example3():
    try:
        f = open('./data/123.txt')
        line = f.read()
        num = int(line)
        print('read num=%d' % num)
    except IOError, e:
        print('we catch io error:', e)
    except ValueError, e:
        print('we catch value error', e)
    finally:
        f.close()

## 若嫌多个异常处理麻烦，可以只是用Exception
def example4():
    try:
        f = open('./data/123.txt')
        line = f.read()
        num = int(line)
        print('read num=%d' % num)
    except Exception, e:
        print('we catch exception:', e)
    finally:
        f.close()

if __name__ == "__main__":
    #example1()
    #example2()
    #example3()
    example4()