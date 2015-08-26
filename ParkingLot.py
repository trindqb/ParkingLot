__author__ = 'TriNguyenDang'
from  Slot import *
from Location import  *
from ManagerPrefer import *

class Parkinglot(object):
    SlotList = None
    Owned = None
    def __init__(self,Data):
        self.SlotList = []
        self.SlotList = Data[0]
        self.Owned = Data[1]

    def __getitem__(self, item):
        if(item == 'SlotList'):
            return self.SlotList
        elif(item == O):
            return self.Owned
    def __setitem__(self, key, value):
        if(key == 'SlotList'):
            self.SlotList = value
        elif(key == O):
            self.Owned = value
    def __str__(self):
        return "Des:\n %s\nList:\n %s"%(self.Owned,self.SlotList)
    def __repr__(self):
        return "<Des: %s, List: %s>"%(self.Owned,self.SlotList)
    @staticmethod
    def InitData(Type):
        if(Type == 'A'):
            Own = Location(XD,YD)
        elif(Type == 'B'):
            Own = Location(XD,-YD)
        elif(Type == 'C'):
            Own = Location(-XD,YD)
        elif(Type == 'D'):
            Own = Location(-XD,-YD)
        else:
            Own = Location.InitDestination()
        Xaxis = Own[X]/XD
        Yaxis = Own[Y]/YD
        TmpS = []
        for x in range(1,LOW_BOUND):
            for y in range(1,SUP_BOUND):
                TmpS.append(Slot([Location(x*Xaxis,y*Yaxis),random.uniform(CONST_SUP_FEE,CONST_INF_FEE),True,ManagerPrefer(),Location(0,0),0]))
        return TmpS,Own
