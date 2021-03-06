# 1.	直接插入排序
# 思想：将一个记录插入到已排序好的有序表中，从而得到一个“新的”，记录数增1的有序表。
# 思路：先将第一个元素看作一个有序的子序列（说白了就是先把第一个元素假设单独放在一个序列里面，那么这个序列目前只有一个元素，当然就是已经有序了），然后从第二个元素开始依次进行插入，直至整个序列有序为止。
# 算法具体实现步骤：
# 1.	先获得一个随机序列
# 2.	拿出序列第一个元素后，从第二个开始用for循环遍历序列
# 3.	定义一个循环变量j，该变量用来控制插入的位置，因为是后一个和前一个比较，所以让j = i-1
# 4.	定义一个哨兵，专门用来临时存放元素
# 5.	循环的让后一个元素和前一个元素比较，如果后一个元素比前一个元素小，就将其插入前一个元素之前。此时可能存在：已插入的元素仍然比前面某个元素小，所以，j -= 1，在比较一次，直至前面没有比自己大的元素，结束一次遍历
# 6.	最终输出排序完成的列表即可。
#
#初始化序列
l = [45,34,78,78,98,23,12]
# 拿出序列第一个元素后，从第二个开始用for循环遍历序列
for i in range(1,len(l)):
    # 后面的和前面的比较
    j = i - 1
    # 哨兵，临时存放元素
    key = l[i]
    # 每一次遍历决定插入的最终位置
    while j >= 0:
        # 如果后面的值小于前面的值
        if key < l[j]:
            # 后面的值赋值给前面的值，相当于交换位置
            l[j+1] = l[j]
            # 前面的值拿出来存在哨兵中
            l[j] = key
        # 继续向前比较
        j -= 1
print(l)





# 3.选择排序之简单选择排序
# 思想：在需要排序的序列中选择最小的一个数与第一个数交换位置，
# 在剩余的n-1个数中在选择一个最小的数与剩余n-1个数的序列中第一个元素交换位置，
# 直至剩余元素个数为1，排序结束
# 算法实现步骤：
# 1.遍历序列
# 2.将每一次遍历取到的数和剩余n-1个数的序列中的第一个元素进行交换位置
l = [3,1,5,7,2,4,9,6]
for i in range(0, len(l)):
    # 默认设置最小值的下标为当前值
    min = i
    # 在剩余n-1个元素的序列中找到最小元素的下标
    for j in range(i + 1, len(l)):
        # if l[i] > l[i+1]
        # 如果找到，就把最小元素的下标赋值给min
        if l[min] > l[j]:
            min = j
    # 将找到的最小值的元素和当前元素做位置交换
    temp = l[min]
    l[min] = l[i]
    l[i] = temp
print(l)


