23+1种设计模式——Python实现
一.基础概念介绍
	1.设计模式：
		设计模式是经过总结、优化的，对我们经常会碰到的一些编程问题的可重用解决方案。
	一个设计模式并不像一个类或一个库那样能够直接作用于我们的代码。反之，设计模式更为高级，它是一种必须在特定情形下实现的一种方法模板。
	设计模式不会绑定具体的编程语言。一个好的设计模式应该能够用大部分编程语言实现(如果做不到全部的话，具体取决于语言特性)。最为重要的是，
	设计模式也是一把双刃剑，如果设计模式被用在不恰当的情形下将会造成灾难，进而带来无穷的麻烦。
	然而如果设计模式在正确的时间被用在正确地地方，它将是你的救星。起初，你会认为“模式”就是为了解决一类特定问题而特别想出来的明智之举。
	说的没错，看起来的确是通过很多人一起工作，从不同的角度看待问题进而形成的一个最通用、最灵活的解决方案。
	也许这些问题你曾经见过或是曾经解决过，但是你的解决方案很可能没有模式这么完备。虽然被称为“设计模式”，但是它们同“设计“领域并非紧密联系
	。设计模式同传统意义上的分析、设计与实现不同，事实上设计模式将一个完整的理念根植于程序中，
	所以它可能出现在分析阶段或是更高层的设计阶段。很有趣的是因为设计模式的具体体现是程序代码，
	因此可能会让你认为它不会在具体实现阶段之前出现(事实上在进入具体实现阶段之前你都没有意识到正在使用具体的设计模式)。
	可以通过程序设计的基本概念来理解模式：增加一个抽象层。抽象一个事物就是隔离任何具体细节，
	这么做的目的是为了将那些不变的核心部分从其他细节中分离出来。当你发现你程序中的某些部分经常因为某些原因改动，
	而你不想让这些改动的部分引发其他部分的改动，这时候你就需要思考那些不会变动的设计方法了。这么做不仅会使代码可维护性更高，
	而且会让代码更易于理解，从而降低开发成本。
    2.抽象
        1.抽象方法：不包含任何可实现代码的方法就叫做抽象方法，即一个方法中没有任何一个方法体
        2.定义：抽象类是包含抽象方法的类，只能在其子类中实现抽象方法的代码
        3.抽象方法的定义
            1.导入abc模块
            import abc
            2.如果需要单个导入的话，一般我们只需要导入ABCMeta和abstractmethod就行
            from abc import ABCMeta,abstractmethod
            3.将元类设置为ABCMeta
            __metaclass__ = ABCMeta
            4.抽象方法前加装饰器abstractmethod
            @abstractmethod
        4.抽象类的特点：
            1.要定义但是并不完整的实现所有方法
            2.基本的大概意思其实就是父类
            3.父类需要明确表示出哪些方法的特征，
        5.需要使用抽象类的地方
            1.用作父类
            2.用作检验实例类型
            3.用作抛出异常说明
        
	2.设计模式分类：
		设计模式分为基本的三种类型：
			1.创建模式，提供实例化的方法，为适合的状况提供相应的对象创建方法。
			2.结构化模式，通常用来处理实体之间的关系，使得这些实体能够更好地协同工作。
			3.行为模式，用于在不同的实体建进行通信，为实体之间的通信提供更容易，更灵活的通信方法。
		具体包含以下分类：
		创建型
			1. Factory Method（工厂方法）
			2. Abstract Factory（抽象工厂）
			3. Builder（建造者）
			4. Prototype（原型）
			5. Singleton（单例）
		结构型
			6. Adapter Class/Object（适配器）
			7. Bridge（桥接）
			8. Composite（组合）
			9. Decorator（装饰）
			10. Facade（外观）
			11. Flyweight（享元）
			12. Proxy（代理）
		行为型
			13. Interpreter（解释器）
			14. Template Method（模板方法）
			15. Chain of Responsibility（责任链）
			16. Command（命令）
			17. Iterator（迭代器）
			18. Mediator（中介者）
			19. Memento（备忘录）
			20. Observer（观察者）
			21. State（状态）
			22. Strategy（策略）
			23. Visitor（访问者）
