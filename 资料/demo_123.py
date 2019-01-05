# 输入三个值，输出三个值中的最大值
a = int(input('请输入一个数字：'))
b = int(input('请输入一个数字：'))
c = int(input('请输入一个数字：'))
print('最大值是:',(a if a > c else c)if a > b else (b if b > c else c))