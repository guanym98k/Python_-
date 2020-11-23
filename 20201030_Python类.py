# 类对象:类对象支持两种操作：属性引用和实例化。

# 实例化
class MyClass:
    # __init__ 是构造函数,很多类都倾向于将对象创建为有初始状态的。
    # 因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = MyClass(3.0,4.5)
print(x.r,"--",x.i)

# 类的方法
# 在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数:
class people:
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s is speaking : i am %d years old , i am %d" %(self.name,self.age,self.__weight))

# 创建实例
p = people('John',10,50)
p.speak()

# 继承
# 创建一个类，继承上边的people类
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        # 调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade=g
    # 覆写父类的方法
    def speak(self):
        print("%s is speaking : i am %d years old and i am in grade %d" %(self.name,self.age,self.grade))
s = student('Danny',10,30,1)
s.speak()

class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("I am %s,I am a speaker!My topic is %s" % (self.name, self.topic))

# 多重继承 分别继承speaker类、student类
class sample(speaker,student):
    a =''

    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()#方法名同，默认调用的是在括号中排前地父类的方法
