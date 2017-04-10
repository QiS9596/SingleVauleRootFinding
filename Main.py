from abc import abstractclassmethod

class basicFunc:
    @abstractclassmethod
    def value(self, x):
        pass

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



from math import cos
from math import pi
class func1(basicFunc):
    def value(self, x):
        return cos(x) - x

falsePosition = FalsePosition(p0=0.5,p1=pi/4,func= func1())
print(falsePosition.solve())