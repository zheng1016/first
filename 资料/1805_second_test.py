# 1.第一种
import random
import math
# def list_work():
#     l = []
#     newl = []
#     while True:
#         random_num = math.floor(random.random()*50+1)
#         l.append(random_num)
#         if len(l) == 10:
#             break
#     print(l)
#     for i in range(len(l)-1):
#         for j in range(len(l)-1-i):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1] =l[j+1],l[j]
#     print(l)
#     for x in l:
#         if x not in newl:
#             newl.append(x)
#     print(newl)
# list_work()
# 第二种
# def make_list():
#     l = []
#     while True:
#         random_num = math.floor(random.random()*50+1)
#         l.append(random_num)
#         if len(l) == 10:
#             break
#     return l
# # print(make_list())
# def bubble_sort(l):
#     for i in range(len(l)-1):
#         for j in range(len(l)-1-i):
#             if l[j] > l[j + 1]:
#                 l[j],l[j+1] =l[j+1],l[j]
#     return l
# def list_repeat(l):
#     newl = []
#     for i in l:
#         if i not in newl:
#             newl.append(i)
#     return newl
# def main():
#     random_list = make_list()
#     after_bubble_sort_list = bubble_sort(random_list)
#     finall_list = list_repeat(after_bubble_sort_list)
#     print(finall_list)
# main()

# 2.第一种
# def clear_boy():
#     num = int(input("请输入人数："))
#     k = 0#计算报数
#     #根据人数生成列表，列表包含num个数，代表有num个人，num的值代表每个人的编号
#     l = [x for x in range(1,num+1)]
#     # print(l)
#     while len(l) > 1:
#         l_copy = l.copy()
#         for i in range(0,len(l_copy)):
#             k += 1
#             if k % 3 == 0:
#                 l.remove(l_copy[i])
#     print("最后留下来的是原来的第%d号兄弟"%l[0])
# clear_boy()

# 第二种
# def out_():
#     num = int(input("请输入人数："))
#     k = 0  # 计算报数
#     # 根据人数生成列表，列表包含num个数，代表有num个人，num的值代表每个人的编号
#     l = [x for x in range(1, num + 1)]
#     def in_():
#         nonlocal num,k,l
#         while len(l) > 1:
#             l_copy = l.copy()
#             for i in range(0,len(l_copy)):
#                 k += 1
#                 if k % 3 == 0:
#                     l.remove(l_copy[i])
#         print("最后留下来的是原来的第%d号兄弟"%l[0])
#     return in_
# clear_boy = out_()
# clear_boy()

# 3.第一种，基本功能实现
# l = []
# dic = {}
# while True:
#     num = input("请输入一个字符：")
#     if num == "over":
#         break
#     l.append(num)
# for i in l:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)
# iMax = 0
# iIndex = ''
# for key in dic:
#     if dic[key] > iMax:
#         iMax = dic[key]
#         iIndex = key
# print("出现次数最多的字符是：%s,总共出现了：%d次"%(iIndex,iMax))

# 第二种，函数封装功能
# def max_code():
#     l = []
#     dic = {}
#     while True:
#         num = input("请输入一个字符：")
#         if num == "over":
#             break
#         l.append(num)
#     for i in l:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#     print(dic)
#     iMax = 0
#     iIndex = ''
#     for key in dic:
#         if dic[key] > iMax:
#             iMax = dic[key]
#             iIndex = key
#     print("出现次数最多的字符是：%s,总共出现了：%d次" % (iIndex, iMax))
#
# max_code()

