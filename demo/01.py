# -*- coding:utf-8 -*-
# coding=utf-8
# python2执行有中文汉字的文件时会报错，需要在文件顶部加上编码

# 注释
"""
print("hellow world")
"""
# print("hellowwww")

# 输入与输出
# age = 10
# name = "哈哈哈"
# print("我今年%d岁"%age)
# print("我名字叫%s"%name)

# age = input("请输入年龄\n")
# name = input("请输入名字\n")
# print('==================')
# print("年龄：%d"%age)
# print("姓名：%s"%name)
# print('==================')

# if条件判断
# age = 10
# condition1 = 5
# condition2 = 15
# age=input('请输入年龄：')
# age_num=int(age)#此处如果输入非数字会报错
# print('\nIF语句开始----------------\n')
# if age_num>condition1:
#     print('年龄大于%d'%condition1)
# else:
#     print('年龄小于等于%d'%condition1)
# if age_num>condition2:
#     print('年龄大于%d'%condition2)
# else:
#     print('年龄小于等于%d'%condition2)
# print('\nIF语句结束================\n')

# age = 10
# name = "哈哈哈"
# print("我今年%d岁"%age,"我名字叫%s"%name)

# print一次输出多个变量
# age = 10
# name = "哈哈哈"
# print("我今年%d岁，我名字叫%s"%(age,name))

# sexual=input("请输入性别，男或女：")
# age=int(input("请输入年龄"))
# if age>=18 and sexual=="女":
#     print("成年%d%s性"%(age,sexual))
# else:
#     print('只接待成年女性')

# sexual=input("请输入性别：")
# if sexual=="男":
#     print("男性")
# elif sexual=="女":
#     print("女性")
# else:
#     print("不男不女")

# 计算1~100的和
# i = 0
# sum = 0
# while i<=100:
#     print("当前数字为：%d\n当前累计总和为：%d"%(i,sum))
#     sum+=i
#     i+=1

# 九九乘法表
# i=1 # 第I行
# while i<=9:
#     j=1 # 第J列
#     while j<=i:
#         print("%d*%d=%d\t"%(j,i,i*j),end='')
#         # print执行完之后会换行，end=""可以避免换行
#         # %\t相当于tab键用于对齐
#         j+=1
#     print("\n")
#     i+=1
# print("九九乘法表完成\n")

# 猜拳游戏
# import random
# player = int(input("请输入：剪刀(0)，石头(1)，布(2) : "))
# computer =random.randint(0,2)
# print("="*30,"电脑出的是%d"%computer)
# if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
#     print("玩家获胜")
# elif player==computer:
#     print("平局")
# else:
#     print("玩家失败")
# print("="*30)

# for循环
# name = 'test'
# for x in name:
#     print(x)
# else:
#     print("没有数据")

# name = 'test'
# for x in name:
#     if(x=='s'):
#         print('循环跳出')
#         break
#     print(x)

# name = 'test'
# for x in name:
#     if(x=='s'):
#         print('循环跳出')
#         continue
#     print(x)

# 字符串-切片
# name = 'abcdef'
# print(name[0:3]) # 取 下标0~2 的字符 abc
# print(name[0:5]) # 取 下标为0~4 的字符 abcde
# print(name[2:]) # 取 下标为2开始到最后的字符 cdef
# print(name[1:-1]) # 取 下标为1开始 到 倒数第2个 之间的字符 bcde
# name2 = '0123456789'
# print(name2[1:-1:3]) # 取 下标为1开始 到 倒数第2个 之间的字符 步长为3 147

# num = 222
# str1 = str(num)
# num1 = int(str1)
# print(str1)
# print(num1+"aa")

# split()的特殊用法
# text="asad asd \t as\tdnksad nsad s adsa\tdsd\tsd sad sa dsa d asd as ds\tapkjgf oij"
# print(text.split())
# ['asad', 'asd', 'as', 'dnksad', 'nsad', 's', 'adsa', 'dsd', 'sd', 'sad', 'sa', 'dsa', 'd', 'asd', 'as', 'ds', 'apkjgf', 'oij']

# 列表
# namesList = ['aaa','bbb','ccc']
# for name in namesList:
#     print(name)
# 带下标索引的遍历
# for i,value in enumerate(namesList):
#     print(i,value)