一.创建型模式
    1.工厂模式
        1.定义：定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。
        2.适用情况：
            1.当一个类不知道它所必须创建的对象的类的时候。
            2.当一个类希望由它的子类来指定它所创建的对象的时候。
            3.当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。
        3.工厂模式在实际应用中大致分为以下两类：
            1.简单工厂模式
            2.工厂方法模式
        举例：有一个学雷锋活动，有买米和扫地两个内容，参与的人有大学生和社区志愿者，他们各自的方法不一样。
简单工厂模式实现：
import abc
class Leifeng:
    '''定义雷锋抽象类，后续会有学生类和志愿者类继承该抽象类'''
    # __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def __init__(self):
        pass
    @abc.abstractmethod
    def but_rice(self):
        pass
    @abc.abstractmethod
    def sweep(self):
        pass

class Student(Leifeng):
    '''学生类，继承雷锋抽象类，重写两个抽象方法'''
    def buy_rice(self):
        print('大学生帮你买大米')
    def sweep(self):
        print('大学生帮你扫地')

class Volunteer(Leifeng):
    '''志愿者类，继承雷锋类，重写两个抽象方法'''
    def buy_rice(self):
        print('志愿者帮你买大米')
    def sweep(self):
        print('志愿者帮你扫地')

class LeifengFactory:
    '''创建雷锋工厂类，根据传入的参数类型返回相应对象'''
    def create_leifeng(self,type):
        map_ = {
            '大学生':Student(),
            '志愿者':Volunteer()
        }
        return map_[type]

if __name__ == '__main__':
    student1 = LeifengFactory().create_leifeng('大学生')
    # student2 = LeifengFactory().create_leifeng('大学生')
    vol1 = LeifengFactory().create_leifeng('志愿者')
    # vol2 = LeifengFactory().create_leifeng('志愿者')
    student1.buy_rice()
    student1.sweep()
    vol1.buy_rice()
    vol1.sweep()


工厂方法模式实现：
import abc
class Leifeng(object):
    '''定义一个雷锋基类，后续大学生类和志愿者类都要继承该类'''
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def but_rice(self):
        pass
    @abc.abstractmethod
    def sweep(self):
        pass

class Student(Leifeng):
    '''学生类，继承雷锋类，重写两个成员方法'''
    def buy_rice(self):
        print('大学生帮你买大米')
    def sweep(self):
        print('大学生帮你扫地')

class Volunteer(Leifeng):
    '''志愿者类，继承雷锋类，重写两个成员方法'''
    def buy_rice(self):
        print('志愿者帮你买大米')
    def sweep(self):
        print('志愿者帮你扫地')
#以上为工厂类
#以下为客户端(工厂方法类)
class LeifengFactory:
    '''定义雷锋工厂类，定义一个雷锋工厂方法'''
    @abc.abstractmethod
    def create_leifeng(self):
        pass

class StudentFactory(LeifengFactory):
    '''定义学生工厂类，继承雷锋工厂并重写雷锋工厂方法'''
    def create_leifeng(self):
        return Student()

class VolunteerFactory(LeifengFactory):
    '''定义志愿者工厂类，继承雷锋工厂并重写雷锋工厂方法'''
    def create_leifeng(self):
        return Volunteer()

if __name__ == '__main__':
    studentFactory = StudentFactory()#创建学生工厂对象
    student = studentFactory.create_leifeng()#通过学生工厂创建学生对象
    student.buy_rice()
    student.sweep()

    volunteerFactory = VolunteerFactory()#创建志愿者工厂对象
    vol = volunteerFactory.create_leifeng()#通过志愿者工厂创建志愿者对象
    vol.buy_rice()
    vol.sweep()

