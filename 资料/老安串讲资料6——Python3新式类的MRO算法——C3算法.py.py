# Python中的MRO和多继承
# 一.相关概念介绍
# 	1.MRO：Method Resolution Order,即方法解析顺序，是用来处理Python中的二义性问题的算法
# 	2.二义性：Python因为支持多继承，而多继承的编程语言往往存在二义性问题。二义性问题分为两种：
# 		1.有两个基类A和B，A和B中都定义了方法f(),C类继承了A类和B类，那么调用C类的f()时出现不确定情况。(魔鬼三角继承)
# 		2. 有一个基类A，定义了方法f()，B类和C类继承了A类（的f()方法），D类继承了B和C类，那么出现一个问题，D不知道应该继承B的f()方法还是C的f()方法。(恐怖菱形继承)
# 	3.深度遍历优先算法：指代一种搜索算法，其算法核心是尽可能先对纵深方向进行搜索，当一条分支搜索到叶子结点后，终止，从左往右找到下一条分支，继续开始纵深方向的搜索，直至搜索到最后一条分支的叶子节点，停止搜索。
# 	4.广度遍历优先算法：指代一种搜索算法，其算法核心是针对树形结构的每一层，从根结点出发，按照一层一层的顺序，每层从左至右的顺序搜索，当搜索到某一层最后一个非叶子结点，结束该层搜索，进入下一层，继续搜索，直至搜索到最后一个叶子节点，停止搜索。
# 	5.拓扑排序
# 		1.有向无环图：如果一个有向图无法从某个顶点出发经过若干条边回到该点，则这个图是一个有向无环图（DAG图）
# 		2.拓扑序列：对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，使得图中任意一对顶点u和v，若边(u,v)∈E(G)，且u在线性序列中出现在v之前。通常，这样的线性序列称为满足拓扑排序(TopologicalOrder)的序列，简称拓扑序列。
# 		3.拓扑排序算法： 循环执行以下两步，直到不存在入度为0的顶点为止
# 			1.选择一个入度为0的顶点并输出之；
#     		2.从网中删除此顶点及所有出边。
# 	6.Python版本介绍
# 		如果按照Python面向对象中多继承的MRO算法演变史为依据，可大致将Python的版本演变划分为四个阶段：
# 		1.Python2.2之前
# 		2.Python2.2
# 		3.Python2.2-Python2.7
# 	7.经典类：一种没有继承的类，所有的类型都是type类型，如果经典类作为父类，子类调用父类构造函数会报错。
# 	8.新式类：每一个类都继承自一个基类，默认继承自object，子类可以调用基类的构造函数，所有类都有一个公共的祖先类object。
# 	9.线性化过程中的单调性原则：遍历时应该先从唯一基类开始查找，即：子类不能改变基类的方法搜索顺序。
# 二.C3算法演变史
# 	1.Python中调用父类的两种方式
# 	示例代码——单继承：
# class A(object):
#    	def __init__(self):
#    		self.name = 'A:name'
#    		print('A:__init__')
#    	def fun(self):
#    		print("A:fun")
# class B(A):
# 	def __init__(self):
# 		print("B:__init__")
# 		A.__init__(self)                         # 使用类名直接调用
# 		super(B, self).__init__()                # 使用super关键字调用
# 	def fun(self):
# 		print("B:fun")
# 		A.fun(self)
# 		super(B, self).fun()
# 		print(self.name)
# b = B()
# 	总结：两种调用父类方法的方式其实都可行，区别在于，直接使用父类名称进行调用，父类方法只会被调用一次，使用super函数调用就是当前子类的基类的方法，可能调用不止一次。
# 	示例代码——多继承：
# class A(object):
# 	def __init__(self):
# 		print('进入a')
# 		print('离开a')
#
# class B(object):
# 	def __init__(self):
# 		print('进入b')
# 		print('离开b')
# class C(A):
# 	def __init__(self):
# 		print('进入c')
# 		super(C,self).__init__()
# 		print('离开c')
# class D(A):
# 	def __init__(self):
# 		print('进入d')
# 		super(D,self).__init__()
# 		print('离开d')
# class E(B,C):
# 	def __init__(self):
# 		print('进入e')
# 		B.__init__(self)
# 		C.__init__(self)
# 		print('离开e')
#
# class F(E,D):
# 	def __init__(self):
# 		print('进入f')
# 		E.__init__(self)
# 		D.__init__(self)
# 		print('离开f')
#
# f = F()
# print(F.__mro__)
#
#
# 	继承关系如图所示：
# 					object
# 					|	|
# 				   |	 |
# 				  |		  |
# 				 |		   |
# 			    |			A
# 			   |		   | |
# 			  |			  |   |
# 			 |			 |     |
# 			B           C        D
# 			 |         |		 |
# 			  |       |			 |
# 			   |     |			 |
# 			    |   |			 |
# 			     | |			 |
# 			      E 			 |
# 			       |			 |
# 			        |	   		 |
# 			         |			 |
# 			          |			 |
# 			           |		 |
# 			           	|		 |
# 			           	 |		 |
# 			           	  |		 |
# 			           	   |	 |
# 			           	    |	 |
# 			           		 |	 |
# 			           		  |	 |
# 			           		   | |
# 			           			F
# 	我们的本意是希望调用构造函数的时候，对于基类的构造方法也进行调用。但是实际结果：
#  		1.A和D的构造函数被调用了2次
#  		2.当调用super(C, self).__init__()的时候，竟然进入D的构造函数
#  		也就是说，D的构造函数被调用了两次，一次是F调用的，一次是C调用的，可是从继承关系上看，C的基类应该是A才对。
#  		什么鬼...不明白...懵逼了...
#  		Ok，一起来了解python中的C3算法.
#  	2.Python2.2之前的经典类
#  		在python 2.2之前，python中使用经典类（classicclass），经典类是一种没有继承的类，所有类型都是type类型，如果经典类作为父类，
#  		子类调用父类构造函数会报错。当时用作MRO的算法是DFS（深度优先），下面的例子是当时使用DFS算法的示例（向右是基类方向）：
#  		1.正常的继承方式:
#  			A-->B-->D
#  			A-->C-->E
#  		DFS的遍历顺序为：A-->B-->D-->C-->E
#  		这种情况下，不会产生问题
#  		2.'恐怖'菱形继承方式
#  			A-->B-->D
#  			A-->C-->D
#  		DFS遍历顺序为：A-->B-->D-->C
#  		此时，如果公共父类D中也定义了f()，C中重写了方法f()，那么C中的f()方法永远也访问不到，因为按照遍历的顺序始终先发现D中的f()方法，
#  		导致子类无法重写基类方法。
#  	3.Python2.2版本中出现的新式类
#  		在python2.2开始，为了使类的内置类型更加统一，引入了新式类（new-style class），新式类每个类都继承自一个基类，默认继承自object，
#  		子类可以调用基类的构造函数。由于所有类都有一个公共的祖先类object，所以新式类不能使用DFS作为MRO。在当时有两种MRO并存：
#  			1.如果是经典类，MRO使用DFS
# 			2.如果是新式类，MRO使用BFS
# 		针对新式类的BFS示例如下（向右是基类方向）：
# 		1.正常的继承方式:
#  			A-->B-->D
#  			A-->C-->E
#  		BFS的遍历顺序为：A-->B-->C-->D-->E
#  		D是B的唯一基类，但是遍历时因为是广度遍历优先，先遍历节点C，这种情况下应该先从唯一基类进行查找，这个原则称为单调性。而在这里，明显，
#  		违背了单调性原则
#  		2.'恐怖'菱形继承方式
#  			A-->B-->D
#  			A-->C-->D
#  		BFS遍历顺序为：A-->B-->C-->D
#  		BFS解决了前面提到的子类无法重写基类方法的问题
#  	4.python2.3-python2.7，经典类和新式类并存，C3算法产生
#  		由于DFS和BFS针对经典类和新式类都有缺陷，从python2.3开始，引入了C3算法。针对前面两个例子，C3算法的遍历顺序如下：
#  		1.正常的继承方式:
#  			A-->B-->D
#  			A-->C-->E
#  		C3的遍历顺序为：A-->B-->D-->C-->E
#  		2.'恐怖'菱形继承方式
#  			A-->B-->D
#  			A-->C-->D
#  		C3遍历顺序为：A-->B-->C-->D
#  		看起来是DFS和BFS的综合，但是并非如此，下面的例子说明了C3算法的具体实现：
#  							object
#  						   |   |   |
#  						 |     |     |
#  					   |	   |       |
#  					 |         |         |
#  				   |           |           |
#  				   E           D            F
#                    |         |   |          |
#                    |       |       |        |
#                    |     |           |      |
#                    |   |               |    |
#                    | |                   |  |
#                    |                        |
#                    B                        C
#                    |                        |
#                      |                      |
#                        |                  |
#                          |             |
#                            |        |
#                              |   |
#                                A
#
#  			首先找入度为0的点，只有A，把A取出，把A相关的边去掉，再找下一个入度为0的点，B和C满足条件，从左侧开始取，取出B，这时顺序是AB，
#  		然后去掉B相关的边，这时候入度为0的点有E和C，依然取左边的E，这时候顺序为ABE，接着去掉E相关的边，这时只有一个点入度为0，那就是C，取C，
#  		顺序为ABEC。去掉C的边得到两个入度为0的点D和F，取出D，顺序为ABECD，然后去掉D相关的边，那么下一个入度为0的就是F，然后是object。
#  		所以最后的排序就为ABECDFobject。
#
#
# Python中的元类
# 	1.类和对象
# 		1.什么是类：类是面向对象的编程语言实现信息封装的基础概念，类是一种用户定义的类型，通俗点，一种封装若干属性和方法的结构就叫做类，类的实例化，就是对象，所以也可以说，类就是用来创建对象的代码片段。
# 		2.什么是对象：对象是现实中的物体或实例。对象是由类实例化而来的，对象是由类创建的，一切万物皆对象。这句话对吗？讲完这个知识点，我们再回来求证这句话到底是不是彻底的对。
# 		3.类的特殊特性：类，本身，也是一个对象！
# 		4.怎么理解：其实，在你定义一个类的时候，就会在内存中创建一个名为类名的对象
# 		5.对象的特征：
# 			1.将他存储在一个变量里
# 			2.复制它
# 			3.给他添加属性
# 			4.当做参数传递给函数
#
# 	经过如上概念，对类，应该有了最最基本的理解。但是，问题继续来了：对象不可能凭空产生，它一定是由某些'事物'生成的。既然类也是一个对象，那不意外，类，同样遵循这个规律
# 	当你在使用class关键字的时候，Python就会自动创建这个'对象'。但是，虽为自动创建，但是，同样可以手动实现
# 	2.type函数：很常用，对吧？返回一个对象的类型。ok，我们现在就玩玩这个type
# 	我们在命令行下随便调试，如下：
# 		anwc@anweichao-pc:~$ ipython3
# 		Python 3.6.5 (default, Apr  1 2018, 05:46:30)
# 		Type 'copyright', 'credits' or 'license' for more information
# 		IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
#
# 		In [1]: type(1)
# 		Out[1]: int
#
# 		In [2]: type(int)
# 		Out[2]: type
#
# 		In [3]: type('1')
# 		Out[3]: str
#
# 		In [4]: type(str)
# 		Out[4]: type
#
# 		In [5]: type(1.11)
# 		Out[5]: float
#
# 		In [6]: type(float)
# 		Out[6]: type
#
# 		In [7]: type(True)
# 		Out[7]: bool
#
# 		In [8]: type(bool)
# 		Out[8]: type
#
# 		In [9]: type([1,2,3])
# 		Out[9]: list
#
# 		In [10]: type(list)
# 		Out[10]: type
#
# 		In [11]: type((1,2,3))
# 		Out[11]: tuple
#
# 		In [12]: type(tuple)
# 		Out[12]: type
#
# 		In [13]: type({'1':2})
# 		Out[13]: dict
#
# 		In [14]: type(dict)
# 		Out[14]: type
#
# 	以上是type最常用的方式，没错，只传递一个参数，作用很简单，返回对象的类型。而此时无论你是type(int)，还是type(dict),亦或是type(tuple)，返回的统统都是type！_ok，聪明的同学已经恍然大悟，这个被返回的type，就是Python中的元类！
# 		1.type函数传递一个参数的用法：当只传递一个参数的时候，其功能单一，仅仅知识返回对象的类型
# 		2.type函数传递三个参数的时候：type是类最根本的元类，此时，用来创建类！
# 			此时type函数语法：
# 			类名 = type(String,tuple,dict)
# 			参数解释：
# 				String：字符型参数，类的名称
# 				tuple:元组，继承关系
# 				dict：字典，定义属性及方法
# 		继续，我们在命令行中看看我们如何手动创建类：
# 		anwc@anweichao-pc:~$ ipython3
# 		Python 3.6.5 (default, Apr  1 2018, 05:46:30)
# 		Type 'copyright', 'credits' or 'license' for more information
# 		IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
#
# 		In [1]: Myancestor = type('Myancestor',(),{})
#
# 		In [2]: Myancestor
# 		Out[2]: __main__.Myancestor
#
# 		In [3]: print(Myancestor)
# 		<class '__main__.Myancestor'>
#
# 		此时你手动创建了一个类Myancestor，我们来看看它的元类是谁：
#
# 		In [4]: type(Myancestor)
# 		Out[4]: type
#
# 		看到了吗？type函数手动创建的类，其元类仍是type！
# 		继续玩，我们手动创建类的时候还能给其设定继承关系和成员属性及方法：
# 		In [5]: MyOld = type('MyOld',(Myancestor,),{'name':'子代'})
#
# 		In [6]: MyOld.__mro__
# 		Out[6]: (__main__.MyOld, __main__.Myancestor, object)
#
# 		添加方法？很简单，先定义好一个函数然后传进字典中即可：
# 		In [7]: def Myfun():
# 		   ...:     pass
# 		   ...:
# 		   ...:
#
# 		In [8]:
#
# 		In [8]: MyBaba = type('MyBaba',(MyOld,),{'name':'子代1','Myfun':Myfun})
#
# 	3.元类：
# 		其实很好理解，创建类的类...有点拗口...Python中，类也是对象，这样的对象就是通过类来创建的。元类就是'类的类'
# 	刚才我们玩坏了的type，就是一个元类，Python中所有的类都是由type创建的！
# 		继续追问：type既然是元类，那type是对象吗？type的类型是什么？ok，'Python中一切万物皆对象'这句话，因为type元类，
# 	止步于此。这句话，我们重新概括：Python中，除了type,一切万物皆对象！
# 	4.结语：元类，是一种99%的人都不需要关心的深度魔法。当你好奇你是否需要懂它，了解它时，恰恰说明你并不需要它，
# 	而明确需要它的人不需要找任何原因解释为什么需要。元类，是你注定得不到搞不明白的东西！
#
