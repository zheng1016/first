#     3.建造者模式
#         1.定义：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
#         2.适用情况：
#             1.当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时。
#             2.当构造过程必须允许被构造的对象有不同的表示时。
#         举例：建筑工程师(指挥者)指挥工人(建造者)建造

# class Builder(object):
#     '''定义建造者抽象类，定义抽象方法用于子类继承'''
#     def create_footer(self):
#         pass

#     def create_body(self):
#         pass

#     def create_header(self):
#         pass

# class Thin(Builder):
#     '''定义瘦子类，继承抽象方法并重写'''
#     def create_footer(self):
#         print('瘦子的脚创建了')

#     def create_body(self):
#         print('瘦子的身体创建了')

#     def create_header(self):
#         print('瘦子的头创建了')

# class Fat(Builder):
#     '''定义胖子类，继承抽象方法并重写'''
#     def create_footer(self):
#         print('胖子的脚创建了')

#     def create_body(self):
#         print('胖子的身体创建了')

#     def create_header(self):
#         print('胖子的头创建了')

# class Director(object):
#     '''定义指挥者类，根据传入参数决定调用哪个子类的方法'''
#     def __init__(self,person):
#         self.person = person
#     def create_person(self):
#         self.person.create_footer()
#         self.person.create_body()
#         self.person.create_header()

# if __name__ == '__main__':
#     thin = Thin()
#     fat = Fat()
#     direct_thin = Director(thin)
#     direct_fat = Director(fat)
#     direct_thin.create_person()
#     direct_fat.create_person()

#     4.原型模式
#         1.定义：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
#         2.适用情况：
#             1.当要实例化的类是在运行时刻指定时，例如，通过动态装载；或者为了避免创建一个与产品类层次平行的工厂类层次时；
#             或者当一个类的实例只能有几个不同状态组合中的一种时。
#             2.需要大量的基于某个基础原型进行微量修改而得到新原型时使用
#         举例：投递简历，需要引用你的过往工作经历。

# from copy import copy,deepcopy
# class Prototype(object):
#     '''创建原型抽象类，用于子类继承'''
#     def clone(self):
#         pass

#     def deep_clone(self):
#         pass

# class WorkExp(object):
#     '''创建工作经验类，定义添加工作经验方法'''
#     def __init__(self):
#         self.timearea = ''
#         self.company = ''

#     def set_workexp(self,timearea,company):
#         self.timearea = timearea
#         self.company = company

# class Resume(Prototype):
#     '''创建简历类，继承原型抽象类，重写抽象方法的同时添加部分属性'''
#     def __init__(self,name):
#         self.name = name
#         self.workexp = WorkExp()

#     def set_personinfo(self,sex,age):
#         self.sex = sex
#         self.age = age

#     def set_workexp(self,timearea,company):
#         self.workexp.set_workexp(timearea,company)

#     def display(self):
#         print(self.name)
#         print(self.sex,self.age)
#         print('工作经历：%s,%s'%(self.workexp.timearea,self.workexp.company))

#     def clone(self):
#         return copy(self)

#     def deep_clone(self):
#         return deepcopy(self)

# if __name__ == '__main__':
#     obj1 = Resume('安伟超')
#     obj2 = obj1.clone()
#     obj3 = obj1.deep_clone()

#     obj1.set_personinfo('男',30)
#     obj1.set_workexp('2016-2018','达内时代科技集团天津天大中心')

#     obj2.set_personinfo('男',32)
#     obj2.set_workexp('2018-2020','达内时代科技集团天津学府中心')

#     obj3.set_personinfo('男',34)
#     obj3.set_workexp('2020-2022','达内时代科技集团天津长虹中心')

#     obj1.display()
#     obj2.display()
#     obj3.display()

#     简历类Resume继承抽象原型的clone和deepclone方法，实现对简历类的复制，并且简历类引用工作经历类，
#     可以在复制简历类的同时修改局部属性

#     5.单例模式
#         1.定义：单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
#             举例：比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
#             我们先看看单例模式问题从何而来：
# class A(object):
#     def __init__(self):
#         pass
#     def foo(self):
#         pass

