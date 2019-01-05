1.什么是python自省
    如果说能够通过一个函数就能学会Python，那这个函数是什么？没错，help()。help()函数的作用就是查看对象的帮助文档。比如：
    anwc@anwc:/media/anwc/帅无敌的小安安/课程资料$ python3
    Python 3.6.5 (default, Apr  1 2018, 05:46:30)
    [GCC 7.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> help(123)
    Help on int object:


    class int(object)


    |  int(x=0) -> integer
    |  int(x, base=10) -> integer
    |
    |  Convert a number or string to an integer, or return 0 if no arguments
    |  are given.  If x is a number, return x.__int__().  For floating point
    |  numbers, this truncates towards zero.
    |
    |  If x is not a number or if base is given, then x must be a string,
    |  bytes, or bytearray instance representing an integer literal in the
    |  given base.  The literal can be preceded by '+' or '-' and be surrounded
    |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    |  Base 0 means to interpret the base from the string as an integer literal.
    | >> > int('0b100', base=0)

    ...

    内容很多，就不一一复制了，help()函数其实就是查看对象的帮助文档，类似于把帮助文档放到linux命令中的less中的效果，按下q就可以退出。
    上面的例子，显示了 int 对象的帮助文档，int 是内置类型，代码在编译 Python 的时候已经 编译过了，没有.py 的源代码。
    那么我们来看看，help 到底有什么功能，看下面：
    >>> help(help)
    Help on _Helper in module _sitebuiltins object:


    class _Helper(builtins.object)


    |  Define the builtin 'help'.
    |
    |  This is a wrapper around pydoc.help that provides a helpful message
    |  when 'help' is typed at the Python interactive prompt.
    |
    |  Calling help() at the Python prompt starts an interactive help session.
    |  Calling help(thing) prints help for the python object 'thing'.
    |
    |  Methods defined here:
    |
    |  __call__(self, *args, **kwds)
    |      Call self as a function.
    |

    :
    如上可以看到，help()函数加与不加参数都可以使用：
    >> > help()

    Welcome to Python 3.6's help utility!

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at https: // docs.python.org/3.6/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, symbols, or topics, type
    "modules", "keywords", "symbols", or "topics".  Each module also comes
    with a one-line summary of what it does
    to list the modules whose name
    or summary contain a given string such as "spam", type "modules spam".

    help >
    问题继续抛出：我们如何知道Python中还有哪些元素等待探索，我们怎么找到这些元素呢？
    ok，来看看Python自带说明的第二个函数dir()
    我们先用help()查看下这个函数的帮助文档：
    >>> help(dir)

    Help on built-in function dir in module builtins:

    dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising(some of) the attributes of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used
    otherwise
    the default dir() logic is used and returns:

    for a module object:
        the module's attributes.
    for a class object:
        its attributes, and recursively the attributes

    of its bases.
    for any other object:
        its attributes, its class's attributes, and

    recursively the attributes of its class's base classes.

    简单的讲，dir 就是把这个对象有的属性(非模块对象也包括类属性，父类属性等)都列出来放到一个 list 中。若对象有__dir__方法，就调用该方法，否则就用默认的方法
    
    接下来，我们使用dir函数查看下help函数内都有什么：
    >>> dir(help)
    ['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
        '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    如上可以看到help()函数有这些属性

    问题继续来，如果我想查看Python里所有的东西呢，不管他是属性还是方法还是对象，我都想看，咋整？
    很简单，dir()函数不传递参数，如下：
    >>> dir()

    ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

    这个builtins，是内置的意思，也就是这个属性里存放的都是内置对象！？看看：
    >>> dir(__builtins__)
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError',
        'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', '_format', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'xrange', 'zip']
    嚯，很多， 刚才我们使用的help,dir也都在里面，随便验证一个：
    >>> abs
    <built-in function abs >
    是吧，内置对象。
    Python的内置函数和对象有很多，慢慢学吧。
    下面我们来看几个有意思的函数：
    1.callable
    这个呢，表示的是函数的调用的意思，也就是说函数调用时用的就是他，验证一下：
    Help on built-in function callable in module builtins:

    callable(obj, /)
    Return whether the object is callable(i.e., some kind of function).

    Note that classes are callable, as are instances of classes with a
    __call__() method.
    (END)

    解读如上文档，意思很明白，返回对象能不能调用，能调用就返回True，不能调用就返回False
    试一下：
    >>> def f():
    ... pass
    ...
    >> > callable(f)
    True
    在试试匿名函数。
    >> > callable(lambda x: x)
    True
    帮助文档说了类可调用，类的实例若有__call__属性也能调用。 那么怎么知道对象有没有__call__属性呢?

    2.hasattr
    先help一下：
    Help on built-in function hasattr in module builtins:

    hasattr(obj, name, / )
    Return whether the object has an attribute with the given name.

    This is done by calling getattr(obj, name) and catching AttributeError.
    (END)
    这个函数其实属于对象属性管理函数，作用很简单，返回对象是否具有某一个属性，可是！上面的这段帮助文档写的很清楚，这是通过getattr来实现的！
    3.getattr
    看下getattr的帮助文档：
    >>> help(getattr)
    Help on built-in function getattr in module builtins:

    getattr(...)
    getattr(object, name[, default]) -> value

    Get a named attribute from an object
    getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist
    without it, an exception is raised in that case.
    由上看出：getattr(object, name[, default])就是获取 object 对象的 name 属性，若 name 不
    存在，若定义了 default 参数返回 default，否则抛出异常。
    
    由上，讲了很多，其实第123行为止，就已经说完了自省。

    总结一下：自省，简单点说，就是Python的自带说明，意思就是用Python的代码自己告诉这个对象是什么，有什么，以及列祖列宗是谁，孙子们又是谁。

    精华一句话：Python提供的自省机制是：help() and dir().

2.鸭子类型
    1.python不支持多态也用不到多态，多态的概念是应用于java和C#  这一类强类型语言中，而Python崇尚鸭子类型（Duck Typing）
    
    2.鸭子类型：是一种动态类型的风格。一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。这个概念的名字来源于由James Whitcomb Riley提出的鸭子测试，“鸭子测试”可以这样表述：“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
    
    3.在鸭子类型中，关注的不是对象类型本身，而是它是如何使用的。我们可以编写一个函数，它接受一个类型为鸭的对象，并调用它的走和叫方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的走和叫方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。

    class F1:
        pass

    # 假设，S1是我们的正统类，它继承于根正苗红的F1，是我们的正统类
    class S1(F1):
        def show(self):
            print('S1.show')

    # S2是路人甲，是个歪瓜裂枣，但是他自己也有一个叫show的方法。
    class S2:
        def show(self):
            print('S2.show')


    # 在Java或C#中定义函数参数时，必须指定参数的类型，也即是说，我们如果用
    # Java写下面的Func，需要告知，obj是F1类还是其他什么东西。
    # 如果限定了F1，那么S2是不可以被采纳的。
    # 然而，在Python中，一切都是Obj，它不care你到底是什么类，直接塞进去就可以

    def Func(obj):
        """Func函数需要接收一个F1类型或者F1子类的类型"""
        obj.show()

    s1_obj = S1()
    Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show

    s2_obj = S2()
    Func(s2_obj)  # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show

3.虚拟内存技术
    参考文献：https://baike.baidu.com/item/%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98/101812?fr=aladdin
    来自百度百科(常识问题，作了解即可)

4.