# 1.随意输入一行字符，分别统计出其中空格，数字和下划线的个数
# 基本功能实现
num_tric = 0
num_num = 0
num__ = 0
s_str = input("请输入一串字符：")
for i in s_str:
    if i == ' ':
        num_tric += 1
    try:
        is_int = int(i)
    except ValueError:
        pass
    else:
        num_num += 1
    if i  == '_':
        num__+=1

print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n"%(num_tric,num_num,num__))

# 函数封装功能
def is_str():
    num_tric = 0
    num_num = 0
    num__ = 0
    s_str = input("请输入一串字符：")
    for i in s_str:
        if i == ' ':
            num_tric += 1
        try:
            is_int = int(i)
        except ValueError:
            pass
        else:
            num_num += 1
        if i == '_':
            num__ += 1

    print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n" % (num_tric, num_num, num__))
is_str()

# 闭包封装功能

def out_():
    num_tric = 0
    num_num = 0
    num__ = 0
    s_str = input("请输入一串字符：")
    def in_str():
        nonlocal num_num,num__,s_str,num_tric
        for i in s_str:
            if i == ' ':
                num_tric += 1
            try:
                is_int = int(i)
            except ValueError:
                pass
            else:
                num_num += 1
            if i == '_':
                num__ += 1
        print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n" % (num_tric, num_num, num__))
    return is_str
is_str = out_()
is_str()

# 对象封装功能
class Is_str:
    def __init__(self):
        self.num_tric = 0
        self.num_num = 0
        self.num__ = 0
        self.s_str = input("请输入一串字符：")
    def begin_is(self):
        for i in self.s_str:
            if i == ' ':
                self.num_tric += 1
            try:
                self.is_int = int(i)
            except ValueError:
                pass
            else:
                self.num_num += 1
            if i == '_':
                self.num__ += 1
            print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n" % (self.num_tric, self.num_num, self.num__))
is_str = Is_str()
is_str.begin_is()
# 2.一个球从100米的高度自由落体，每次落地后反弹回原高度的一半，求它在第十次落地之后，共经过多少米（排除所有误差存在）第十次反弹的高度为多少
# 基础算法实现
height = 100
times = 10
total_s = []
height_finally = height
while len(total_s) < times:
    total_s.append(height * 2)
    height_finally /= 2
print(sum(total_s)-height)
print(height_finally)

# 函数封装功能

def hei_cal():
    height = 100
    times = 10
    total_s = []
    height_finally = height
    while len(total_s) < times:
        total_s.append(height * 2)
        height_finally /= 2
    print(sum(total_s) - height)
    print(height_finally)
hei_cal()

# 闭包封装功能

def out_():
    height = 100
    times = 10
    total_s = []
    height_finally = height
    def in_():
        nonlocal height_finally,height,times,total_s
        while len(total_s) < times:
            total_s.append(height * 2)
            height_finally /= 2
        print(sum(total_s) - height)
        print(height_finally)
hei_cal = out_()
hei_cal()

# 对象封装功能
class Height_cal:
    def __init__(self):
        self.height = 100
        self.times = 10
        self.total_s = []
        self.height_finally = self.height
    def hei_cal(self):
        while len(self.total_s) < self.times:
            self.total_s.append(self.height * 2)
            self.height_finally /= 2
        print(sum(self.total_s) - self.height)
        print(self.height_finally)
hei_cal = Height_cal()
hei_cal.hei_cal()

# 3.手写冒泡排序算法
# 基础算法实现
l = [9,8,6,5,3]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)

# 函数封装实现

def bubble_sort():
    l = [9, 8, 6, 5, 3]
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print(l)
bubble_sort()

# 闭包封装实现

def out_():
    l = [9,7,5,4]
    def in_():
        nonlocal l
        for i in range(len(l) - 1):
            for j in range(len(l) - 1 - i):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
        print(l)
    return in_
bubble_sort = out_()
bubble_sort()

# 对象封装实现

class Bubble_sort:
    def __init__(self):
        self.l = [9,7,5,4]
    def bubble_sort(self):
        for i in range(len(self.l) - 1):
            for j in range(len(self.l) - 1 - i):
                if self.l[j] > self.l[j + 1]:
                    self.l[j], self.l[j + 1] = self.l[j + 1], self.l[j]
        print(self.l)
bubble_sort = Bubble_sort()
bubble_sort.bubble_sort()
#
# 4.动态生成一个列表
# 基础算法实现
l = []
while True:
    num = int(input("请输入一个数字："))
    if num == '0':
        break
    l.append(num)
print(l)

# 函数封装功能

def make_list():
    l = []
    while True:
        num = int(input("请输入一个数字："))
        if num == '0':
            break
        l.append(num)
    print(l)
make_list()

# 闭包封装功能

def out_():
    l = []
    def in_():
        nonlocal l
        while True:
            num = int(input("请输入一个数字："))
            if num == '0':
                break
            l.append(num)
        print(l)
    return in_