# 4.选择排序之堆排序
#     1.算法介绍
#         堆排序是一种树形选择排序，是对直接选择排序的有效改进
#     2.首先先介绍几个知识点概念：
#         1.二叉树：在计算机科学中，每个结点最多有两个子结点的树就叫做二叉树
#             比如：有一个一维数组(python中用列表代替)[3,6,7,2,3,5,6,7,8,9,5,4,3,6,7]
#             将其用以下树形结构展示：
#                             3
#                     6               7
#                 2       3       5       6
#              7     8 9    5  4     3 6     7
#             此树即为二叉树
#             二叉树的子数有左右之分，顺序绝不能颠倒
#
#         3.深度遍历优先算法：指代一种搜索算法，其算法核心是尽可能先对纵深方向进行搜索，
#         当一条分支搜索到叶子结点后，终止，从左往右找到下一条分支，继续开始纵深方向的搜索
#         4.广度遍历优先算法：指代一种搜素算法，其算法核心是针对树形结构的每一层，从根结点出发，按照一层一层的顺序，
#         每层从左至右的顺序搜索，当搜索到某一层最后一个非叶子结点，结束该层搜索，进入下一层，继续搜索，
#         直至搜索到最后一个叶子节点，停止搜索。
#         5.完全二叉树：设二叉树的深度为h，除了h层外，其他各层(h-1)层结点数都达到了最大个数，第h层所有的结点都连续集中在最左边，就是一颗完全二叉树
#         6.叶子结点：没有子女的结点就叫叶子结点
#         7.堆：计算机科学中一类特殊的数据结构的总称。定义如下：n个元素的序列[k1,k2,k3,...ki,...,kn](i = 1,2,3,4,...,n/2),当且仅当满足以下条件：
#         (ki <= k2i,ki <= k2i+1)或>=时，就称之为堆。
#         如果用一个列表存储一个堆，则该堆一定对应一个完全二叉树。那么该完全二叉树的根结点就叫做堆的堆顶元素。
#         当上述条件均为小于时，就会产生小顶堆，反之产生大顶堆。所以由堆的定义可以看出，第一个元素，即堆顶元素必为最小项或最大项，
#         同时，所有非叶子结点的值均不大于或不小于其子女的值
#         比如：
#             大顶堆：[87,84,85,36,11,32]
#                           87
#                     84          45
#                 36      11  32
#             小顶堆：[12,23,26,32,24,30,28,43,35]
#                               12
#                         23          26
#                     32      24  30      28
#                 43      35
#     3.算法实现步骤：
#         初始时把要排序的n个数的序列看作是一棵顺序存储的二叉树（一维数组存储二叉树），调整它们的存储序，
#         使之成为一个堆，将堆顶元素输出，得到n 个元素中最小(或最大)的元素，这时堆的根节点的数最小（或者最大）。
#         然后对前面(n-1)个元素重新调整使之成为堆，输出堆顶元素，得到n 个元素中次小(或次大)的元素。
#         依此类推，直到只有两个节点的堆，并对它们作交换，最后得到有n个节点的有序序列。称这个过程为堆排序。
#         因此，实现堆排序需解决两个问题：
#             1. 如何将n 个待排序的数建成堆；
#             2. 输出堆顶元素后，怎样调整剩余n-1 个元素，使其成为一个新堆。



import random
import math

#随机生成0~100之间的数值，此随机生成的序列无序
def get_randomNumber():
    list=[]
    i=0
    num = int(input("请输入元素个数："))
    while i<num:
        list.append(math.floor(random.random()*100+1))
        i += 1
    return list

# 将一个无序序列形成完全二叉树，此完全二叉树同样无序
def PrintList_Dui(l):
    # 提供一个初始化好的列表
    # 第一行时只有一个数
    # 每行的数字数量
    number_count=1#2  4
    # 行数
    row_number=1   #2  3
    # 遍历这个列表
    # 形成的堆结构
    print("形成的完全二叉树结构：")
    for i in range(len(l)):
        # 因为要形成一个完全二叉树，每一层(行)的元素数量为2 ** (行数-1)个
        # 使用一个巧妙的算法来实现打印出一个完全二叉树
        # 此段算法分析：
        # i = 0时，循环刚开始，因为0和number_count不等，if跳过，直接先打印arr[0]的值，10
        # i = 1时，1和1相等，执行if,number_count(每行元素个数)变为3，然后换行，行数加1，再输出arr[1] 9
        # i = 2时，2 和 3 不等，直接打印arr[2] 8
        # i = 3时，3和3相等，if执行，number_count变为7，换行，行数变为3，输出arr[3] = 7
        # ...
        # 直至程序结束
        #-----------------------------#
        if i==number_count:
            number_count += 2 ** row_number# i = 1时，a = 3
            print("\n")
            row_number += 1# i = 1时 row = 2
        #-----------------------------#
        print (l[i],end="  ")# i = 0,if跳过，直接运行这行，10被打印  i = 1时，if执行，换到第二行，打印9
        #-----------------------------#
    print("Over")
    return l

# 至此，基本功能实现，接下来就是详细实现步骤(大顶堆，形成升序序列)
# 第一步：创建堆。
# 将一个无序列表写为顺序二叉树，从最后一个非叶子节点开始，按照从下至上，从左至右的顺序遍历，依次寻找每一个非叶子节点的左右子节点，然后将其与父节点大小进行比较
# ，如果子节点比父节点大，就将父子节点交换值

