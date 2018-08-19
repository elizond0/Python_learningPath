# -*- coding:utf-8 -*-
# coding=utf-8
# python2执行有中文汉字的文件时会报错，需要在文件顶部加上编码

# 注释
'''
print("hellow world")
'''
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

name = 'test'
for x in name:
    if(x=='s'):
        print('循环跳出')
        continue
    print(x)