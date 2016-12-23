# coding=utf-8

## 生成器函数
def countdown(num):
    print('Starting...')
    while num>0:
        yield num
        num-=1

## 生成器表达式
# '()'表示一个生成器表达式，
# 不要混淆列表推导式‘[]’和生成器表达式‘()’
my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in range(10))

if __name__ == '__main__':
    val=countdown(5)
    print(val)
    print(val.next())
    print(val.next())

    print(gen_obj.next())
    print(gen_obj.next())