# a = A()
# print(id(a))
# b = A()
# print(id(b))
#             运行结果如下：
#             anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#             140534096496512
#             140534096497128
#             很明显，通过打印实例的id可以发现，A类默认被创建了两个实例a和b
#             那么，如何让类只去实例化一个对象，而后再创建的实例是返回上一次的对象的引用呢？
#         2.单例模式实现方式——使用模块
#             其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：   
# 创建一个单例模块mysingleton.py

# mysingleton.py
# class Singleton(object):
#     def __init__(self):
#         self.name = '小安安'
#     def foo(self):
#         print('我是：%s'%self.name)
# singleton = Singleton()


# from mysingleton import singleton
# singleton.foo()

#         3.单例模式实现方式——使用装饰器

# def singleton(cls,*args,**kwargs):
#     '''
#     使用装饰器的原理：
#     1.先创建外层函数，需要传入一个参数，此参数为类(对象)
#     2.创建一个空字典，用来保存单例
#     3.创建一个内层函数，用来获得单例
#     4.内层函数中进行判断：如果当前字典不存在单例，就创建单例，如果存在，直接返回该单例的引用
#     5.外层函数返回内层函数

#     '''
#     instances = {}
#     print('装饰器函数被调用！')
#     def get_singleton(*args,**kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         print('装饰器内层函数也被调用！')
#         print(instances)
#         return instances[cls]
#     return get_singleton

# @singleton
# #此处，相当于：Student = singleton(Student)
# class Student(object):
#     '''
#     创建单例的原理：
#     1.先由类实例化对象：xiaoanan = Student(30,'小安安')并传参，此时，因为前面已添加装饰器@singleton，Student此时相当于绑定到了get_singleton函数，这句实例化对象的语句其实就是如下格式：xiaoanan = get_singleton(30,'小安安'),而实例化对象时，这句话相当于调用了装饰器的内部函数get_singleton，因为是第一次创建对象xiaoanan ,当前字典中并没有单例xiaoanan,所以内层函数get_singleton中会执行if语句真值表达式为True时的语句，即：instances[cls] = cls(*args,**kwargs)，而这里的cls接收到的参数是Student，所以此句代码相当于：instances[Student] = Student(30,'小安安'),即给字典键名为Student的键添加一个值，这个值是Student类实例化的对象
#     2.当又一次实例化对象xiaochaochao时，因为仍然还是通过Student类实例化该对象，而之前的单例已经存在于字典中了，所以不会再创建第二个单例，只会直接返回已有的单例并绑定当前的引用，进而真正实现了单例模式！
    
#     '''
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name
#         print('__init__()方法被调用了')
# xiaoan = Student(30,'小安安')
# xiaochaochao = Student(18,'小超超')
# print(id(xiaoan))
# print(id(xiaochaochao))

#             最终执行结果：
#             anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#             装饰器函数被调用！
#             __init__()方法被调用了
#             装饰器内层函数也被调用！
#             {<class '__main__.Student'>: <__main__.Student object at 0x7fe08913f748>}
#             装饰器内层函数也被调用！
#             {<class '__main__.Student'>: <__main__.Student object at 0x7fe08913f748>}
#             140602349188936
#             140602349188936

#             此方式即实现了单例模式。



#         4.单例模式实现方式——使用类
# import threading
# import time

# class Singleton(object):
#     def __init__(self):
#         # time.sleep(1)
#         pass

#     @classmethod
#     def instance(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             Singleton._instance = Singleton(*args,**kwargs)
#         return Singleton._instance
# def test(args):
#     a = Singleton.instance()
#     print(id(a))
# # b = Singleton.instance()


# for i in range(10):
#     t = threading.Thread(target=test,args=[i,])
#     t.start()

#             程序暂时先写成这样，我们先运行一下，看看结果：
#             anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             140291643101480
#             看上去，没毛病，恩，实现了单例，但其实！有毛病！此时看上去没问题是因为执行速度过快，如果我们让__init__方法存在一些IO操作，就会发现问题。
#             下面，我们用睡眠代替可能的IO操作看看会出现什么效果

# import threading
# import time

# class Singleton(object):
#     def __init__(self):
#         time.sleep(1)

#     @classmethod
#     def instance(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             Singleton._instance = Singleton(*args,**kwargs)
#         return Singleton._instance
# def test(args):
#     a = Singleton.instance()
#     print(id(a))
# # b = Singleton.instance()