整体实现思路：
    雷锋类，大学生类，志愿者类和简单工厂一样，然后新写一个工厂方法基类，定义一个工厂方法接口（
    工厂方法模式的工厂方法应该就是指这个方法），然后写一个学生工厂类，志愿者工厂类，类中重写工厂方法，返回各自的类。

工厂方法模式相对于简单工厂模式的优点：
    在简单工厂中，如果需要新增类，例如加一个中学生类（MiddleStudent），就需要新写一个类，同时要修改工厂类的map_，加入'中学生':
MiddleStudent()。这样就违背了封闭开放原则中的一个'类写好后，尽量不要修改里面的内容'，这个原则。而在工厂方法中，
需要增加一个中学生类和一个中学生工厂类（MiddleStudentFactory），虽然比较繁琐，但是符合封闭开放原则。在工厂方法中，
将判断输入的类型，返回相应的类这个过程从工厂类中移到了客户端中实现，所以当需要新增类时，也是要修改代码的，
但此时，只需修改客户端的代码就行，工厂类的代码我们不需要修改。


    2.抽象工厂模式
        1.定义:提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
        2.适用情况：
            1.一个系统要独立于它的产品的创建、组合和表示时。
            2.一个系统要由多个产品系列中的一个来配置时。
            3.当你要强调一系列相关的产品对象的设计以便进行联合使用时。
            4.当你提供一个产品类库，而只想显示它们的接口而不是实现时。

举例：模拟向数据库用户表和部门表获取及插入数据，并且我们可能采用mysql和oracle数据库
import sys

class User(object):
    '''定义抽象user类，并定义抽象获取user数据方法，抽象插入user数据方法'''
    def get_user(self):
        pass

    def insert_user(self):
        pass

class Department(object):
    '''定义抽象department类，并定义抽象获取department数据方法，抽象插入department数据方法'''
    def get_department(self):
        pass

    def insert_department(self):
        pass
#以上为抽象类
#以下为具体操作数据库类
class MysqlUser(User):
    '''定义操作具体user数据库的类，继承抽象user类，采用mysql数据库实现'''
    def get_user(self):
        print('Mysqluser get user')
    def insert_user(self):
        print('Mysqluser insert user')

class MysqlDepartment(Department):
    '''定义操作具体department数据库的类，继承抽象department类，采用mysql数据库实现'''
    def get_department(self):
        print('Mysqldepartment get department')
    def insert_department(self):
        print('Mysqldepartment insert department')

class OracleUser(User):
    '''定义操作具体user数据库的类，继承抽象user类，采用Oracle数据库实现'''
    def get_user(self):
        print('Oracleuser get user')
    def insert_user(self):
        print('Oracleuser insert user')

class OracleDepartment(Department):
    '''定义操作具体department数据库的类，继承抽象department类，采用Oracle数据库实现'''
    def get_department(self):
        print('Oracledepartment get department')
    def insert_department(self):
        print('Oracledepartment insert department')

#以下为抽象工厂类
class AbstractFactory:
    '''定义抽象工厂类及抽象方法，后续mysql工厂类级oracle工厂类会继承该类'''
    def create_user(self):
        pass

    def create_department(self):
        pass

class MysqlFactory(AbstractFactory):
    '''定义mysql工厂类，继承抽象工厂类'''
    def create_user(self):
        return MysqlUser()

    def create_department(self):
        return MysqlDepartment()


class OracleFactory(AbstractFactory):
    '''定义Oracle工厂类，继承抽象工厂类'''
    def create_user(self):
        return OracleUser()

    def create_department(self):
        return OracleDepartment()

