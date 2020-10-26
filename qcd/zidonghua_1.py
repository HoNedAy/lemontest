#接口自动化步骤
# 1、excel测试用例准备好，代码自动读取数据
# 2、发送接口请求，得到响应结果
# 3、执行结果 vs预期结果  --断言  通过 不通过
# 4、写入最终的真实结果--execl表格里
#
# 第三方库：操作excel表格--openpyxl库，实现去excel表格里读取数据，数据的回写
# 1.安装：pip install openpyxl==或pycharm安装
# 2、导入 import openpyxl

# 注意：execl表格要跟python文件在同一级别
# execl表格三大对象：
# 1、工作簿对象
# 2、表格对象：sheet
# 3、单元格对象：cell
# print("kjhjk")   #单元格里面的内容
# import openpyxl
# wb1=openpyxl.load_workbook('jiekou.xlsx')  #加载工作簿--execl表格名字--内存
# # sheet=wb1["register"]
# #获取表单
# print(wb1.cell(1,0))
# cell=sheet.cell(row=1,column=1)  #通过表单获取行号、列号==单元格
# print("kjhjk")   #单元格里面的内容

#
# def good_job():  #定义一个函数
#     salaly=8000
#     bouns=2000
#     subsidy=500
#     sum1=salaly+bouns+subsidy
#     print('这个工资总和是{}'.format(sum1))
# good_job() #用函数名进行函数的调用--函才会执行

# def good_job(salaly,bouns,subsidy=10,*args,**kwargs):  #定义一个函数
#     sum1=salaly+bouns+subsidy
#     for i in args:
#         sum1+=i
#     for k in kwargs:   #遍历循环
#         sum1 +=kwargs[k]
#     return sum1,salaly     #定义了一个返回值
# result=good_job(100,100,100) #用函数名进行函数的调用--函数才会执行
# for res in result:
#     print(res)
# print('result----{}'.format(result))
# if res>=300:  #取最后那个进行计算
#     print('大于300')
# else:
#     print('小于300-')


# 1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面
#
# a=[1,2,'6','summer']
#
# print('i' in a)


# 2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
# dict_1={"class_id":45,'num':20}
# num=dict_1['num']  #方法一取值
# num1=dict_1.get('num')  #方法二取值
# if num>5:
#     print('课堂人数为：{}'.format(num))
# else:
#     print('课堂人数小于5')






# 注：num表示课堂人数。如果大于5，输出人数。
# 3、
# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。

# 并且把字典都存在新的 list中，最后打印最终的列表。
# 方法1： 手动扩充--字典--存放在列表里面；
# dict1={'姓名':'方方土','性别':'male','年龄':'18','城市':'广州'}
# dict2={'姓名':'七木','性别':'male','年龄':'18','城市':'广州'}
# dict3={'姓名':'荷花鱼','性别':'male','年龄':'18','城市':'广州'}
# dict4={'姓名':'kingo','性别':'male','年龄':'18','城市':'广州'}
# dict5={'姓名':'Amiee','性别':'male','年龄':'18','城市':'广州'}
# dict6={'姓名':'焕蓝','性别':'male','年龄':'18','城市':'广州'}
# list2=[dict1,dict2,dict3,dict4,dict5,dict6]
# print(list2)


# 方法2： 自动--dict（）

list3 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
list_null=[]  #新建一个空列表
list4 = ['male', 'male', 'female', 'male', 'female', 'male']
list5 = [18,19,20,21,22,23]
list6 = ['广州', '深圳', '上海', '长沙', '北京', '东莞']
print(list_null)
for i in range(6):
 dict_num=  dict(name=list3[i],sex=list4[i],age=list5[i],city=list6[i])  #字典
 # print(dict_num)
 list_null.append(dict_num)  #把字典复制给空列表
print(list_null)

# 1. 把字符串转成列表 - list()
# str='今天你学习了吗'
# list1=list(str)
# print(list1)
# 2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
# sum=0 #定义总和变量，用来存储相加的总数
# for i in range(10):
#     # print(i)
#     sum += i
#     print(sum)
# 3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
# def def_num(obj):
#     # if type(obj)==list or type(obj)==dict or type(obj)==str:   #判断类型方法一
#         if isinstance(obj,list)  or isinstance(obj,dict) or isinstance(obj,str):  # 判断类型方法二
#             if len(obj)>5:
#                 print(True)
#             else:
#                 print(False)
# def_num(["lgkhjglk",'ghjhg','h','h','hf','fdiuhf'])

