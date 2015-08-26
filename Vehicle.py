__author__ = 'TriNguyenDang'
import matplotlib.pyplot as plt
import numpy as np
from ManagerPrefer import *
import Prefer
from Location import *
import random
from Ascending import *
#from Slot import *


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
    def InitVehicle(Type):
        if(Type == 'A'):
            Destination = Location(XD,YD)
        elif(Type == 'B'):
            Destination = Location(XD,-YD)
        elif(Type == 'C'):
            Destination = Location(-XD,YD)
        elif(Type == 'D'):
            Destination = Location(-XD,-YD)
        else:
            Destination = Location.InitDestination()
        TmpA = Location.InitLocation()
        while(-LOW_BOUND<=TmpA[X])and(TmpA[X]<=LOW_BOUND)and(-SUP_BOUND<=TmpA[Y])and(TmpA[Y]<=SUP_BOUND):
            TmpA = Location.InitLocation()
        TmpT = random.uniform(CONST_SUP_TIME,CONST_INF_TIME)
        TmpP = ManagerPrefer()
        TmpM = Location(0,0)
        TmpC = 0
        return TmpA,Destination,TmpT,TmpP,TmpM,TmpC
    def __str__(self):
        return "ID: %s\t Des: %s\tTime: %s\t Pre: %s\t M:%s\t C:%s"%(self.ID,self.Destination,self.ParkingTime,self.ListPrefer,self.Matched,self.Cost)

    def __repr__(self):
        return "\n<ID: %s\t Des %s\t Time: %s\t Pre: %s\t M: %s\t C: %s>\n"%(self.ID,self.Destination,self.ParkingTime,self.ListPrefer,self.Matched,self.Cost)

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

    def CalculatePrefer(self,Parking,Destination):
        TmpP = ManagerPrefer()
        for Slot in Parking:
            TmpLocation = Slot[ID]
            TmpCost = Slot[F]*self[PT] + CONST_COST_DRIVING*(self[ID] - Slot[ID])/10 + CONST_COST_WALKING*(Slot[ID] - Destination)/10
            TmpP.add(Prefer(TmpLocation,TmpCost))
        Ascending(TmpP)
        self[P] = TmpP


    def CalculatePrefer(self,ListSlot,Destination,Type):
        tmp = ManagerPrefer()
        for subSlot in ListSlot:
            tmpLocation = subSlot[ID]
            tmpCost = subSlot[F]*self[PT] + CONST_COST_DRIVING * (self[ID] - subSlot[ID])/10 + CONST_COST_WALKING*(Destination - subSlot[ID])/10
            tmp.add(Prefer(tmpLocation,tmpCost))
        if(Type == AS):
            ManagerPrefer.QuickSort(tmp.ListPrefer)
        elif(Type == DS):
            ManagerPrefer.QuickSort2(tmp.ListPrefer)
        self[P] = tmp

    def DrawMatched(self,Color,Marker):
        plt.plot([self['ID']['X'],self['Matched']['X']],[self['ID']['Y'],self['Matched']['Y']],color = Color,marker = Marker)

    pass