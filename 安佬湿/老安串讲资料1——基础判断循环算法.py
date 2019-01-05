# 1.输入一个数字，判断输入的数字是奇数还是偶数
#基础算法实现
num = int(input("请输入一个数字："))
if num % 2 == 0:
    print("您输入的数字是偶数")
else:
    print("您输入的数字是奇数")

# 函数封装功能
def if_num():
    num = int(input("请输入一个数字："))
    if num % 2 == 0:
        print("您输入的数字是偶数")
    else:
        print("您输入的数字是奇数")
    return num
if_num()

# 闭包封装功能
def out_num():
    num = int(input("请输入一个数字："))
    def if_num():
        nonlocal num
        if num % 2 == 0:
            print("您输入的数字是偶数")
        else:
            print("您输入的数字是奇数")
        return num
    return if_num
in_num = out_num()
in_num()

# 对象封装功能
class If_num:
    def __init__(self):
        self.num = int(input("请输入一个数字："))
    def if_num(self):
        if self.num % 2 == 0:
            print("您输入的数字是偶数")
        else:
            print("您输入的数字是奇数")
in_out = If_num()
in_out.if_num()

# 2.输入一个年份，判断输入的年份是闰年还是平年
# 基础算法实现
year = int(input("请输入一个年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("您输入的年份是闰年!")
else:
    print("您输入的年份是平年!")

# 函数封装功能
def is_run():
    year = int(input("请输入一个年份："))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("您输入的年份是闰年!")
    else:
        print("您输入的年份是平年!")
is_run()

# 闭包封装功能
def out_run():
    year = int(input("请输入一个年份："))
    def in_run():
        nonlocal year
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("您输入的年份是闰年!")
        else:
            print("您输入的年份是平年!")
    return in_run
is_run = out_run()
is_run()

# 对象封装功能
class Is_run:
    def __init__(self):
        self.year = int(input("请输入一个数字："))
    def isReady_run(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            print("您输入的年份是闰年!")
        else:
            print("您输入的年份是平年!")
is_run = Is_run()
is_run.isReady_run()

# 3.形如ABCCBA形式的字符串我们都叫做回文字符。请问，如何判断输入的某个字符是回文字符？
# 基础算法实现
str = input("请输入一个字符串：")
if str[::-1] == str:
    print("您输入的字符串是回文字符")
else:
    print("您输入的字符串不是回文字符")

# 函数封装功能
def is_hui():
    str = input("请输入一个字符串：")
    if str[::-1] == str:
        print("您输入的字符串是回文字符")
    else:
        print("您输入的字符串不是回文字符")
is_hui()

# 闭包封装功能
def out_hui():
    str = input("请输入一个字符串：")
    def in_hui():
        nonlocal str
        if str[::-1] == str:
            print("您输入的字符串是回文字符")
        else:
            print("您输入的字符串不是回文字符")
    return in_hui
is_hui = out_hui()
is_hui()
# 对象封装功能
class Is_hui:
    def __init__(self):
        self.str = input("请输入一个字符串：")
    def isReady_hui(self):
        if self.str[::-1] == self.str:
            print("您输入的字符串是回文字符")
        else:
            print("您输入的字符串不是回文字符")
is_hui = Is_hui()
is_hui.isReady_hui()
# 4.输出100以内的所有的质数（素数）
# 基础算法实现
for i in range(2,101):
    count = 0
    for j in range(2,i-1):
        if i % j == 0:
            count = 1
            break
    if count == 0:
        print(i)
# 函数封装功能
def isSushu():
    for i in range(2,101):
        count = 0
        for j in range(2,i-1):
            if i % j == 0:
                count = 1
                break
        if count == 0:
            print(i)
isSushu()

# 闭包封装功能
def out_Is():
    it = [x for x in range(2,101)]
    def in_Is():
        # nonlocal it
        for i in it:
            count = 0
            for j in range(2,i-1):
                if i % j == 0:
                    count = 1
                    break
            if count == 0:
                print(i)
    return in_Is
is_sushu = out_Is()
is_sushu()

# 对象封装功能
class Is_Su:
    def __init__(self):
        self.it = [x for x in range(2,101)]
    def is_sushu(self):
        for i in self.it:
            self.count = 0
            for j in range(2,i-1):
                if i % j == 0:
                    self.count = 1
                    break
            if self.count == 0:
                print(i)
ok = Is_Su()
ok.is_sushu()
# 5.有1,2,3,4四个数字，请问能组成多少个互不相同且无重复数字的三位数？
# 基础算法实现
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print(i,j,k)

# 函数封装功能
def is_Num():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and i != k and j != k:
                    print(i,j,k)
is_Num()

# 改为闭包
def out_is():
    it = range(1,5)
    def in_is():
        nonlocal it
        for i in it:
            for j in it:
                for k in it:
                    if i != j and i != k and j != k:
                        print(i,j,k)
    return in_is
ok = out_is()
ok()
# 6.输入三个整数，请把这三个数由小到大的输出（要求使用最简单的逻辑算法）
# 基础算法实现
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))
print((a if a > c else c)if a > b else (b if b > c else c))
# 函数封装功能
def is_max():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    c = int(input("请输入第三个数字："))
    print((a if a > c else c)if a > b else (b if b > c else c))
is_max()
# 闭包封装功能
def out_max():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    c = int(input("请输入第三个数字："))
    def in_max():
        nonlocal a,b,c
        print((a if a > c else c) if a > b else (b if b > c else c))
    return in_max
is_max = out_max()
is_max()
# 对象封装功能
class Is_Max:
    def __init__(self):
        self.a = int(input("请输入第一个数字："))
        self.b = int(input("请输入第二个数字："))
        self.c = int(input("请输入第三个数字："))
    def is_max(self):
        print((self.a if self.a > self.c else self.c) if self.a > self.b else (self.b if self.b > self.c else self.c))
is_max = Is_Max()
is_max.is_max()
# 7.输出9*9乘法口诀
# 基础算法实现
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s'%(i,j,i*j),end=" ")
    print()
# 函数封装功能
def mul_list():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end=" ")
    print()