if __name__ == '__main__':
    db = input('请输入数据库类型：')
    myfactory = ''
    if db == 'mysql':
        myfactory = MysqlFactory()
    elif db == 'oracle':
        myfactory = OracleFactory()
    else:
        print('不支持的数据库类型')
        sys.exit()

    user = myfactory.create_user()
    department = myfactory.create_department()
    user.insert_user()
    user.get_user()
    department.insert_department()
    department.get_department()

    抽象工厂类优点：
        1.具体工厂类如MysqlFactory在一个应用中只需要初始化一次，这样改动一个具体工厂变得很容易，
        只需要改变具体工厂就可以改变整个产品的配置。
        2.具体的创建实例过程与客户端分离，客户端通过他们的抽象接口操纵实例，产品的具体类名也被具体工厂的实现分离，
        不会出现在客户端代码中
    抽象工厂类缺点：
        在新增一个具体工厂就需要增加多个类才能实现

    3.建造者模式
        1.定义：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
        2.适用情况：
            1.当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时。
            2.当构造过程必须允许被构造的对象有不同的表示时。
        举例：建筑工程师(指挥者)指挥工人(建造者)建造

class Builder(object):
    '''定义建造者抽象类，定义抽象方法用于子类继承'''
    def create_footer(self):
        pass

    def create_body(self):
        pass

    def create_header(self):
        pass

class Thin(Builder):
    '''定义瘦子类，继承抽象方法并重写'''
    def create_footer(self):
        print('瘦子的脚创建了')

    def create_body(self):
        print('瘦子的身体创建了')

    def create_header(self):
        print('瘦子的头创建了')

class Fat(Builder):
    '''定义胖子类，继承抽象方法并重写'''
    def create_footer(self):
        print('胖子的脚创建了')

    def create_body(self):
        print('胖子的身体创建了')

    def create_header(self):
        print('胖子的头创建了')

class Director(object):
    '''定义指挥者类，根据传入参数决定调用哪个子类的方法'''
    def __init__(self,person):
        self.person = person
    def create_person(self):
        self.person.create_footer()
        self.person.create_body()
        self.person.create_header()

if __name__ == '__main__':
    thin = Thin()
    fat = Fat()
    direct_thin = Director(thin)
    direct_fat = Director(fat)
    direct_thin.create_person()
    direct_fat.create_person()

    4.原型模式
        1.定义：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
        2.适用情况：
            1.当要实例化的类是在运行时刻指定时，例如，通过动态装载；或者为了避免创建一个与产品类层次平行的工厂类层次时；
            或者当一个类的实例只能有几个不同状态组合中的一种时。
            2.需要大量的基于某个基础原型进行微量修改而得到新原型时使用
        举例：投递简历，需要引用你的过往工作经历。

from copy import copy,deepcopy
class Prototype(object):
    '''创建原型抽象类，用于子类继承'''
    def clone(self):
        pass

    def deep_clone(self):
        pass

class WorkExp(object):
    '''创建工作经验类，定义添加工作经验方法'''
    def __init__(self):
        self.timearea = ''
        self.company = ''

    def set_workexp(self,timearea,company):
        self.timearea = timearea
        self.company = company

class Resume(Prototype):
    '''创建简历类，继承原型抽象类，重写抽象方法的同时添加部分属性'''
    def __init__(self,name):
        self.name = name
        self.workexp = WorkExp()

    def set_personinfo(self,sex,age):
        self.sex = sex
        self.age = age

    def set_workexp(self,timearea,company):
        self.workexp.set_workexp(timearea,company)

    def display(self):
        print(self.name)
        print(self.sex,self.age)
        print('工作经历：%s,%s'%(self.workexp.timearea,self.workexp.company))

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)

if __name__ == '__main__':
    obj1 = Resume('安伟超')
    obj2 = obj1.clone()
    obj3 = obj1.deep_clone()

    obj1.set_personinfo('男',30)
    obj1.set_workexp('2016-2018','达内时代科技集团天津天大中心')

    obj2.set_personinfo('男',32)
    obj2.set_workexp('2018-2020','达内时代科技集团天津学府中心')

    obj3.set_personinfo('男',34)
    obj3.set_workexp('2020-2022','达内时代科技集团天津长虹中心')

    obj1.display()
    obj2.display()
    obj3.display()

    简历类Resume继承抽象原型的clone和deepclone方法，实现对简历类的复制，并且简历类引用工作经历类，
    可以在复制简历类的同时修改局部属性

    5.单例模式
        1.定义：单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
            举例：比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
            我们先看看单例模式问题从何而来：
