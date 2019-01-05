#函数重写
#定义：在自定义的类中，通过添加特定的方法，让自定义的类生成的对象能像内建对象一样进行内建函数操作
# 1.对象转字符串函数重写
# ex：
# class My_Function:
# 	def __init__(self,value):#此例子仅仅只是个例子，在这里传不传参数都无所谓的
# 		self.data = value

# 	def __repr__(self):
# 		print("__repr__方法被调用啦！")
# 		return "数字:%d"%self.data

# 	def __str__(self):
# 		print("__str__函数被调用啦!")
# 		return 'My_Function(%d)'%self.data

# fun = My_Function(100)
# print(repr(fun))
# print(str(fun))

# 2.内建函数重写：
# 	１．abs(obj)方法
	# abs():对一个值求绝对值
# class My_Function:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		return 'My_Function(%d)'%self.data

# 	def __abs__(self):
# 		if self.data < 0:
# 			return My_Function(-self.data)
# 		else:
# 			return My_Function(self.data)


	# 2.len函数,reverse函数重写

# class My_List:
# 	def __init__(self,it):
# 		self.L = [x for x in it]

# 	def __repr__(self):
# 		return "My_List(%r)"%self.L

# 	def __len__(self):
# 		return len(self.L)

# 	def append(self,n):
# 		self.L[len(self.L):] = [n]

# 	def __reversed__(self):
# 		return self.L[::-1]

# l = My_List(range(0,5))
# print("l是：",l)
# print(len(l))
# print(reversed(l))

# 3.数值转换函数int(),float()重写
# class My_Number:
# 	def __init__(self,value):
# 		self.data = int(value)

# 	def __repr__(self):
# 		return "My_Number(%d)"%self.data

# 	def __int__(self):
# 		return self.data

# 	def __float__(self):
# 		return float(self.data)

# num = My_Number(100)
# print("num　is :",num)
# print(int(num))
# print(float(num))


# 4.对象属性管理函数重写
# class GetAttr:
# 	def __init__(self,value1,value2):
# 		self.age = value1
# 		self.sex = value2

# 	def __repr__(self):
# 		return 'GetAttr(%d,%s)'%(self.age,self.sex)

# 	def __getattr__(self,name):
# 		if name == 'age':
# 			return self.age
# 		elif name == 'sex':
# 			return self.sex
# 		else:
# 			raise AttributeError

# 	def __hasattr__(self,name):
# 		if name == 'age' or name == 'sex':
# 			return True
# 		else:
# 			return False
		
# 	def __setattr__(self,name,value):
# 		if name == 'age':
# 			print("__setattr__()方法调用")
# 			self.__dict__[name] = value
# 			return self.age
# 		if name == 'sex':
# 			self.__dict__[name] = value
# 			return self.sex

		
# attr1 = GetAttr(28,"男")
# # print("attr1 is :",attr1)
# # print(getattr(attr1,'sex'))
# # print(hasattr(attr1,'sex1'))
# # print(setattr(attr1,'age',31))
# attr1.age = 40
# print(attr1.age)



# 5.运算符重载
# class My_Calculator:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		return 'My_Calculator(%d)'%self.data

# 	def myadd(self,other):
# 		return My_Calculator(self.data + other.data)

# 	#加法重载
# 	def __add__(self,other):
# 		return My_Calculator(self.data + other.data)

# 	#减法重载
# 	def __sub__(self,other):
# 		return My_Calculator(self.data - other.data)

# 	#乘法重载
# 	def __mul__(self,other):
# 		return My_Calculator(self.data * other.data)

# 	#除法重载
# 	def __truediv__(self,other):
# 		return My_Calculator(self.data / other.data)

# 	#地板除重载
# 	def __floordiv__(self,other):
# 		return My_Calculator(self.data // other.data)

# 	#求余重载
# 	def __mod__(self,other):
# 		return My_Calculator(self.data % other.data)

# 	#幂运算重载
# 	def __pow__(self,other):
# 		return My_Calculator(self.data ** other.data)	


# n1 = My_Calculator(100)
# n2 = My_Calculator(200)
# print("ni is :",n1)
# print(n1+n2)

# # 6.反向算数运算符重载

# class My_Calculator:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		return 'My_Calculator(%d)'%self.data

# 	#加法重载
# 	def __add__(self,other):
# 		if type(other) is int:
# 			return My_Calculator(self.data + other)
# 		elif type(other) is My_Calculator:
# 			return My_Calculator(self.data + other.data)

# 	#反向加法重载
# 	def __radd__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data + lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data + lhs.data)

# 	#反向减法重载
# 	def __rsub__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data - lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data - lhs.data)

# 	#反向乘法重载
# 	def __rmul__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data * lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data * lhs.data)

# 	#反向除法重载
# 	def __rtruediv__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data / lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data / lhs.data)

