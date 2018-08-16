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
condition1 = 5
condition2 = 15
age=input('请输入年龄：')
age_num=int(age)#此处如果输入非数字会报错
print('\nIF语句开始----------------\n')
if age_num>condition1:
    print('年龄大于%d'%condition1)
else:
    print('年龄小于等于%d'%condition1)
if age_num>condition2:
    print('年龄大于%d'%condition2)
else:
    print('年龄小于等于%d'%condition2)
print('\nIF语句结束================\n')