class A(object):
    def __init__(self):
        pass
    def foo(self):
        pass

a = A()
print(id(a))
b = A()
print(id(b))
            运行结果如下：
            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
            140534096496512
            140534096497128
            很明显，通过打印实例的id可以发现，A类默认被创建了两个实例a和b
            那么，如何让类只去实例化一个对象，而后再创建的实例是返回上一次的对象的引用呢？
        2.单例模式实现方式——使用模块
            其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：   
创建一个单例模块mysingleton.py

mysingleton.py
class Singleton(object):
    def __init__(self):
        self.name = '小安安'
    def foo(self):
        print('我是：%s'%self.name)
singleton = Singleton()


from mysingleton import singleton
singleton.foo()

        3.单例模式实现方式——使用装饰器

def singleton(cls,*args,**kwargs):
    '''
    使用装饰器的原理：
    1.先创建外层函数，需要传入一个参数，此参数为类(对象)
    2.创建一个空字典，用来保存单例
    3.创建一个内层函数，用来获得单例
    4.内层函数中进行判断：如果当前字典不存在单例，就创建单例，如果存在，直接返回该单例的引用
    5.外层函数返回内层函数

    '''
    instances = {}
    print('装饰器函数被调用！')
    def get_singleton(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        print('装饰器内层函数也被调用！')
        print(instances)
        return instances[cls]
    return get_singleton

@singleton
#此处，相当于：Student = singleton(Student)
class Student(object):
    '''
    创建单例的原理：
    1.先由类实例化对象：xiaoanan = Student(30,'小安安')并传参，此时，因为前面已添加装饰器@singleton，Student此时相当于绑定到了get_singleton函数，这句实例化对象的语句其实就是如下格式：xiaoanan = get_singleton(30,'小安安'),而实例化对象时，这句话相当于调用了装饰器的内部函数get_singleton，因为是第一次创建对象xiaoanan ,当前字典中并没有单例xiaoanan,所以内层函数get_singleton中会执行if语句真值表达式为True时的语句，即：instances[cls] = cls(*args,**kwargs)，而这里的cls接收到的参数是Student，所以此句代码相当于：instances[Student] = Student(30,'小安安'),即给字典键名为Student的键添加一个值，这个值是Student类实例化的对象
    2.当又一次实例化对象xiaochaochao时，因为仍然还是通过Student类实例化该对象，而之前的单例已经存在于字典中了，所以不会再创建第二个单例，只会直接返回已有的单例并绑定当前的引用，进而真正实现了单例模式！
    
    '''
    def __init__(self,age,name):
        self.age = age
        self.name = name
        print('__init__()方法被调用了')
xiaoan = Student(30,'小安安')
xiaochaochao = Student(18,'小超超')
print(id(xiaoan))
print(id(xiaochaochao))

            最终执行结果：
            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
            装饰器函数被调用！
            __init__()方法被调用了
            装饰器内层函数也被调用！
            {<class '__main__.Student'>: <__main__.Student object at 0x7fe08913f748>}
            装饰器内层函数也被调用！
            {<class '__main__.Student'>: <__main__.Student object at 0x7fe08913f748>}
            140602349188936
            140602349188936

            此方式即实现了单例模式。



        4.单例模式实现方式——使用类
import threading
import time

class Singleton(object):
    def __init__(self):
        # time.sleep(1)
        pass

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,'_instance'):
            Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance
def test(args):
    a = Singleton.instance()
    print(id(a))
# b = Singleton.instance()


for i in range(10):
    t = threading.Thread(target=test,args=[i,])
    t.start()

            程序暂时先写成这样，我们先运行一下，看看结果：
            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            140291643101480
            看上去，没毛病，恩，实现了单例，但其实！有毛病！此时看上去没问题是因为执行速度过快，如果我们让__init__方法存在一些IO操作，就会发现问题。
            下面，我们用睡眠代替可能的IO操作看看会出现什么效果

