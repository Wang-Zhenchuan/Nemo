"王震川———————————————————————————————————————————————————————————————————————————Python"
# 代码必需一行行、一组组运行
# 就算你想运行整个文件也不可能
# 我在文件各处打了点小广告
# 年轻人，踏踏实实的，不好吗？不好吗？？不好吗？？？不好吗？？？？不好吗？？？？？？？？？？？？？
"输入输出————————————————————————————————王震川————————————————————————————————————Python"
#                                第一节：输入输出     BEGIN
"输入输出————————————————————————————————王震川————————————————————————————————————Python"
# （print）函数：输出函数
# （input）函数：输入函数
"输入输出—————————————————————————————————————————————————————————————————————————Python"
#                                         主要内容
# 本节主要讲了（print）函数和（input）函数
# 本节有两个扩展（print和input），讲到了下一节的变量与数据类型
# 本节有一个附件（格式化输出），讲到了下一节的变量与数据类型
"输入输出—————————————————————————————————————————————————————————————————————————Python"

"输入输出—————————————————————————————————————————————————————————————————————————Python"
#                                         目录
# 第一节：输入输出     BEGIN——————————————————————————————————————————————————————————7
# 正文     BEGIN————————————————————————————————————————————————————————————————————35
# 正文1  （print）函数——————————————————————————————————————————————————————————————38
# 扩展1（print）———————————————————————————————————————————————————————————————————84
# 正文2  （input）函数————————————————————————————————————————————————————————————136
# 扩展2（input）—————————————————————————————————————————————————————————————————144
# 正文     END——————————————————————————————————————————————————————————————————187
# 附件：格式化输出     BEGIN————————————————————————————————————————————————————194
# 附件：格式化输出     END—————————————————————————————————————————————————————322
# 第一节：输入输出     END————————————————————————————————————————————————————328
"输入输出—————————————————————————————————————————————————————————————————————————Python"



"输入输出—————————————————————————————————————————————————————————————————————————Python"
# 第一节：输入输出  正文   BEGIN


# 正文1  （print）函数
print("hello world")
print("hello,world")
print(1)
# ("")内有什么，就输出什么

print("hello","world")
print("hello" "world")
print("hello""world")
# 输出多个值，中间用逗号隔开
# 只有（,）在（""）外起分隔作用（输出后为空格）