# 第三种，函数分离功能
# def make_list():
#     l = []
#     while True:
#         num = input("请输入一个字符：")
#         if num == "over":
#             break
#         l.append(num)
#     return l
# def make_dic(l):
#     dic = {}
#     for i in l:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#     return dic
# def max_code(dic):
#     iMax = 0
#     iIndex = ''
#     for key in dic:
#         if dic[key] > iMax:
#             iMax = dic[key]
#             iIndex = key
#     print("出现次数最多的字符是：%s,总共出现了：%d次" % (iIndex, iMax))
# def main():
#     # init_list = make_list()
#     # init_dic = make_dic(make_list())
#     # max_code(init_dic)
#     max_code(make_dic(make_list()))
# main()

# import sys as s
#
# # 4.答案：
# def make_random():
#     l = []
#     while True:
#         random_num = math.floor(random.random()*30+1)
#         l.append(random_num)
#         if len(l) == 4:
#             break
#     return l
# def buy_caipiao():
#     l = []
#     while True:
#         try:
#             num = int(input("请输入列表的元素，元素值类型为整型："))
#         except ValueError:
#             print("您输入的元素的值类型不是整型！请重新输入！")
#             s.exit()
#         if num == 0:
#             break
#         l.append(num)
#     return l
#
# def check(random_list,user_caipiao):
#     count = 0
#     for i in user_caipiao:
#         if i in random_list:
#             count += 1
#     return count
#
# def result():
#     random_list = make_random()
#     user_caipiao = buy_caipiao()
#     finall_count = check(random_list,user_caipiao)
#     print('摇奖机生成的中奖序列为：%s'%random_list)
#     print('用户购买的彩票为：%s'%user_caipiao)
#     print('当前用户彩票中奖数字个数为：%d,结果如下：'%finall_count)
#     if finall_count == 1:
#         print("猜中一个数字！奖励50!")
#     elif finall_count == 2:
#         print("猜中两个数字！奖励500!")
#     elif finall_count == 3:
#         print("猜中三个数字！奖励5000!")
#     elif finall_count == 4:
#         print("猜中四个数字！奖励50000!")
#     else:
#         print("真可惜，您一个都没猜中！再买一注吧？")
#         result()
# result()


# 内聚：从功能角度度量一个模块(也可以间接的引申为一个函数，一个类)内的联系。一个好的内聚应当是只在一个模块(函数，类)中干一件事。此概念
# 描述的是模块内的功能联系
# 耦合：耦合是软件结构中各个模块(函数，类)之间相互连接的一种度量，耦合强度取决于模块(函数，类)间接口的复杂程度。
# 高内聚，低耦合，是软件工程中的概念，是判断设计好坏的标准。也就是说，往后我们的模块化开发，都要遵循高内聚低耦合的标准，即，模块内功能的
# 内聚程度是否高，模块间耦合的联系程度是否低。大白话的意思其实就是，单一模块中，功能是否只有一个，且功能的实现过程中各部分之间的联系程度是否高，
# 模块之间，功能的依赖程度是否低，功能的分离程度是否高
# 高内聚低耦合，最大的一个目的，就是为了实现单一功能的高复用性


# 杨辉三角
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# .....
# 首先每一行首尾都有一个[1]
# 第一个也为[1]
# 设第一行的列表l = [1]
# 从第二行开始，规律大致为：
# [1] + [中间部分] + [1]
# 中间规律：
# 1
# 1 1
# 第二行：
# 1 2 1 即：
# [1] + l[0]+l[1] + [1]
# 第三行：
# 1 3 3 1 即：
# [1]+ l[0]+l[1] + l[1]+l[2] + [1]
# 以此类推，得到中间的规律为l[i]+l[i+1] for i in range(x)
# 至于i的规律，很简单，上一行列表元素个数-1
# 所以，生成器表达式的列表推导式已经出来了
# p = [1]+[p[i]+p[i+1] for i in range(len(l)-1)]+[1]
#
# def yanghui():
#     p = [1]
#     while True:
#         yield p
#         p = [1]+[p[i]+p[i+1] for i in range(len(p)-1)]+[1]
#
#
# n = 0
# for j in yanghui():
#     print(j)
#     n += 1
#     if n == 11:
#         break


