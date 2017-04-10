from abc import abstractclassmethod

class basicFunc:
    @abstractclassmethod
    def value(self, x):
        pass
    def __str__(self):
        return self.intro_str

class solvingAgent:
    MAX_ITER = 500
    DEFAULT_TOL = pow(10,-8)
    @abstractclassmethod
    def solve(self):
        pass


class FalsePosition(solvingAgent):

    def __init__(self, p0, p1, func):
        self.func = func
        self.q0 = self.func.value(p0)
        self.q1 = self.func.value(p1)
        self.p1 = p1
        self.p0 = p0

    def solve(self):
        i = 0
        while i < self.MAX_ITER:
            self.p = self.p1 - self.q1*(self.p1 - self.p0)/(self.q1 -self.q0)

            if abs(self.p - self.p1) < self.DEFAULT_TOL:
                print(i)
                return self.p

            i += 1
            self.q = self.func.value(self.p)

            if self.q*self.q1 < 0:
                self.p0 = self.p1
                self.q0 = self.q1

            self.p1 = self.p
            self.q1 = self.q

        print("Too many iterations")
        return

class Bisection(solvingAgent):
    def __init__(self, a, b, func):
        self.a = a
        self.b = b
        self.func = func

    def solve(self):
        i = 0
        FA = self.func.value(self.a)

        while i < self.MAX_ITER:
            self.p = self.a + (self.b - self.a)/2
            FP = self.func.value(self.p)

            if (FP == 0) or ((self.b - self.a)/2 < self.DEFAULT_TOL):
                print(i)
                return self.p

            i += 1

            if FA*FP > 0:
                self.a = self.p
                FA = FP
            else:
                self.b = self.p

        print("Too many Iterations")
        return

class NewtonMethod(solvingAgent):
    def __init__(self, initialGuess, func):
        self.initialGuess = initialGuess
        self.func = func
    def solve(self):
        i = 0
        while i < self.MAX_ITER:
            p = self.initialGuess - self.func.value(self.initialGuess)/self.d(self.initialGuess)

            if abs(p - self.initialGuess) < self.DEFAULT_TOL:
                print(i)
                return p

            i += 1

            self.initialGuess = p

    def d(self,v):
        return (self.func.value(v+0.01)-self.func.value(v-0.01))/0.02

from math import sin
from math import cos
from math import pi
from math import e
class func1(basicFunc):
    def __init__(self):
        self.intro_str = " f(x) = x^2-3"
    def value(self, x):
        return x*x-3
class func2(basicFunc):
    def __init__(self):
        self.intro_str = " f(x) = e^(-x) * (3.2sin(x)-0.5cos(x))"
    def value(self, x):
        return pow(e,-x)*(3.2*sin(x)-0.5*cos(x))


print("function" + func1().__str__())
falsePosition = FalsePosition(p0=1,p1=2,func= func1())
bisection = Bisection(a = 1, b = 2, func= func1())
print("false position method:")
print(falsePosition.solve())
print("bisection method")
print(bisection.solve())
print("newton method")
newtonMethod = NewtonMethod(1,func1())
print(newtonMethod.solve())

print("function" + func2().__str__())
falsePosition = FalsePosition(p0=2,p1=4,func= func2())
bisection = Bisection(a = 2, b = 4, func= func2())
print("false position method:")
print(falsePosition.solve())
print("bisection method")
print(bisection.solve())