import threading
import time

class Singleton(object):
    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,'_instance'):
            Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance
def test(args):
    a = Singleton.instance()
    print(id(a))
# b = Singleton.instance()


for i in range(10):
    t = threading.Thread(target=test,args=[i,])
    t.start()

            此时，我们再看看程序运行的结果：
            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
            140107826004320
            140107826107280
            140107825398672
            140107825883008
            140107825392944
            140107825882896
            140107825398952
            140107826107504
            140107825835816
            140107825881496

            问题出现了！按照以上方式创建的单例，不支持多线程！
            ok，如果非得采用这种方式来创建单例，解决办法是：加锁！
            未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全
            再看如下代码：

import threading
import time

class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls,*args,**kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton,'_instance'):
                Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance
def test(args):
    a = Singleton.instance()
    print(id(a))
# b = Singleton.instance()


for i in range(10):
    t = threading.Thread(target=test,args=[i,])
    t.start()

time.sleep(5)
a = Singleton.instance()
print(id(a))


            此时，我们再看看程序运行的结果：
            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
            140142050939176
            140142050939176
            140142050939176
            140142050939176
            140142050939176
            140142050939176
            140142050939176
            140142050939176
            140142050939176
            140142050939176

            到此，其实大致解决了我们的需求了，但是还是有一些小问题，就是当程序执行时，执行了time.sleep(20)后，下面实例化对象时，此时已经是单例模式了，但我们还是加了锁，这样不太好，再进行一些优化，把intance方法，改成下面的这样就行：


import threading
import time

class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,'_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton,'_instance'):
                    Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance
def test(args):
    a = Singleton.instance()
    print(id(a))
# b = Singleton.instance()


for i in range(10):
    t = threading.Thread(target=test,args=[i,])
    t.start()

time.sleep(5)
a = Singleton.instance()
print(id(a))

            至此，支持多线程的单例实现结束，但这种方式还有弊端，不过不痛不痒了，很好发现：这种方式实现的单例，使用时会有限制，以后实例化对象必须通过调用类方法实现，即：
            a = Singleton.instance()
            而原本单单通过累的实例化，得到的就不是单例了。

        5.单例模式实现方式——基于__new__方法实现
            接上面的例子，已知，对于多线程情况下的单例，为了保证线程安全我们在内部加入了锁。
            同时，再引入一个知识点。当我们实例化对象的时候，是先执行了__new__方法(如果不写，会默认调用Object.__new__,因为现版本中都是新式类，新式类默认继承自object)实例化对象，再调用__init__方法初始化实例化对象。基于以上，我们可以使用__new__方法实现单例模式
import threading
import time

class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        time.sleep(1)
    def __new__(cls,*args,**kwargs):
        if not hasattr(Singleton,'_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton,'_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

# o1 = Singleton()
# o2 = Singleton()
# print(o1)
# print(o2)

def test(args):
    o = Singleton()
    print(id(o))

for i in range(10):
    t = threading.Thread(target=test,args=[i,])
    t.start()

        6.单例模式实现方式——基于metaclass实现
            1.知识点补充
                1.Python中的类也是一个对象
                2.类是由元类来创建的
                3.type是众多类的元类
                4.类由type创建。创建类时，type的__init__()方法自动执行；类()，即由类实例化对象时，执行type的__call__()方法(其中包含__new__()和__init__()方法)
                5.对象由类创建。创建对象时，类的__init__()方法自动调用，对象()时执行类的__call__()方法
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonType):
    def __init__(self,name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1,obj2)
二.结构型模式
    1.适配器模式
        1.定义：将一个类的接口转换成为客户希望的另外一个接口，使得原本由于接口不兼容而不能一起工作的那些类可以一起工作.
        2.适用情况：系统数据和行为都正确,但接口不符合时,目的是使控制范围之外的一个原有对象与某个接口匹配,适配器模式主要应用于希望复用一些现存的类,但接口又与复用环境不一致的情况