# 	#反向地板除重载
# 	def __rfloordiv__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data // lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data // lhs.data)

# 	#反向求余重载
# 	def __rmod__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data % lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data % lhs.data)

# 	#反向幂运算重载
# 	def __rpow__(self,lhs):
# 		if type(lhs) is int:
# 			return My_Calculator(self.data ** lhs)
# 		elif type(lhs) is My_Calculator:
# 			return My_Calculator(self.data ** lhs.data)

#７．复合赋值运算符重载
# class My_iCalculator:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'My_iCalculator(%d)'%self.data
# 	#加法运算符重载
# 	def __add__(self,rhs):
# 		print('__add__()方法被调用')
# 		return My_iCalculator(self.data + rhs.data)

# 	#复合加法运算符重载
# 	def __iadd__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data + rhs.data)

# 	#复合减法运算符重载
# 	def __isub__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data - rhs.data)

# 	#复合乘法运算符重载
# 	def __isub__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data * rhs.data)

# 	#复合除法运算符重载
# 	def __isub__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data / rhs.data)

# 	#复合地板除运算符重载
# 	def __isub__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data // rhs.data)

# 	#复合求余运算符重载
# 	def __isub__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data % rhs.data)

# 	#复合幂运算符重载
# 	def __isub__(self,rhs):
# 		print("__iadd__()方法被调用")
# 		return My_iCalculator(self.data ** rhs.data)

# n1 = My_iCalculator(2)
# n2 = My_iCalculator(4)
# n1+=n2
# print(n1)


#8.一元运算符重载

# 针对具体情况而言，比如对于整型，浮点型等数值型数据，取反即前面加上-号（布尔值除外，布尔值如果是True，取反后的值为False）

# 比如列表等数据类型，取反就是反转列表，负号就是对每一个元素取负值

# class My_Number:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'My_Number(%d)'%self.data

# 	#负号运算符重载
# 	def __neg__(self):
# 		print("__neg__()方法被调用")
# 		return -self.data

# 	#取反运算符重载
# 	def __invert__(self):
# 		print("__invert__()方法被调用")
# 		if type(self.data) is bool:
# 			if self.data == True:
# 				return False
# 			elif self.data == False:
# 				return True
# 		elif type(self.data) is int or type(self.data) is float:
# 			return -self.data

# num = My_Number(1)
# print(-num)

# 列表等数据类型的一元运算符重载

# class Mylist:
# 	def __init__(self,it):
# 		self.data = [x for x in it]

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'Mylist(%r)'%self.data

# 	def __neg__(self):
# 		print("__neg__()方法被调用")
# 		return Mylist((-x for x in self.data))

# 	def __invert__(self):
# 		print("__invert__()方法被调用")
# 		return Mylist(reversed(self.data))

# l1 = Mylist([1,2,3,4,5,6])
# print(l1)
# l2 = -l1
# print(l2)


# 索引和切片的运算符重载
# class Mylist:
# 	def __init__(self,it):
# 		self.data = [x for x in it]

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'Mylist(%r)'%self.data

# 	def __getitem__(self,i):
# 		print("__getitem__()方法被调用")
# 		return self.data[i]

# 	def __setitem__(self,i,value):
# 		print("__setitem__()方法被调用")
# 		self.data[i] = value

# l = Mylist(range(1,11))
# print(l)
# print(l[2])
# l[4] = '安伟超'
# print(l)


# in   not in 运算符重载
# 分类讨论

# 数字类型：
# class Mynumber:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'Mynumber(%d)'%self.data

# 	def __contains__(self,item):
# 		print("__contains__()方法被调用")
# 		if item < self.data and item > 0:
# 			return True
# 		else:
# 			return False

# num = Mynumber(10)
# # print(num)
# print(3 in num)

# 列表：
# class Mylist:
# 	def __init__(self,it):
# 		self.data = [x for x in it]

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'Mylist(%r)'%self.data

# 	def __contains__(self,item):
# 		print("__contains__()方法被调用")
# 		if item in self.data:
# 			return True
# 		else:
# 			return False

# l = Mylist(range(1,11))
# # print(l)
# print(4 in l)


# 迭代器协议实现

# class Mylist:
# 	def __init__(self,it):
# 		self.data = [x for x in it]

# 	def __repr__(self):
# 		return "Mylist(%r)"%self.data

# 	def __iter__(self):
# 		return MyListIterator(self.data)

# class MyListIterator:
# 	def __init__(self.lst_data):
# 		print("迭代器已经创建")
# 		self.data = lst_data
# 		self.cur_pos = 0

# 	def __next__(self):
# 		if self.cur_pos >= len(self.data):
# 			raise StopIteration

# 		index = self.cur_pos
# 		self.cur_pos+=1
# 		return self.data[index]












	

	







