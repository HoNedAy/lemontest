# 名字命名规则
# （1）只能包含数字、字母、下划线
# （2）不能以数字开头
# （3）不能使用关键字
#      可以通过import keyword
# print(keyword.kwlist)打印关键字
# ctrl+/也可以多行注释
# import keyword
# print("打印到控制台")
# print(type(12))
# print(type(3.14))
# print(isinstance(12,int))
# print("刚刚'你好呀'下雨啦")
# print("刚刚\"人名\"下雨啦")
# print("""
#    今天下雨了没
#             今天没下雨
#                         今天学python
# """)

#切片取多个值===字符串取值，索引从0开始 0.1.2.3
#步长：隔几步取值
# str="今天1天气真好！"
# print(str[0:3:2])#隔2步取值，取索引值为0,2的字符串
# print(str[1:6:2])#隔2步取值，取索引为1,3,5的字符串
# print(str[-1])#-1代表最后一个元素
# print(str[::-1])#从右向左取值

# # print(str1[0:len(str1):1])#从0开始取值，len()是str1字符串的长度
# # str1="12今天你学习了吗？"
# # str2=str1.replace("12","新的值")
# # # print(str2)
# # print(str1.index('学习'))#获取元素开始的位置--索引--字符串不存在的时候会报错
# # print(str1.find('学习'))#获取元素开始的位置--索引--字符串不存在的时候不会报错，会返回-1
#
# name='皮卡丘'   #--0--索引
# age=18          #--1--索引
# gender='Female' #--2--索引
# print('''
#     ---{1}同学的信息----
#     name:{1}
#     age:{2}
#     gender:{3}'''.format(name,name,age,gender)
# )
# print(10+80)
# print('按时'+'交作业')
# print(str(123)+'向前走呀')  #123要转化为字符串：str()--内置函数：int(),float(),bool()

# a=10
# a += 5  #a=a+5  a=15
# print(a)
# a-=10    #a=a-10

# print(10>8 and 5>6)  #--True and Flase ==False
# print(10>8 or 5>6)   #--True or Flase ==True
# print( not 10>8 )   #--True--> Flase


# str="hello word"
# print('ee' in str)
# print('ee' not in str)
#
# list=[12,'你好呀',True,3.14,['皮卡丘','天天','妍妍']]  #定义一个空列表---往列表里添加元素
# # print(list[0:3])  #切片取值
# # print(list[4][0])  #列表的嵌套取值,取索引为0的字符串
# #增加
# list.append('小雪')        #追加到元素的末尾---最常用的
# list.insert(2,'伊呀呀呀')  #在指定的位置添加元素
# list.extend(['aaa','鲍鱼','卡罗尔'])  #一次添加多个元素，不是以整体添加的
# list.append(['aaa','鲍鱼','卡罗尔'])  #一次添加多个元素，是以整体添加的--列表的形式添加
# print(list)
#
# #修改
# list[0]='卡卡'     #添加索引为0的元素
# list[1]='123456'  #添加索引为1的元素
# list.insert(1,'卡卡')
# list.remove('卡卡')   #重复元素，只删除第一个遇见的元素
# list.insert(0,['卡卡','卡卡'])  #指定位置天机多个元素
# list.remove('卡卡')   #删除了不是整体的卡卡

# print(list.count('伊呀呀呀'))   #统计某个元素出现的次数
# print(len(list))


# tuple_1=('皮卡丘','南瓜','涵涵')  #取变量名如果用了内置函数的名字的话--调用这个内置函数时就会报错。
# # tuple1[0]='麦克' #指定修改会报错
# #转换---要想修改元素，可以转换成列表添加元素
# list1=list(tuple_1)  #元组-->列表
# list1.append('杰克')   #添加元素，在最末尾添加
# tuple_1=tuple(list1)  #列表-->元组
# print(tuple_1)

# dict1={'name':'皮卡丘','age':18,'weight':'80','height':160}
# print(dict1)
# #取值  ---
# print(dict1['name'],dict1['weight'])  #key取value
# print(dict1.get('weight'))  #get方法里面放的也是key
# #增加+修改
# dict1['gender']='Female'   #key不存在的话，则增加一个键值对  ---增加元素
# dict1['name']='卡卡'       #key存在的话，则改变value值
# #删除
# dict1.pop('gender')     #必须指定一个key来删除key:value
# #修改
# dict1.update({'city':'广州','hobby':'写代码'})   #增加 多个元素的时候---用update
# print(dict1)

# #集合 ：set --{} --无序
# list1=[11,22,33,44,55,88,99]  #含有重复数据的
# set1=set(list1)   #列表--->集合  =====去重操作
# print(set1)


#控制流
# money=int(input('输入金额：'))   #----input()  #输入的变量是字符串类型的----要转换为整型int
# if money>=600:
#     print('买大房子')
# elif money>=100:
#     print('买小房子')
# elif money==50:
#     print('买小车子')
# else:
#     print('继续搬砖')

#For循环
# str='今天学习了思维课程'  #定义了一个字符串变量
# count=0   #定义了一个计时器，用来计算循环次数的
# for item in str:
#     if(item=='天'):
#         # break
#         continue  #--中断，后面的还会执行，只跳出了本次循环
#     elif(item=='思'):
#         break   # ---中断，后面的不会再执行的，跳出了整个循环
#     print(item)
#     # print('*'*10)
    # count+=1  #每次循环，值自加1
    # print(count)   #打印循环次数
    # print(len(str))

# #range--开始（默认0），结束，步长（默认1）
# # for num in range(0,60,2):
# #     print(num)
# #
# name=input('请输入姓名：')
# age=input('请输入年龄：')
# sex=input('请输入性别：')
# print(
#     '''
# *********************
#       姓名：{1}
#       年龄：{2}
#       性别：{3}
# ********************  '''.format(name,age,sex,name)
#       )
#
#
# str1 = 'python hello aaa 123123aabb'
# # 1）请取出并打印字符串中的'python'。
# print(str1[0:7:1])
# # 2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
# print( 'o a' in str1)
# print( 'he' in str1)
# print( 'ab'in str1)
# # 3）替换python为 “lemon”.
# str1 =str1.replace('python','lemon')
# print(str1)
# # 4) 找到aaa的起始位置
# print(str1.index('aaa'))


# print("kjhjk")   #单元格里面的内容