# 第一步：创建堆
def build_heap(l, size):
    # 从最后一个非叶子结点开始遍历，从下至上，从左至右遍历
    for i in range(0, (size // 2))[::-1]:
        adjust_heap(l, i, size)
        # 此时需要进行调整堆，所以调用调整堆的函数，创建堆其实只是先需要创建一个初始化的堆结构，但因为形成堆结构就需要进行依次
        # 调整堆，所以在这里需要调用调整堆函数

# 第二步：调整堆
def adjust_heap(l, i, size):
    # 父节点i的左子节点
    lchild = 2 * i + 1
    # 父节点i的右子节点
    rchild = 2 * i + 2
    # 堆顶(最大值)的下标
    max = i
    if i < size // 2:
        # 如果没有超出数组的深度，且非叶子节点左子节点的值大于父节点的值
        if lchild < size and l[lchild] > l[max]:
            # 将该非叶子节点的左子节点的值存在在max变量
            max = lchild
        # 如果没有超出数组的深度，且非叶子节点右子节点的值大于父节点的值
        if rchild < size and l[rchild] > l[max]:
            # 将该非叶子节点的右子节点的值存放在max变量
            max = rchild
        # 挑出来的非叶子节点的值的下标此时已经存在max(堆顶，也是最大值)中，将max(带着的就是挑出来的左或者右子节点的下标)跟父节点进行交换
        if max != i:
            l[max], l[i] = l[i], l[max]
            # 到此，准备遍历第二遍，第二遍仍然是在重复调整堆，所以调整函数需要再执行一遍，形成递归。
            adjust_heap(l, max, size)

# 第三步：堆排序
def heap_sort(l):
    # 获取列表长度
    size = len(l)
    # 堆排序之前，先创建堆
    build_heap(l, size)
    # 从后向前遍历，将每一次调整堆之后获得的堆顶和最后一个元素交换位置，先得到第一大最大值
    for i in range(0, size)[::-1]:
        # 循环内，继续进行调整堆，不断得到第二大最大值，第三大最大值，...第n大最大值
        # 这里是交换位置
        l[0], l[i] = l[i], l[0]
        # 重复进行调整堆，直至剩下最后两个元素交换位置，排序完成
        adjust_heap(l, 0, i)
        # 整个完整的调整堆的过程就是一个堆排序过程
        # 所以，其实可以发现，创建堆的过程其实只需要一遍调整堆就ok，但因为第二步是重复调整堆，
        # 所以很自然的直接过度到调整堆函数，
        # 而重复调整堆之后每一次调整堆都会交换堆顶和最后一个元素的位置
        # 不断的形成升序方向的最大值，所以完整的重复调整堆的过程就是堆排序
    return l


l = get_randomNumber()
print("排序之前(随机生成的列表)：%s" %l)
b = PrintList_Dui(l)
print("排序之前，形成完全二叉树结构之后的无序列表:%s"
      "(其实跟原列表一样一样的，只不过是对照着这个无序列表形成完全二叉树结构)"%b)
finall_list = heap_sort(l)
print('排序之后的列表为：%s'%finall_list)




# 5.交换排序之冒泡排序
# 算法归类：交换排序
# 算法思想：使用交换思想，即：前一个元素和后一个元素进行大小比较，如果前面比后面大，就交换位置，然后继续向后比较，直至一次冒泡结束，将最大值(或最小值)
# 放到最后一个位置。通过多次的冒泡，最终实现排序
# 举例：
# [9,7,5,3]                   [9,8,6,4,3]             ......
# ---------                   ------------
# [7,9,5,3]                   [8,9,6,4,3]
# [7,5,9,3]                   [8,6,9,4,3]
# [7,5,3,9]                   [8,6,4,9,3]             ......
# ---------                   [8,6,4,3,9]
# [5,7,3,9]                   ------------
# [5,3,7,9]                   [6,8,4,3,9]
# ---------                   [6,4,8,3,9]
# [3,5,7,9]                   [6,4,3,8,9]             ......
#                             ------------
#                             [4,6,3,8,9]
#                             [4,3,6,8,9]
#                             ------------
#                             [3,4,6,8,9]
#
# 通过以上的模拟冒泡排序的算法举例，可以总结出如下规律：
# n个元素的序列，总共需要冒泡n-1次
# 设冒泡次数为i，那么每一次冒泡需要比较的次数就为n-i次
# 至此，算法结束

# 算法实现：
import random
import math
l = []
counts = int(input("请输入您想生成的序列的元素个数："))
while True:
    num = math.floor(random.random()*100+1)
    l.append(num)
    if len(l) == counts:
        break
print('排序前，生成好的随机列表为:%s'%l)
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print("排序后的列表为：%s"%l)