mul_list()
# 闭包封装功能
def out_():
    it = range(1,10)
    def in_():
        nonlocal it
        for i in it:
            for j in it:
                print('%s*%s=%s'%(i,j,i*j),end=" ")
                if j > i:
                    break
            print()
    return in_
mul_list = out_()
mul_list()

# 8. .输出1000以内所有的水仙花数。水仙花数：是指一个三位数，其各位数字的立方和等于这个数本身
# 基础算法实现
for i in range(100,1000):
    if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
        print(i)
# 函数封装功能
def flower():
    for i in range(100,1000):
        if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
            print(i)
flower()
# 闭包封装功能
def out_():
    it = range(100,1000)
    def in_():
        nonlocal it
        for i in it:
            if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
                print(i)
    return in_
flower = out_()
flower()
# 对象封装功能
class Flower:
    def __init__(self):
        self.it = range(100,1000)
    def flower(self):
        for i in self.it:
            if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
                print(i)
flower = Flower()
flower.flower()
# 9.将一个正整数进行分解质因数
# 基础算法实现
n = num = int(input("请输入一个数字："))
l = []
for i in range(num // 2 + 1):
    for j in range(2,n):
        if n % j == 0:
            l.append(j)
            n //= j
            break
if len(l) == 0:
    print('没有质因数！')
else:
    l.append(n)
    print('%d = %d'%(num,l[0]),end=' ')
    for x in range(1,len(l)):
        print('*%d'%l[x],end=' ')
# 函数封装功能
def fenjie():
    n = num = int(input("请输入一个数字："))
    l = []
    for i in range(num // 2 + 1):
        for j in range(2, n):
            if n % j == 0:
                l.append(j)
                n //= j
                break
    if len(l) == 0:
        print('没有质因数！')
    else:
        l.append(n)
        print('%d = %d' % (num, l[0]), end=' ')
        for x in range(1, len(l)):
            print('*%d' % l[x], end=' ')
fenjie()
# 对象封装功能
class Fenjie(object):
    def __init__(self):
        self.n = self.num = int(input("请输入一个数字："))
        self.l = []
    def fenjie(self):
        for i in range(self.num // 2 + 1):
            for j in range(2, self.n):
                if self.n % j == 0:
                    self.l.append(j)
                    self.n //= j
                    break
        if len(self.l) == 0:
            print('没有质因数！')
        else:
            self.l.append(self.n)
            print('%d = %d' % (self.num, self.l[0]), end=' ')
            for x in range(1, len(self.l)):
                print('*%d' % self.l[x], end=' ')