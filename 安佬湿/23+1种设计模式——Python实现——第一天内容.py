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
