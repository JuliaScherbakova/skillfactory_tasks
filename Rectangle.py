import math

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __int__(self, r):
        self.r = r
        math.pi
    def get_area_circle(self):
        return math.pi * (self.r ** 2)