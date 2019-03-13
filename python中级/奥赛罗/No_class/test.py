
class A(object):
    def __init__(self):
        self.x=self.inputA()

    def inputA(self):
        return 'a'

class B(A):
    def __init__(self):
        A.__init__(self)
        self.x=self.inputB()
    def inputB(self):
        c=input()
        return c

zhengyix=B()
Zhengyix=A()
print(zhengyix.x)
print(Zhengyix.x)
print(zhengyix.x)
#A.__init__(self)
'''
class A:
    def __init__(self):
        self.namea="aaa"
    def funca(self):
        print "function a : %s"%self.namea
class B(A):
    def __init__(self):
        #这一行解决了问题
        A.__init__(self)
        self.nameb="bbb"
    def funcb(self):
        print "function b : %s"%self.nameb

b=B()
print b.nameb
b.funcb()
b.funca()
'''