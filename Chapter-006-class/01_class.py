# coding=utf-8

## 删除对象
class Dog(object):
    def __init__(self):
        print('init a dog')

    def __del__(self):
        print('del a dog')

## 类的属性和对象的属性
class Student(object):
    name='A02'
    count=0
    def __init__(self, name):
        self.name=name

    @classmethod
    def update(cls, x):
        cls.count +=x

if __name__ == '__main__':
    dog = Dog()
    del dog

    s1=Student('ben')
    s2=Student('john')
    print(s1.name)
    print(s2.name)
    print(Student.name)
    Student.update(2)
    print(Student.count)