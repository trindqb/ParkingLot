__author__ = 'TriNguyenDang'
import math
import random
import matplotlib.pyplot as plt
from Const import *

class Location(object):
    X = None
    Y = None
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    def __getitem__(self, item):
        if(item == X):
            return self.X
        elif(item == Y):
            return self.Y
    def __setitem__(self, key ,value):
        if(key == X):
            self.X = value
        if(key == Y):
            self.Y = value
    def __str__(self):
        return "(%s,%s)"%(self.X,self.Y)
    def __repr__(self):
        return "<%s,%s>"%(self.X,self.Y)
    def __sub__(self, other):
        return math.sqrt(pow(other[X] - self[X],2) + pow(other[Y] - self[Y],2))

    def __eq__(self, other):
        return (self[X] == other[X])and(self[Y]==other[Y])

    def Draw(self,Color,Marker):
        plt.plot(self.X,self.Y,color = Color,marker = Marker)

    def Line(self,other,Color,Marker):
        plt.plot([self.X,other.X],[self.Y,other.Y],color =Color,marker = Marker)

    @staticmethod
    def InitDestination():
        return Location(60*random.choice([-1,1]),60*random.choice([-1,1]))

    @staticmethod
    def InitLocation():
        return Location(random.randint(1,100)*random.choice([-1,1]),random.randint(1,100)*random.choice([-1,1]))


