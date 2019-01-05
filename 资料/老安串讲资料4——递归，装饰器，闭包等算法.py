# 三.递归 ，装饰器，闭包等算法
# 1.有一对兔子，从出生后第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，加入兔子都不死，问一年之后总共有多少兔子
# 递归算法实现
# 递归算法实现计算每月兔子数
def fib_year(m):
    if m == 1:
        return 1
    elif m == 2:
        return 1
    else:
        return fib_year(m-1) + fib_year(m-2)
# 功能函数：计算一年之后总共的兔子数
def rib_num():
    l = []
    for i in range(1,13):
        num = fib_year(i)
        l.append(num)
    print('一年之后一共有：%d只兔子。'%(2*sum(l)))
rib_num()
# 2.输出一个斐波那契数列
# 递归算法计算每一个斐波那契数
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 功能函数：形成斐波那契数列
def make_fib():
    l = []
    m = int(input("您想生成几个数的斐波那契数列呢？请输入："))
    for i in range(1,m+1):
        num = fib(i)
        l.append(num)
    print('生成的斐波那契数列为：%s'%l)
make_fib()
#
# 3.青蛙跳台阶问题。
# 	1.一个青蛙，一次可以跳上1级台阶，也可以跳上2级台阶。问青蛙跳上一个n级台阶总共有多少种跳法
# 	2.一个青蛙，一次可以跳上1级台阶，也可以跳上2级台阶……也可以跳上n级台阶。问青蛙跳上一个n级台阶总共有多少种跳法
# 原始方法：
# 问题1
def fib(n):
    if n == 0:
        return "不合法！"
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))

# 问题2
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return 2 * fib(n-1)


print(fib(4))



#此代码示例为：将两种青蛙跳问题采用面向对象思想进行实现
import sys

# 单例模式
class Fib:
    def __init__(self):
        print("现有如下两个问题：")
        print("1.一只青蛙一次可以跳上１级台阶，也可以跳上２级。求该青蛙跳上一个n级台阶总共有多少种跳法")
        print("2.一只青蛙一次可以跳上１级台阶，可以跳上２级台阶，......，也可以跳上n级台阶。求该青蛙跳上一个n级台阶总共有多少种跳法")
        print("--------------------------------------------------------------------------------------")
        print("您要实现哪个问题呢？")
        self.choose = int(input("请选择："))
        try:
            self.num = int(input("请输入青蛙跳的台阶次数："))
        except ValueError:
            print("您输入的台阶数不合法，只能输入整型，请重新输入！")
            sys.exit()

        else:
            print("值合法！程序继续运行！")


    def work_one(self,num):
        if num == 0:
            return "您输入的台阶数不合法，请重新输入！"
        elif num == 1:
            return 1
        elif num == 2:
            return 2
        else:
            return self.work_one(num - 1) + self.work_one(num - 2)

    def work_two(self,num):
        if num == 0:
            return 1
        elif num == 1:
            return 1
        else:
            return 2 * self.work_two(num-1)

    def work(self,choose):
        if choose == 1:
            print("第一个问题的答案：")
            print("青蛙跳上一个%d级台阶总共有%d种方法。"%(self.num,self.work_one(self.num)))
        if choose == 2:
            print("第二个问题的答案：")
            print("青蛙跳上一个%d级台阶总共有%d种方法。" % (self.num, self.work_two(self.num)))

fib = Fib()

fib.work(fib.choose)
# 4.猴子吃桃：有一堆桃子，猴子第一天吃了一半，还不过瘾，又吃了一个，第二天将剩下的桃子又吃了一半，
# 还不过瘾，又吃了一个，以后的每天早上都吃了前一天剩下的桃子的一半多一个，
# 到第十天早上再想吃的时候，发展只有一个桃子了，求原来有多少桃子
# 基础算法实现
x = 1
for i in range(9,0,-1):
    x = 2*(x+1)
print("原来有%d个桃子"%x)

# 闭包封装基本功能
def out_():
    x = 1
    def in_():
        nonlocal x
        for i in range(9,0,-1):
            x = 2 * (x + 1)
        print("原来有%d个桃子"%x)
    return in_
monkey = out_()
monkey()
# 递归实现功能
def monkey(x,day):
    day -= 1
    if day == 0:
        return x
    x = 2 * (x + 1)
    return monkey(x,day)
print('原来有%d个桃子'%monkey(1,10))
# 闭包实现递归功能
def out_():
    x = 1
    day = 10
    def in_():
        nonlocal x, day
        day -= 1
        if day == 0:
            return x
        x = 2 * (x + 1)
        return in_()
    return in_
monkey = out_()
num = monkey()
print('原来有%d个桃子'%num)
# 对象实现功能
class Monkey:
    def __init__(self):
        self.x = 1
        self.day = 10
    def monkey(self):
        self.day -= 1
        if self.day == 0:
            return self.x
        self.x = 2 * (self.x + 1)
        return self.monkey()
monkey = Monkey()
num = monkey.monkey()
print('原来有%d个桃子'%num)
# 5.实现任意一个数的阶乘
# 基础算法实现
def factorial(x):
    res = x
    for i in range(1,x):
        res *= i
        print(res)
    return res
num = int(input('请输入一个正整数：'))
result = factorial(num)
print(result)
# 递归算法实现
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
num = int(input('请输入一个正整数：'))
result = factorial(num)
print(result)


# 6.动态生成一个列表，调用启动函数启动程序，用户输入1，执行列表排序功能，用户输入2，执行列表反序功能，用户输入3，执行列表去重功能，用户输入4，实现分割功能。
		# 拓展：使用装饰器实现
l = []
def create_list():
    print("游戏开始！请输入数字，用来生成你想要的列表：")
    while True:
        num = int(input("请输入："))
        if num == 0:
            break
        l.append(num)
    return l
print("恭喜！您输入的列表:\nl = %r"%create_list())
print("生成成功！请进行下一步操作！")
print('')
print("----------------------------\n|当前小程序包含四部分功能：|\n| 1.列表排序功能;          |\n| 2.列表去重功能;          | \n| 3.列表反序功能;          |\n| 4.列表分割功能;          |\n----------------------------\n请选择您想要的功能，输入序号即可！")
list_num = int(input("请输入："))

#排序功能

def SORT_LIST(fn):
    def sort_list():
        for i in range(len(l)-1):
            for j in range(len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j],l[j+1] = l[j+1],l[j]
        print(l)
    return sort_list

#去重功能

def DELETE_REPEAT(fn):
    def delete_repeat():
        newL = []
        for i in l:
            if i not in newL:
                newL.append(i)
        print(newL)
    return delete_repeat

#反序功能

def REVERSE(fn):
    def reverse_list():
        print(l[::-1])
    return reverse_list

if list_num == 1:
    @SORT_LIST
    def start():
        pass
elif list_num == 2:
    @DELETE_REPEAT
    def start():
        pass
elif list_num == 3:
    @REVERSE
    def start():
        pass
start()