class Target(object):

    def request(self):
        print('普通请求')

class Adaptee(object):

    def specific_request(self):
        print('特殊请求')

class Adapter(Target):

    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()

if __name__ == "__main__":
    target = Adapter()
    target.request()


    # 2.桥接模式
    #     1.定义：将抽象部分与它的实现部分分离，使它们都可以独立地变化
    #     2.核心思想：桥接模式的核心意图就是把类的实现独立出来，让他们各自变化。这样使每种实现的变化不会影响其他实现，从而达到应对变化的目的


# 抽象手机软件类
class HandsetSoft(object):

    def run(self):
        pass

#具体游戏类,游戏是手机软件,继承抽象手机软件类
class HandsetGame(HandsetSoft):

    def run(self):
        print "运行手机游戏"

#手机通讯录
class  HandsetAddressList(HandsetSoft):

    def run(self):
        print "运行通信录"


#抽象手机品牌类
class HandsetBrand(object):

    def __init__(self):
        self.soft = ""

    def set_handsetsoft(self,soft):
        self.soft = soft

    def run(self):
        pass

# 手机品牌N
class HandsetBrandN(HandsetBrand):

    def run(self):
        self.soft.run()

# 手机品牌M
class HandsetBrandM(HandsetBrand):

    def run(self):
        self.soft.run()

if __name__ == "__main__":
    game = HandsetGame()
    address = HandsetAddressList()

    phoneN = HandsetBrandN()
    phoneN.set_handsetsoft(game)
    phoneN.run()

    phoneM = HandsetBrandM()
    phoneM.set_handsetsoft(address)
    phoneM.run()


    # 3.组合模式
    #     1.定义：将对象组合成成树形结构以表示“部分-整体”的层次结构,组合模式使得用户对单个对象和组合对象的使用具有一致性.
    #     2.适用情况：
    #         1.在需要体现部分与整体层次的结构时
    #         2.希望用户忽略组合对象与单个对象的不同，统一的使用组合结构中的所有对象时

