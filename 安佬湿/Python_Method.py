# 1.python面向对象中各种方法的具体使用情况
# class A(object):
#     def __init__(self):
#         print("A类的构造方法被调用啦！")
#
#     def __del__(self):
#         print("A类的析构方法被调用啦！")
#     #实例方法
#     def fun(self):
#         print("A类的实例方法被调用啦！")
#
#     #类方法
#     @classmethod
#     def class_fun(cls):
#         print("A类的类方法被调用啦！")
#
#     #静态方法
#     @staticmethod
#     def static_fun():
#         print("A类的静态方法被调用啦！")


# a = A()
#
# print('======我是一条美丽的分割线======')
# #查看规律：
# # 1.先用类分别调用三种方法
# try:
#     A.fun()
# except TypeError:
#     print("类无法调用实例方法！")
# A.class_fun()
# A.static_fun()
# # 2.再用由类实例化过来的对象调用三种方法
# print('======我是一条美丽的分割线======')
# a.fun()
# a.class_fun()
# a.static_fun()


# 由此 我们可以得出以下规律：
#             实例方法            类方法                 静态方法
# a = A()     a.fun()            a.class_fun()          a.static_fun()
# A           不可用              A.class_fun()          A.static_fun()

# 即：类方法，静态方法，类和由类实例化出来的对象，皆可直接调用！
# 对于实例方法，只能由类实例化的对象进行调用，类本身无法直接调用实例方法


# 2.子类中是否能够调用父类的成员方法？类方法？静态方法？

# class B(A):
#     def __init__(self):
#         pass
#     def fun(self):
#         super(B,self).fun()
#         super(B,self).static_fun()
#         super(B,self).class_fun()
#         print("B是子类，调用B的实例方法")
#
# b = B()
# b.fun()
# 结论：子类可以任意调用父类的成员方法或类方法或静态方法

# 3.python中子类如何调用父类的构造方法？

#
# class A(object):
#     def __init__(self):
#         self.name = '安伟超'
#         print(self.name)
#     def fun(self):
#         print("A类的实例方法被调用！")
#
# class B(A):
#     def __init__(self):
#         # 方法1：直接用超类调用自身构造方法即可
#         # A.__init__(self)
#         # 方法2：使用super函数调用超类的构造方法即可
#         # super(B,self).__init__()
#         self.name = '小安安'
#         print(self.name)
#     def fun(self):
#         print("B类的实例方法被调用！")
#
# b = B()
# # print(b.name)
# # b.fun()


# 4.MRO：方法解析顺序
# /先看实例：
# class K(object):
#     pass
# class H(K):
#     pass
# class J(K):
#     pass
# class E(H):
#     pass
# class D(H):
#     pass
# class F(J):
#     pass
# class G(J):
#     pass
# class B(E,D):
#     pass
# class C(F,G):
#     pass
# class A(B,C):
#     pass
# print(A.__mro__)

# class A(object):
#     def f(self):
#         print("A类的方法被调用！")
# class B(object):
#     def f(self):
#         print("B类的方法被调用！")
#
# class C(A,B):
#     def f(self):
#         super(C,self).f()
#         print("C类的方法被调用！")
#
# c = C()
# c.f()

# class A(object):
#
#     def __init__(self):
#         print
#         "enter A"
#
#         print
#         "leave A"
#
#
# class B(object):
#
#     def __init__(self):
#         print
#         "enter B"
#
#         print
#         "leave B"
#
#
# class C(A):
#
#     def __init__(self):
#         print
#         "enter C"
#
#         super(C, self).__init__()
#
#         print
#         "leave C"
#
#
# class D(A):
#
#     def __init__(self):
#         print
#         "enter D"
#
#         super(D, self).__init__()
#
#         print
#         "leave D"
#
#
# class E(B, C):
#
#     def __init__(self):
#         print
#         "enter E"
#
#         B.__init__(self)
#
#         C.__init__(self)
#
#         print
#         "leave E"
#
#
# class F(E, D):
#
#     def __init__(self):
#         print
#         "enter F"
#
#         E.__init__(self)
#
#         D.__init__(self)
#
#         print
#         "leave F"
#
#
# f = F()
#
#




