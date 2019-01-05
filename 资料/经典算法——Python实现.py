# 1.二分法查找：对于区间[a，b]上连续不断且f（a）·f（b）<0的函数y=f（x），通过不断地把函数f（x）的零点所在的区间一分为二，使区间的两个端点逐步逼近零点，进而得到零点近似值的方法叫二分法。
# 代码实现：
l = []
item = int(input('请输入您想查找的元素：'))
while True:
    num = int(input('请输入数字：'))
    l.append(num)
    if len(l) == 5:
        break
print('输入的列表为：%s'%l)

for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print('排序后的列表为：%s'%l)

low = 0
high = len(l)-1
res = 0

# print(l)
while low < high:
    middle = (low + high) // 2
    guess = l[middle]
    if guess > item:
        high = middle - 1
    elif guess < item:
        low = middle + 1
    else:
        res = middle
        break
print('您查找的元素：%d,其位置为第%d位'%(item,res))