# 元组
# a = (11, 22)
# b = a
# print(b)  # b=(11,22)
# c, d = a
# print(c, d)  # c=11 , d=22 拆包 unpack

# 列表的常用操作
# 待查找的列表
# nameList = ['xiaoWang','xiaoZhang','xiaoHua']

# 获取用户要查找的名字
# findName = input('请输入要查找的姓名:')

# 查找是否存在
# if findName in nameList:
#     print('在字典中找到了相同的名字')
# else:
#     print('没有找到')

# # 循环遍历字典
# dict1 = {'name':'abc','age':18}
# # 遍历key键
# for key in dict1.keys():
#     print(key)
# # 遍历value值
# for value in dict1.values():
#     print(value)
# # 遍历item元素
# for item in dict1.items():
#     print(item)
# # 遍历key-value键值对
# for key,value in dict1.items():
#     print(key,value)

# 全局变量和局部变量名字相同时
# a = 100
# def func1():
#     print("=======func1=======")
#     # print(a) # 首先会在局部变量之中寻找是否存在，如果存在则不会获取全局变量
#     a=200
#     print(a) # 200 局部变量

# def func2():
#     print("=======func2=======")
#     print(a) # 100 全局变量

# def func3():
#     print("=======func3=======")
#     global a # 此处讲a提升为全局变量，并且使全局变量可修改
#     print(a) # 100 全局变量
#     a=300 # 修改了全局变量
#     print(a) # 300

# print("global_before:",a) # 100 初始a的值

# func1()
# func2()
# func3()

# print("global_after:",a) # 300 此时a的值已经被func3修改了

# 默认参数
# def printinfo(age = 35):
#    print("Age:",age)

# printinfo() # Age: 35
# printinfo(age = 9) # Age: 9

# 不定长参数 基本语法
# def functionname([formal_args,] *args, **kwargs):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# def func(a,b,*args,**kwargs):
#     print("a:",a)
#     print("b:",b)
#     print("args:",args)
#     # print("kwargs:",kwargs)
#     for key,value in kwargs.items():
#         print(key,":",value)

# c=(3,4,5)
# d=["a","b","c"]
# f={"name":"abc"}
# func(1,2,6,7,*c,*d,**f)
# a: 1
# b: 2
# args: (6, 7, 3, 4, 5, 'a', 'b', 'c') # 多于a，b的参数会被存在数组args中
# name : abc # kwargs需要for key,value in kwargs.items()进行处理

# 匿名函数
# sum = lambda arg1, arg2: arg1 + arg2

# print("Value of total : ", sum( 10, 20 ))
# print("Value of total : ", sum( 20, 20 ))

# 匿名函数作为参数传递
# def func(a,b,funcL):
#     print("a:",a)
#     print("b:",b)
#     print("result=",funcL(a,b))

# func(1,2,lambda x,y:x+y)

# 匿名函数指定规则进行排序
# data=[
#     {"name":"zhangsan", "age":18},
#     {"name":"lisi", "age":19},
#     {"name":"wangwu", "age":17}
# ]
# # 按name排序
# data.sort(key=lambda x:x['name'])
# print(data)

# # 按age排序
# data.sort(key=lambda x:x['age'])
# print(data)


# a=123
# b=a
# a=1234
# print(a,b) # 1234,123

# a="hello"
# b=a
# a="hellowword"
# print(a,b) # hellowword hello

# a=('a','b','c')
# b=a
# a=('a','b','c','d')
# print(a,b) # ('a', 'b', 'c', 'd') ('a', 'b', 'c')

# a=['a','b','c']
# b=a
# a=['a','b','c','d']
# print(a,b) # ['a', 'b', 'c', 'd'] ['a', 'b', 'c', 'd']

# a="hello"
# # a[0]="w" # 报错'str' object does not support item assignment
# print(a)

# a="hello"
# # a[0]="w" # 报错'str' object does not support item assignment
# print(a)

# a=100 # @1
# a=[100] # @2
# def test(num):
#     # num+=num
#     num=num+num
#     print(num)

# test(a) # @1 200 ; @2 [100,100] ；@3 [100,100]
# print(a) # @1 100 ; @2 [100,100] ； @3 [100]

# 文件读写
# f=open("./demo/test.txt",'w+')
# f.write('abc')
# f.close()