make_list = out_()
make_list()

# 对象封装功能
class Make_list:
    def __init__(self):
        self.l = []
    def make_list(self):
        while True:
            num = int(input("请输入一个数字："))
            if num == '0':
                break
            self.l.append(num)
        print(self.l)
make_list = Make_list()
make_list.make_list()

# 5.将一个列表进行反序
# 基础算法实现
l = [4,5,3,2]
newL = l[::-1]
print(newL)
# 函数封装功能
def res():
    l = [4, 5, 3, 2]
    newL = l[::-1]
    print(newL)
res()
# 闭包封装功能
def out_():
    l = [4, 5, 3, 2]
    def in_():
        nonlocal l
        newL = l[::-1]
        print(newL)
    return in_
res = out_()
res()
# 对象封装功能
class Res:
    def __init__(self):
        self.l = [3,2,4,5]
    def res(self):
        self.newL = self.l[::-1]
        print(self.newL)
res = Res()
res.res()

# 6.去除一个列表中重复的元素
# 基础算法实现
l = [2,2,3,3,5,6,7,5]
newL = []
for i in l:
    if i not in newL:
        newL.append(i)
print(newL)
# 函数封装功能实现
def rep():
    l = [2, 2, 3, 3, 5, 6, 7, 5]
    newL = []
    for i in l:
        if i not in newL:
            newL.append(i)
    print(newL)
rep()
# 闭包封装功能
def out_():
    l = [2, 2, 3, 3, 5, 6, 7, 5]
    newL = []
    def in_():
        nonlocal l, newL
        for i in l:
            if i not in newL:
                newL.append(i)
        print(newL)
    return in_
rep = out_()
rep()
# 对象封装功能
class Rep:
    def __init__(self):
        self.l = [2, 2, 3, 3, 5, 6, 7, 5]
        self.newL = []
    def rep(self):
        for i in self.l:
            if i not in self.newL:
                self.newL.append(i)
        print(self.newL)
rep = Rep()
rep.rep()

# 7.现有一个序列，这个序列是用户随机输入的一串字符（降低难度，用户只会输入26个小写字母的随机排列）。问当前用户输入的字符中出现次数最多的字符是谁，并统计次数
# 基础算法实现
l = []
dic = {}
while True:
    num = input("请输入一个字符：")
    if num == "over":
        break
    l.append(num)
for i in l:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
iMax = 0
iIndex = ''
for key in dic:
    if dic[key] > iMax:
        iMax = dic[key]
        iIndex = key
print("出现次数最多的字符是：%s,总共出现了：%d次"%(iIndex,iMax))
# 函数封装功能
def is_max():
    l = []
    dic = {}
    while True:
        num = input("请输入一个字符：")
        if num == "0":
            break
        l.append(num)
    for i in l:
        if i not in dic:
            dic[i] = 0
        else:
            dic[i] += 1
    # print(dic)
    iMax = 0
    iIndex = ''
    for key in dic:
        if dic[key] > iMax:
            iMax = dic[key]
            iIndex = key
    print("出现次数最多的字符是：%s,总共出现了：%d次"%(iIndex,iMax))

is_max()
# 闭包封装功能
def out_():
    l = []
    dic = {}
    iMax = 0
    iIndex = ''
    def in_():
        nonlocal l,dic,iMax,iIndex
        while True:
            num = input("请输入一个字符：")
            if num == "0":
                break
            l.append(num)
        for i in l:
            if i not in dic:
                dic[i] = 0
            else:
                dic[i] += 1
        print(dic)
        for key in dic:
            if dic[key] > iMax:
                iMax = dic[key]
                iIndex = key
    return in_
is_max = out_()
is_max()
# 对象封装功能
class Is_max:
    def __init__(self):
        self.l = []
        self.dic = {}
        self.iMax = 0
        self.iIndex = ''
    def is_max(self):
        while True:
            num = input("请输入一个字符：")
            if num == "0":
                break
            self.l.append(num)
        for i in self.l:
            if i not in self.dic:
                self.dic[i] = 0
            else:
                self.dic[i] += 1
        print(self.dic)
        for key in self.dic:
            if self.dic[key] > self.iMax:
                self.iMax = self.dic[key]
                self.iIndex = key
        print("出现次数最多的字符是：%s,总共出现了：%d次" % (self.iIndex, self.iMax))
is_max = Is_max()
is_max.is_max()

# 8.现有一个降序排列的列表，用户输入一个数字，将其插入列表中形成一个新的降序排序的列表
# 基础算法实现
l = []
while True:
    num = int(input("请输入一个字符："))
    if num == 0:
        break
    l.append(num)
print(l)
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] < l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)

insert_num = int(input("请输入您想插入的数字："))
for k in range(len(l)):
    if insert_num <= l[-1]:
        l.append(insert_num)
        break
    elif insert_num >= l[0]:
        l.insert(0,insert_num)
        break
    elif insert_num < l[k] and insert_num > l[k+1]:
        l.insert(k+1,insert_num)
        break
    elif insert_num == l[k]:
        l.insert(k,insert_num)
        break