print("hello"world")
# 一个字符串一对（""）

print("hello",",","world")
print("hello"",""world")
print("hello" "," "world")

print('hello')
print("hello')
print('hello")
# 只有（""）、（''）起作用

print(1*2)
print(1+2)
print(1-2)
print(1/2)

print("1"+"2")
print("1"-"2")
print("1"*"2")
# 用（""）括起来后为字符串，不能相互运算，但可以用（+）拼接

print("1"*2)
print("1"/2)
print("1"+2)
# 用（""）括起来后为字符串，不能与数字运算，但可以用（*）增加数量

print("1*2")
# 在（""）内仍可运算

print("1""*""2")
王震川—————————————————————————————————————————————————————————————————————————————Python
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川—————————————————————————————————————————————————————————————————————————————Python
# 扩展1（print）
print("2"+1)
print("2"+str(1))
print(int("2")+1)
print("2",1)
# 数字和字符串不能相互运算，但是字符串和数字可以互换数据类型后再输出

print("hello world")
print("hello world",sep="")
print("hello world",sep=" ")
print("hello world",sep=".")
print("hello world",sep=",")
print("hello world",sep=";")
# 函数（sep），Separate，分开、分隔
# 函数（sep）默认（sep=' '）

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
# 多行运行
print("hello world",end="\n")
print("hello world",end="\n")
print("hello world",end="\n")
print("hello world",end="\n")
print("hello world",end="\n")
# 多行运行，（\n)，换行符

print("hello world",end="")
print("hello world",end="")
print("hello world",end="")
print("hello world",end="")
print("hello world",end="")
# 多行运行
print("hello world",end=" ")
print("hello world",end=" ")
print("hello world",end=" ")
print("hello world",end=" ")
print("hello world",end=" ")
# 多行运行
print("hello world",end=",")
print("hello world",end=",")
print("hello world",end=",")
print("hello world",end=",")
print("hello world",end=",")
# 多行运行，函数（end），结尾、末端
# 函数（end）默认（end='\n'）
王震川—————————————————————————————————————————————————————————————————————————————Python
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川—————————————————————————————————————————————————————————————————————————————Python
# 正文2  （input）函数
input()
# 运行，发现程序并未结束，此时需要输入
# 否则，此函数会一直等待，程序卡死在此
# 输入字符后，回车，程序运行，程序结束
王震川—————————————————————————————————————————————————————————————————————————————Python
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川—————————————————————————————————————————————————————————————————————————————Python
# 扩展2（input）
a=input()1
print(a)
# （a），变量名

a=input()1
print("a")

input()
print()
# 没有规定输出、输入的是什么，不会输出输入结果

input()
print(a)
# 没有规定变量名，不会输出输入结果

a=input()
print()
# 没有规定输出的是什么，不会输出输入结果

a=input("请输入数字: ")
print(a)

a=input()
print("你输入的是:","a")

a=input("请输入数字:")
print("你输入的是:","a")
# 增加提示不会改变输入输出内容

a=input("请输入数字:")
print(a+5)
# 注意！！！变量a的值（输入内容）在代码中被（""）括起来了，数据类型为字符串，不能直接与数运算
# 注意！！！这一点运行时你有可能注意不到！！！！！！！！！！！！！！！！！！！！！！！！！！！

a=int(input("请输入数字: "))
print(a+5)
# 将输入的内容（变量的值）转换成int型（整数）后就可以运算了
王震川—————————————————————————————————————————————————————————————————————————————Python
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川—————————————————————————————————————————————————————————————————————————————Python
# 第一节：输入输出  正文   END
王震川—————————————————————————————————————————————————————————————————————————————Python



# 如果在输出的字符串中出现了变量，我们可以使用格式化输出的方式打印该变量
王震川—————————————————————————————————————————————————————————————————————————————Python
# 附件：格式化输出   BEGIN
王震川—————————————————————————————————————————————————————————————————————————————Python
# （一）fromat
# 该方法是使用字符串的str.format()的参数位置替换被（{}）占位的地方的数据，参数位置从0开始

# （1）直接写，不指定参数位置，则按先后顺序
print("我是{},我有{}块钱".format("王震川", 100))

print("我是(),我有()块钱".format("王震川", 100))
# （{}）不能替换为（()）

print("我是{},我有{}块钱",format("王震川", 100))
# （.）不能替换为（,）


# （2）使用变量，不指定参数位置，则按先后顺序
name = "王震川"
money = 100
print("我是{},我有{}块钱".format(name,money ))


# （3）指定参数位置
name = "王震川"
money = 100
print("我是{0},我有{1}块钱,我买了{1}个棒棒糖".format(name,money))

name = "王震川"
money = 100
print("我是{1},我有{2}块钱,我买了{2}个棒棒糖".format(name,money))
# 第1个变量参数位置为0，第2个变量参数位置为1……以此类推，第n个变量参数位置为(n+1)

name = "王震川"
money = 100
print("我是{0},我有{1}块钱,我买了{1}个棒棒糖".format(money,name))
王震川—————————————————————————————————————————————————————————————————————————————Python
# （format）比较麻烦，写法太长了，我们可以使用（%）替代
王震川—————————————————————————————————————————————————————————————————————————————Python
# （二）%


# （1）普通用法
name = "王震川"
money = 100
print("我是%s,我有%d块钱"%(name, money))
# 上面用到的（%s）、（%d）叫做占位符，不同类型的变量在格式化输出的时候使用的占位符不一样

name = "王震川"
money = 100
print("我是%s,我有%d块钱"(name, money))
# 变量和字符串之间不能没有（%）

name = "王震川"
money = 100
print("我是%s,我有%d块钱"%      (name, money))
print("我是%s,我有%d块钱"     %(name, money))
print("我是%s,我有%d块钱"     %      (name, money))
# （%）左边、右边可以有空格


# （2）常用的占位符
# 符号	         说明
# %c	  格式化字符和ASCII码
# %s	  格式化字符串
# %d、%u  格式化整数、格式化无符号整数
# %f	  格式化小数
# %o	  格式化无符号整数、格式化无符号八进制数
# %x、%X  格式化16进制数
# %e、%E  格式化科学计数法表示的浮点数


# （3）控制输出数据的变化
# 如：保留的小数或整数位数（位数不够是否用0补充）、数据类型、是否左对齐
name = "王震川"
money = 100.1415926
print("我是%s,我有%f亿资产"%(name, money))
# 正常输出

name = "王震川"
money = 100.1415926
print("我是%s,我有%5.4f亿资产"%(name, money))
# 保留5位整数，4位小数（浮点型类型下，整数保留无效）

name = "王震川"
money = 100.1415926
print("我是%s,我有%.8f亿资产"%(name, money))
# 指定保留8位小数（位数不够默认用0占位）

name = "王震川"
money = 100.1415126
print("我是%s,我有%d亿资产"%(name, money))
# 把浮点型当成整型输出

name = "王震川"
money = 100.1415126
print("我是%s,我有%5d亿资产"%(name, money))
# 把浮点型当成整型输出，保留5位整数（位数不够默认用空格占位）

name = "王震川"
money = 100.1415126
print("我是%s,我有%05d亿资产"%(name, money))
# 保留5位整数，规定不够就用0补充

name = "王震川"
money = 100.1415126
print("我是%s,我有%-5d亿资产"%(name, money))
# （-）表示左对齐（没有右对齐）

name = "王震川"
money = 100.1415126
print("我是%s,我有%+5d亿资产"%(name, money))
print("我是%s,我有%#5d亿资产"%(name, money))
# 这里只是顺便说一下像（%5d）里的5一样的数，右边不能加任何符号，否则无法运行下去；
# 但左边能加（-）、（+）和（#），（*）没有任何作用，（+）可在输出数据左边加上它
王震川—————————————————————————————————————————————————————————————————————————————Python
# %还是太麻烦了，Python在3.6之后，推出了更简单的f写法
王震川—————————————————————————————————————————————————————————————————————————————Python
# （三）f
# 如果只是想打印一个变量的话，完全可以使用f写法

name = "王震川"
money = 100.1415126
print(f"我是{name},我有{money}亿资产")
# 只需要在字符串前加一个f，然后在大括号里写变量名即可
王震川—————————————————————————————————————————————————————————————————————————————Python
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川王震川
王震川—————————————————————————————————————————————————————————————————————————————Python
# 附件：格式化输出   END
王震川—————————————————————————————————————————————————————————————————————————————Python
a=("177746835@outlook.com")
b=a
a=print("You can e-mail me at",b,sep=' wang')
王震川—————————————————————————————————————————————————————————————————————————————Python
#                                 第一节：输入输出     END
王震川—————————————————————————————————————————————————————————————————————————————Python
# This is Variable.Are you interested?("yes"or"no"?)
idea=input("yes or no: ")
if idea=="yes":
    print("Please come to the second section!")
#Oh,no!Sorry!!This is Conditional Statements!!Don't look at these strings of code!!!
王震川—————————————————————————————————————————————————————————————————————————————Python