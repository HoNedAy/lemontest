
from qcd import test  #导入函数文件
from test_date import date  #导入测试数据文件
from  selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)

#调用函数--1、先把函数调用出来  2、传参到函数调用里
url=date.url['url']  #取值url
username=date.login_date["username"]  #取值登录名
password=date.login_date["password"]  #取值密码
s_key=date.s_key["s_key"] #取值搜索的关键字

#1、函数的调用--传参
#2、定义了一个放回值--调用的时候用一个变量来接受返回值
result=test.search_key(driver=driver,url=url,username=username,password=password,s_key=s_key)

print(result)
if s_key in result:
    print("搜索结果是正确的")
else:
    print("用例测试不通过")