# 文件复制备份
# def copy(file,newfile):
#     f1=open(file)
#     content=f1.read()
#     f1.close()

#     print(content)

#     f2=open(newfile,'w')
#     f2.write(content)
#     f2.close()

# filename = input("请输入要复制的文件名：")
# newfilename = input("请输入备份文件的名字：")

# copy(filename,newfilename)

# 大文件复制备份
# def copy(file,newfile):
#     content=''
#     tmp=''
#     f1=open(file)
#     # content=f1.read() # 如果遇到大文件时，read读取所有内容是非常容易内存报错的
#     while True:
#         tmp=f1.read(1024) # read的单位是字节
#         content+=tmp
#         if len(tmp)==0:
#             break

#     f2=open(newfile,'w')
#     f2.write(content) # write 只接受字符串参数

#     f1.close()
#     f2.close()

# filename = input("请输入要复制的文件名：")
# newfilename = input("请输入备份文件的名字：")

# copy(filename,newfilename)

# # 定位读写
# f1=open('test.txt')
# f1.read(2)
# position=f1.tell()
# print(position) # 2
# f1.close()

# 重设文件读写的位置
# f1=open('test.txt')
# f1.read(2)
# position=f1.tell()
# print(position) # 2

# f1.seek(0,0) # 将文件定位到头部
# position=f1.tell()
# print(position) # 0

# f1.close()

# import os
# print(os.listdir("./"))

# 批量重命名
# import os
# floder_path='testDir'
# # floder_path=input("请输入需要批量重命名的文件夹路径：")
# floder_list=os.listdir(floder_path) # 获取文件列表
# customStr='文件前缀-' # 自定义前缀
# # os.chdir(floder_path) # 更改操作路径
# # print(os.getcwd()) # 当前操作的绝对路径
# for name in floder_list:
#     if name.find(customStr)>-1:
#         continue # 如果要添加的前缀已经存在，则不进行追加
#     # print(name.find(customStr))

#     old_file_path=floder_path+'/'+name
#     new_file_path=floder_path+'/'+ customStr + name

#     # print(old_file_path,new_file_path)
#     os.rename(old_file_path,new_file_path)

# 类和对象
# class Car:
#     def getCarInfo(self):
#         print('车的信息')

#     def moveCar(self):
#         print('车在移动')

# BMW = Car()
# BMW.getCarInfo()
# BMW.moveCar()

# BMW.color='black'
# print(BMW.color) # black

# QQ = Car()
# # print(QQ.color) # 报错，实例的属性不会影响类

# 类的公有属性
# class Car:
#     def __init__(self, *args, **kwargs):
#         self.color='blue'

#     def getCarInfo(self):
#         print('车的信息')

#     def moveCar(self):
#         print('车在移动')

# BMW = Car()
# BMW.getCarInfo()
# BMW.moveCar()

# BMW.color='black'
# print(BMW.color) # black

# QQ = Car()
# print(QQ.color) # blue

# class Car:
#     def __init__(self, *args, **kwargs):
#         self.color='blue' # 此时self指向的是实例的引用地址 <__main__.Car object at 0x00000168C5D0FF98>
#         self.name='' # 由于类的方法用到name属性，此时声明可以避免报错
#         if len(args)>0:
#             self.name=args[0] # 使用参数列表，可以在创建实例时直接传入属性值

#     def getCarInfo(self):
#         print('%s车的信息'%self.name)

#     def moveCar(self):
#         print('%s车在移动'%self.name)

#     def introduce(self):
#         self.getCarInfo()
#         self.moveCar()

# BMW = Car('BMW')
# # BMW.name='BMW'
# BMW.introduce()

# BMW2 = Car()
# BMW2.introduce()

# class Car:
#     def __init__(self, *args, **kwargs):
#         self.color='blue' # 此时self指向的是实例的引用地址 <__main__.Car object at 0x00000168C5D0FF98>
#         self.name='' # 由于类的方法用到name属性，此时声明可以避免报错
#         if len(args)>0:
#             self.name=args[0] # 使用参数列表，可以在创建实例时直接传入属性值

#         self.introduce()

#     def __str__(self):
#         return 'self' # __str__必须要有返回值

#     def getCarInfo(self):
#         print('%s车的信息'%self.name)

#     def moveCar(self):
#         print('%s车在移动'%self.name)

#     def introduce(self):
#         self.getCarInfo()
#         self.moveCar()