from abc import ABCMeta,abstractmethod
class Component(object):
    '''定义抽象组织类，用于子类继承'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add(self,comp):
        pass

    @abstractmethod
    def remove(self,comp):
        pass

    @abstractmethod
    def display(self, depth):
        pass


class Leaf(Component):
    '''定义叶子节点类，继承抽象类，重写抽象方法'''
    def add(self,comp):
        print('不能添加叶子节点')

    def remove(self,comp):
        print("不能删除叶子节点")

    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += strtemp+'-'
        print(strtemp+self.name)



class Composite(Component):
    '''定义非叶子节点类，继承抽象类，重写抽象方法'''
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self,comp):
        self.children.append(comp)

    def remove(self,comp):
        self.children.remove(comp)

    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += strtemp+'-'
        print(strtemp+self.name)
        for comp in self.children:
            comp.display(depth+2)

if __name__ == "__main__":
    #生成树根
    root = Composite("root")
    #根上长出2个叶子
    root.add(Leaf('leaf A'))
    root.add(Leaf('leaf B'))

    #根上长出树枝Composite X
    comp = Composite("Composite X")
    comp.add(Leaf('leaf XA'))
    comp.add(Leaf('leaf XB'))
    root.add(comp)

    #根上长出树枝Composite X
    comp2 = Composite("Composite XY")
    #Composite X长出2个叶子
    comp2.add(Leaf('leaf XYA'))
    comp2.add(Leaf('leaf XYB'))
    root.add(comp2)
    # 根上又长出2个叶子,C和D,D没张昊,掉了
    root.add(Leaf('Leaf C'))
    leaf = Leaf("Leaf D")
    root.add(leaf)
    root.remove(leaf)
    #展示组织
    root.display(1)


    4.装饰模式
        1.定义：动态的给一个对象添加一些额外的职责,就增加功能来说,装饰模式比生成子类更为灵活
        2.特点：有效的把类的核心职责和装饰功能区分开,而且可以去除相关类中重复的装饰逻辑
# 定义对象接口
class Person(object):
    def __init__(self,name):
        self.name = name
    def show(self):
        print("装扮的%s"%self.name)

#装饰类
class Finery(Person):
    def __init__(self):
        pass
    def Decorate(self,componet):
        self.componet = componet
    def show(self):
        if self.componet != None:
            self.componet.show()

#装扮——T恤
class TShirts(Finery):
    def __init__(self):
        pass
    def show(self):
        print('T恤')
        self.componet.show()

#装扮——大裤衩
class BigTrouser(Finery):
    def __init__(self):
        pass
    def show(self):
        print('大裤衩')
        self.componet.show()

# 装扮——人字拖
class FlipFlops(Finery):
    def __init__(self):
        pass
    def show(self):
        print('人字拖')
        self.componet.show()

if __name__ == '__main__':
    p = Person('Andy')
    ff = FlipFlops()
    bt = BigTrouser()
    ts = TShirts()
    ff.Decorate(p)
    bt.Decorate(ff)
    ts.Decorate(bt)
    ts.show()

    5.外观模式
        1.定义：为子系统中的一组接口提供一个一致界面,此模式定义一个高层接口,使得子系统更加容易使用

# 外观类
class Fund(object):
    def __init__(self):
        self.stocka = StockA()
        self.stockb = StockB()
        self.realty = Realty()
    def buy(self):
        self.stocka.buy()
        self.stockb.buy()
        self.realty.buy()
    def sell(self):
        self.stocka.sell()
        self.stockb.sell()
        self.realty.sell()
# 投资股票A类
class StockA(object):
    def buy(self):
        print('buy StockA')
    def sell(self):
        print('sell StockA')
# 投资股票B类
class StockB(object):
    def buy(self):
        print('buy StockB')
    def sell(self):
        print('sell StockB')
# 投资房地产
class Realty(object):
    def buy(self):
        print('buy Realty')
    def sell(self):
        print('sell Realty')



if __name__=="__main__":
    fund = Fund()
    fund.buy()
    fund.sell()


    6.享元模式
        1.定义：运用共享技术有效地支持大量细粒度的对象.
        享元模式可以避免大量非常相似类的开销，在程序设计中，有时会生成大量细粒度的类实例来表示数据，如果这些实例除了几个参数外基本相同，就可以把参数已到实例外面，在方法调用时，把它们传进来，就可以通过共享大幅度减少单个实例的数目

# 抽象网站类
class Website(object):
    def use(self):
        pass

# 具体网站类
class ConcreteWebsite(Website):
    def __init__(self, name):
        self.name = name
    def use(self):
        print("网站分类",self.name)
# 不共享的网站类
class UnshareConcreteWebsite(Website):
    def __init__(self, name):
        self.name = name
    def use(self):
        print("不共享网站分类",self.name)
# 网站工厂
class WebsiteFactory(object):
    def __init__(self):
        self.hashtable = dict()
    # 获取网站类  如果存在直接返回,如果不存在建好之后返回
    def get_website(self, key):
        if not key in self.hashtable:
            self.hashtable[key] = ConcreteWebsite(key)
        return self.hashtable[key]
    # 网站实例的个数
    def get_website_count(self):
        return len(self.hashtable.keys())
if __name__ == "__main__":
    factory = WebsiteFactory()
    f1 = factory.get_website("blog")
    f2 = factory.get_website("blog")
    f3 = factory.get_website("blog")
    f4 = factory.get_website("website")
    f5 = factory.get_website("website")
    f6 = factory.get_website("website")
    f7 = UnshareConcreteWebsite("test")
    f1.use()
    f2.use()
    f3.use()
    f4.use()
    f5.use()
    f6.use()
    f7.use()
    