print(l)
# 函数封装功能
def insert_num():
    l = []
    while True:
        num = int(input("请输入一个字符："))
        if num == 0:
            break
        l.append(num)
    print(l)
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print(l)

    insert_num = int(input("请输入您想插入的数字："))
    for k in range(len(l)):
        if insert_num <= l[-1]:
            l.append(insert_num)
            break
        elif insert_num >= l[0]:
            l.insert(0, insert_num)
            break
        elif insert_num < l[k] and insert_num > l[k + 1]:
            l.insert(k + 1, insert_num)
            break
        elif insert_num == l[k]:
            l.insert(k, insert_num)
            break
    print(l)
insert_num()
# 闭包封装功能
def out_():
    l = []
    def in_():
        nonlocal l
        while True:
            num = int(input("请输入一个字符："))
            if num == 0:
                break
            l.append(num)
        print(l)
        for i in range(len(l) - 1):
            for j in range(len(l) - 1 - i):
                if l[j] < l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
        print(l)

        insert_num = int(input("请输入您想插入的数字："))
        for k in range(len(l)):
            if insert_num <= l[-1]:
                l.append(insert_num)
                break
            elif insert_num >= l[0]:
                l.insert(0, insert_num)
                break
            elif insert_num < l[k] and insert_num > l[k + 1]:
                l.insert(k + 1, insert_num)
                break
            elif insert_num == l[k]:
                l.insert(k, insert_num)
                break
        print(l)
    return in_
insert_num = out_()
insert_num()
# 对象封装功能（通过对象间的继承关系实现功能整合）
class Make_list:
    def __init__(self):
        self.l = []
    def make_list(self):
        while True:
            num = int(input("请输入一个字符："))
            if num == 0:
                break
            self.l.append(num)
        return self.l

class Bubble_sort:
    def bubble_sort(self,make_over_list):
        for i in range(len(make_over_list) - 1):
            for j in range(len(make_over_list) - 1 - i):
                if make_over_list[j] < make_over_list[j + 1]:
                    make_over_list[j], make_over_list[j + 1] = make_over_list[j + 1], make_over_list[j]
        return make_over_list
class Insert_number:
    def insert_number(self,bubble_sort_over_list):
        insert_num = int(input("请输入您想插入的数字："))
        for k in range(len(bubble_sort_over_list)):
            if insert_num <= bubble_sort_over_list[-1]:
                bubble_sort_over_list.append(insert_num)
                break
            elif insert_num >= bubble_sort_over_list[0]:
                bubble_sort_over_list.insert(0, insert_num)
                break
            elif insert_num < bubble_sort_over_list[k] and insert_num > bubble_sort_over_list[k + 1]:
                bubble_sort_over_list.insert(k + 1, insert_num)
                break
            elif insert_num == bubble_sort_over_list[k]:
                bubble_sort_over_list.insert(k, insert_num)
                break
        return bubble_sort_over_list
if __name__ == '__main__':
    finally_list = Make_list().make_list()
    bubble_list = Bubble_sort().bubble_sort(finally_list)
    insert_list = Insert_number().insert_number(bubble_list)
    print("插入后的列表为：%r"%insert_list)

# 9.初始化一个列表，将最大的数与第一个数交换位置，最小的数与最后一个数交换位置，输出交换之后的列表
# 基础算法实现
l = []
while True:
    num = int(input("请输入一个字符："))
    if num == 0:
        break
    l.append(num)
print(l)
for k in range(len(l)):
    max_num = max(l)
    min_num = min(l)
    max_num,l[0] = l[0],max_num
    min_num,l[-1] = l[-1],min_num
print(l)

# 10.有n个人围成一圈，顺序排号。从第一个人开始报数（1~3报数），凡报到3的人退出圈子，问最后留下的人原来排在第几号。
num = int(input("请输入人数："))
k = 0#计算报数
#根据人数生成列表，列表包含num个数，代表有num个人，num的值代表每个人的编号
l = [x for x in range(1,num+1)]
# print(l)
while len(l) > 1:
    l_copy = l[:]
    for i in range(0,len(l_copy)):
        k += 1
        if k % 3 == 0:
            l.remove(l_copy[i])
print("最后留下来的是原来的第%d号兄弟"%l[0])

#面向对象

class Remove():
    def __init__(self):
        self.num = int(input("请输入你想要的人数："))
        self.count = 0

    def make_list(self):
        self.L = [x for x in range(1,self.num+1)]
        return self.L

    def remove_number(self):
        self.make_list()
        while len(self.L) > 1:
            self.L_copy = self.L[:]
            for i in range(0,len(self.L_copy)):
                self.count += 1
                if self.count % 3 == 0:
                    self.L.remove(self.L_copy[i])
        return self.L

rm = Remove()
print("最后留下来的是原来的第%d号兄弟"%rm.remove_number()[0])
