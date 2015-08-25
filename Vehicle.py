__author__ = 'TriNguyenDang'
import matplotlib.pyplot as plt
import numpy as np
from ManagerPrefer import *
import Prefer
from Location import *
import random
from Const import *



class Vehicle:
    ID = None
    Destination = None
    ParkingTime = None
    ListPrefer = None
    Matched = None
    Cost = None
    def __init__(self,Lists):
        self.ID = Lists[0]
        self.Destination = Lists[1]
        self.ParkingTime = Lists[2]
        self.ListPrefer = Lists[3]
        self.Matched = Lists[4]
        self.Cost = Lists[5]

    #randomize data using Poison distribution
    @staticmethod
    def InitVehicle():
        X = 1
        Y = 1
        while(-LOW_BOUND<=X)and(X<=LOW_BOUND)and(-SUP_BOUND<=Y)and(Y<=SUP_BOUND):
            X = random.randint(1,100)*random.choice([-1,1])
            Y = random.randint(1,100)*random.choice([-1,1])
        ID = Location( X,Y )
        XYD = random.choice([0,1,2,3])
        #print XYD
        Des = Location(0,0)
        T = round(random.uniform(0.13,2.0),2)
        LP = ManagerPrefer()
        #LP.add(Prefer(Location(0,0),1.2))
        M = Location(0,0)
        Cost = 0
        return ID,Des,T,LP,M,Cost
    def __str__(self):
        return "ID: %s,Des: %s,Time: %s,Pre: %s,M:%s,C:%s"%(self.ID,self.Destination,self.ParkingTime,self.ListPrefer,self.Matched,self.Cost)

    def __repr__(self):
        return "\n<ID: %s,Des: %s,Time: %s,Pre: %s,M:%s,C:%s>\n"%(self.ID,self.Destination,self.ParkingTime,self.ListPrefer,self.Matched,self.Cost)

    def __getitem__(self, item):
        if(item == ID):
            return self.ID
        elif(item == D):
            return self.Destination
        elif(item == P):
            return self.ParkingTime
        elif(item == M):
            return self.Matched
        elif(item == C):
            return self.Cost
        elif(item == P):
            return self.ListPrefer
    def __setitem__(self, key, value):
        if(key == ID):
            self.ID = value
        elif(key == D):
            self.Destination = value
        elif(key == P):
            self.ParkingTime = value
        elif(key == P):
            self.ListPrefer = value
        elif(key == M):
            self.Matched = value
        elif(key == C):
            self.Cost = value

    def CalculatePrefer(self,ListSlot,Destination,Type):

        tmp = ManagerPrefer()
        for subSlot in ListSlot:
            tmpLocation = subSlot['ID']
            tmpCost = subSlot['Fee']*self['ParkingTime'] + CONST_COST_DRIVING * (self['ID'] - subSlot['ID'])/10 + CONST_COST_WALKING*(Destination - subSlot['ID'])/100
            tmp.add(Prefer(tmpLocation,tmpCost))
        if(Type == 'Ascending'):
            ManagerPrefer.QuickSort(tmp.ListPrefer)
        elif(Type == 'Descending'):
            ManagerPrefer.QuickSort2(tmp.ListPrefer)
        self['ListPrefer'] = tmp

    def DrawMatched(self,Color,Marker):
        plt.plot([self['ID']['X'],self['Matched']['X']],[self['ID']['Y'],self['Matched']['Y']],color = Color,marker = Marker)

    pass