# BMW = Car('BMW')
# BMW2 = Car()
# print(BMW) # self


# class Car:
#     def __init__(self, args, **kwargs):
#         self.color = (
#             "blue"
#         )  # 此时self指向的是实例的引用地址 <__main__.Car object at 0x00000168C5D0FF98>
#         self.name = ""  # 由于类的方法用到name属性，此时声明可以避免报错
#         if len(args) > 0:
#             self.name = args[0]  # 使用参数列表，可以在创建实例时直接传入属性值
#             # args[0] = "BMW"  # 如果将args转回list类型，则全局变量会被修改
#             customName=args
#             customName[0] = "BMW" # 由于py中变量的赋值是改变引用地址的指向，所以即使重新声明了私有变量，依然会污染全局变量

#         self.introduce()

#     def __str__(self):
#         return "self"  # __str__必须要有返回值

#     def getCarInfo(self):
#         print("%s车的信息" % self.name)

#     def moveCar(self):
#         print("%s车在移动" % self.name)

#     def introduce(self):
#         self.getCarInfo()
#         self.moveCar()


# nameB = ["MSN", "MMM"]
# BMW = Car(nameB)
# BMW2 = Car(nameB)
# print(nameB) # ['BMW', 'MMM']
# # 可以发现全局变量nameB已经被修改了，因此在传入不可变类型的全局变量时，在类中禁止对参数进行重新赋值

# 私邮方法和私有属性
# class Cars:
#     def __init__(self,producer):
#         self.__producer=producer

#     def set_name(self,attr):
#         self.attr=attr
#         self.__success('set_name')

#     def __success(self,msg):
#         print('%s成功'%msg)

#     def get_producer(self):
#         print(self.__producer)

# bmw=Cars('生产者：哈哈哈')
# bmw.set_name('bmw') # set_name成功
# # bmw.__success('调用') # 会报错，私有方法仅在对象内部可以调用
# bmw.get_producer() # 生产者：哈哈哈
# # print(bmw.__producer) # 报错，私有属性不可被外部直接调用

# __del__方法
# class Cars:
#     def __del__(self):
#         print('del方法被调用')

# newCar=Cars()
# oldCar=newCar
# # 对象的引用地址的链接数,比实际数量大1
# import sys
# print(sys.getrefcount(newCar)) # 3

# del newCar
# print(sys.getrefcount(oldCar)) # 2
# print('准备删除对象newCar')
# print('='*20)
# # 准备删除对象newCar
# # del方法被调用
# # =============

# # 这里由于有2个对象指向同一个引用地址，引用地址的链接为2
# # 删除对象的引用地址的链接大于1时，del方法会被异步执行，而不是立即调用

# 继承
# # 父类
# class Animal:
#     def eat(self):
#         print('吃')

#     def drint(self):
#         print('喝')

#     def sleep(self):
#         print('睡')

# # cat=Animal()
# # cat.eat() # 吃

# # 子类
# class Dog(Animal):
#     def bark(self):
#         print('汪汪')

# # dog1=Dog()
# # dog1.eat() # 吃
# # dog1.bark() # 汪汪

# class FlyDog(Dog):
#     def fly(self):
#         print('飞天狗')

#     # 重写bark方法
#     def bark(self):
#         print('飞天狗汪汪叫')

#         # 调用被重写的方法
#         # 方法1 调用方法的所属类名.方法(self)，参数self必传
#         Dog.bark(self) # 汪汪
#         # 方法2 super()表示上一级的类
#         super().bark() # 汪汪

# flydog1=FlyDog()
# flydog1.eat() # 吃
# flydog1.bark() # 飞天狗汪汪叫
# flydog1.fly() # 飞天狗

# 多继承
# # 定义一个父类
# class A:
#     def printA(self):
#         print('----A----')

# # 定义一个父类
# class B:
#     def printB(self):
#         print('----B----')

#     def test(self):
#         print('test-A')

# # 定义一个子类，继承自A、B
# class C(A,B):
#     def printC(self):
#         print('----C----')

#     def test(self):
#         print('test-B')

# obj_C = C()
# obj_C.printA() # ----A----
# obj_C.printB() # ----B----
# obj_C.test() # test-B 按照对象搜索方法是的先后顺序
# print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序
# # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# 类属性和实例属性