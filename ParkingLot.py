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
        Xaxis = Own[X]/60
        Yaxis = Own[Y]/60
        TmpS = []
        for x in range(1,LOW_BOUND):
            for y in range(1,SUP_BOUND):
                TmpS.append(Slot([Location(x*Xaxis,y*Yaxis),random.uniform(CONST_SUP_FEE,CONST_INF_FEE),True,ManagerPrefer(),Location(0,0),0]))

        return TmpS,Own
PA = Parkinglot(Parkinglot.InitData('D'))
print PA['SlotList']