# for i in range(10):
#     t = threading.Thread(target=test,args=[i,])
#     t.start()

#             此时，我们再看看程序运行的结果：
#             anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#             140107826004320
#             140107826107280
#             140107825398672
#             140107825883008
#             140107825392944
#             140107825882896
#             140107825398952
#             140107826107504
#             140107825835816
#             140107825881496

#             问题出现了！按照以上方式创建的单例，不支持多线程！
#             ok，如果非得采用这种方式来创建单例，解决办法是：加锁！
#             未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全
#             再看如下代码：

# import threading
# import time

# class Singleton(object):
#     _instance_lock = threading.Lock()
#     def __init__(self):
#         time.sleep(1)

#     @classmethod
#     def instance(cls,*args,**kwargs):
#         with Singleton._instance_lock:
#             if not hasattr(Singleton,'_instance'):
#                 Singleton._instance = Singleton(*args,**kwargs)
#         return Singleton._instance
# def test(args):
#     a = Singleton.instance()
#     print(id(a))
# # b = Singleton.instance()


# for i in range(10):
#     t = threading.Thread(target=test,args=[i,])
#     t.start()

# time.sleep(5)
# a = Singleton.instance()
# print(id(a))


#             此时，我们再看看程序运行的结果：
#             anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176
#             140142050939176

#             到此，其实大致解决了我们的需求了，但是还是有一些小问题，就是当程序执行时，执行了time.sleep(20)后，下面实例化对象时，此时已经是单例模式了，但我们还是加了锁，这样不太好，再进行一些优化，把intance方法，改成下面的这样就行：


# import threading
# import time

# class Singleton(object):
#     _instance_lock = threading.Lock()
#     def __init__(self):
#         time.sleep(1)

#     @classmethod
#     def instance(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton,'_instance'):
#                     Singleton._instance = Singleton(*args,**kwargs)
#         return Singleton._instance
# def test(args):
#     a = Singleton.instance()
#     print(id(a))
# # b = Singleton.instance()


# for i in range(10):
#     t = threading.Thread(target=test,args=[i,])
#     t.start()

# time.sleep(5)
# a = Singleton.instance()
# print(id(a))

#             至此，支持多线程的单例实现结束，但这种方式还有弊端，不过不痛不痒了，很好发现：这种方式实现的单例，使用时会有限制，以后实例化对象必须通过调用类方法实现，即：
#             a = Singleton.instance()
#             而原本单单通过累的实例化，得到的就不是单例了。

        # 5.单例模式实现方式——基于__new__方法实现
        #     接上面的例子，已知，对于多线程情况下的单例，为了保证线程安全我们在内部加入了锁。
        #     同时，再引入一个知识点。当我们实例化对象的时候，是先执行了__new__方法(如果不写，会默认调用Object.__new__,因为现版本中都是新式类，新式类默认继承自object)实例化对象，再调用__init__方法初始化实例化对象。基于以上，我们可以使用__new__方法实现单例模式
# import threading
# import time

# class Singleton(object):
#     _instance_lock = threading.Lock()
#     def __init__(self):
#         time.sleep(1)
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton,'_instance'):
#                     Singleton._instance = object.__new__(cls)
#         return Singleton._instance

# # o1 = Singleton()
# # o2 = Singleton()
# # print(o1)
# # print(o2)

# def test(args):
#     o = Singleton()
#     print(id(o))

# for i in range(10):
#     t = threading.Thread(target=test,args=[i,])
#     t.start()

        # 6.单例模式实现方式——基于metaclass实现
        #     1.知识点补充
        #         1.Python中的类也是一个对象
        #         2.类是由元类来创建的
        #         3.type是众多类的元类
        #         4.类由type创建。创建类时，type的__init__()方法自动执行；类()，即由类实例化对象时，执行type的__call__()方法(其中包含__new__()和__init__()方法)
        #         5.对象由类创建。创建对象时，类的__init__()方法自动调用，对象()时执行类的__call__()方法
# import threading

# class SingletonType(type):
#     _instance_lock = threading.Lock()
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
#         return cls._instance

# class Foo(metaclass=SingletonType):
#     def __init__(self,name):
#         self.name = name


# obj1 = Foo('name')
# obj2 = Foo('name')
# print(obj1,obj2)
