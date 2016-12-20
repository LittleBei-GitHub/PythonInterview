# coding=utf-8

## 类的实例方法
class Kls():
    def __init__(self, data):
        self.data=data

    def printd(self):
        print(self.data)

## 类的静态函数
# python类中带有self的方法也叫绑定对象方法
# python类中有没有不带self的方法，有，静态方法就是其中一个
#
# 静态方法需要有一个修饰关键字staticmethod，
# 注意前面有一个@，连起来@staticmethod表示下面声明的是一个静态函数方法。
#
# 这是Python中的一种特殊用法，其实就是用了一个装饰器的技巧
#
# 那么Python中为啥要有静态函数:
# 场景就是和类相关的操作，但是又不会依赖和改变类、实例的状态,
# 调用静态方法可以无需创建对象

# 例子
# 有一个机器人的类，
# 有两个方法重启(do_Reset)和保存数据库(save_DB),
# 这两个方法操作之前都需要检查指令
IND='ON'
def check_Indication():
    return (IND=='ON')

class Robot():
    def __init__(self, data):
        self.data=data

    def do_Reset(self):
        if check_Indication():
            print('Reset done for :{0}'.format(self.data))

    def save_DB(self):
        if check_Indication():
            self.db='new db connection'
            print('DB connection ready for:'+self.data)

# 上例中将check_Indication()放在类的外面，
# 每次访问时都很麻烦，
# 并且让类的所有对象都能方便共享呢
#
# 有同学说简单,挪进来,然后再把调用check_Indication的地方变成Robot.check_Indication()
#
# 注意以下写法错误

# IND='ON'
#
# class Robot1():
#     def __init__(self, data):
#         self.data=data
#
#     def check_Indication():
#         return (IND == 'ON')
#
#     def do_Reset(self):
#         if Robot1.check_Indication():
#             print('Reset done for :{0}'.format(self.data))
#
#     def save_DB(self):
#         if Robot1.check_Indication():
#             self.db='new db connection'
#             print('DB connection ready for:'+self.data)

# 很明显可以看出上述做法是有错的
# 这时静态函数就可以派上用场了
IND='ON'

class Robot2():
    def __init__(self, data):
        self.data=data
    @staticmethod
    #@classmethod
    def check_Indication():
        return (IND == 'ON')

    def do_Reset(self):
        if Robot2.check_Indication():
            print('Reset done for :{0}'.format(self.data))

    def save_DB(self):
        if Robot2.check_Indication():
            self.db='new db connection'
            print('DB connection ready for:'+self.data)

## 类方法
# 类的方法就叫类方法，
# 比如我们想让方法不在实例中运行,就可以用到类方法.
# 也是用装饰器@classmethod来修饰的
#
# 例子
def get_num_of_instance(cl):
    return cl.num_student

class Student():
    num_student=0
    def __init__(self):
        Student.num_student+=1

# 其实我完全可以在类里面建一个函数，
# 然后获得类的引用去获取类的变量

class Student1():
    num_student=0
    def __init__(self):
        Student1.num_student+=1

    @classmethod
    def get_num_of_instance(cls):
        return cls.num_student

if __name__=="__main__":
    ik1=Kls('srun')
    ik1.printd()

    robot1=Robot('No1_Machine')
    robot1.do_Reset()
    robot1.save_DB()

    # 这种做法是会报错的
    # robot2 = Robot1('No2_Machine')
    # robot2.do_Reset()
    # robot2.save_DB()

    robot3 = Robot2('No3_Machine')
    robot3.do_Reset()
    robot3.save_DB()

    # 统计学生个数
    s1=Student()
    s2=Student()
    print(Student.num_student)
    print(get_num_of_instance(Student))

    s3 = Student1()
    s4 = Student1()
    print(Student1.num_student)
    print(Student1.get_num_of_instance())