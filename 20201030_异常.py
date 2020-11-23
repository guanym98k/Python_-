# try语句按照如下方式工作；
#     首先，执行try子句（在关键字try和关键字except之间的语句）
#     如果没有异常发生，忽略except子句，try子句执行后结束。
#     如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。
#     如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
#     如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
# finally 不管try子句里面有没有发生异常，finally子句都会执行
def demo1():
    while True:
        try:
            s = int(input("请尝试输入一个字符串,下面的except就会捕获到异常:"))
            break
        except ValueError as error:
            print("发生错误:转换整数类型失败,错误为:{0}".format(error))
        finally:
            print("无论什么情况下都会执行！")

# 使用 raise 语句抛出一个指定的异常
def demo2():
    raise NameError('HiThere')

# 用户自定义异常
# 你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承，例如:
class MyError(Exception):
    def __init__(self,value):
        self.value= value
    def _str_(self):
        return repr(self.value)

def demo3():
    try:
        raise MyError("自定义异常!")
    except MyError as e:
        print("发生异常：",e.value)

# 预定义的清理行为:
# 以下代码若没有with的话,就需要执行f.close()手动关闭,
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法.
def demo4():
    with open("MyFile.txt") as f:
        for line in f:
            print(line, end="")

# =======> 调用方法
demo4()