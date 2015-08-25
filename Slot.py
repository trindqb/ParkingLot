__author__ = 'TriNguyenDang'
from Const import *
class Slot(object):
    ID = None
    Fee = None
    State = None
    ListPrefer = None
    Matched = None
    Cost = None
    def __init__(self,List):
        self.ID = List[0]
        self.Fee = List[1]
        self.State = List[2]
        self.ListPrefer = List[3]
        self.Matched = List[4]
        self.Cost = List[5]
    def __getitem__(self, item):
        if(item == ID):
            return self.ID
        elif(item == F):
            return self.Fee
        elif(item == S):
            return self.State
        elif(item == P):
            return self.ListPrefer
        elif(item == M):
            return self.Matched
        elif(item == C):
            return self.Cost
    def __setitem__(self, key, value):
        if(key == ID):
            self.ID = value
        elif(key == F):
            self.Fee = value
        elif(key == S):
            self.State = value
        elif(key == P):
            self.ListPrefer = value
        elif(key == C):
            self.Cost = value
        elif(key == M):
            self.Matched = value
    '''
    def CalculatePrefer(self,ListVehicle):
        tmp = ManagerPrefer()
        for subVehicle in ListVehicle:
            tmpLocation = subVehicle['ID']
            tmpCost = self['Fee']*subVehicle['ParkingTime']
            tmp.add(Prefer(tmpLocation,tmpCost))
        ManagerPrefer.QuickSort2(tmp.ListPrefer)
        self['ListPrefer'] = tmp
    '''

    def __str__(self):
        return "ID: %s,Fee: %s,State: %s,LP:%s"%(self.ID,self.Fee,self.State,self.ListPrefer)
    def __repr__(self):
        return "<ID: %s,Fee: %s,State: %s,LP:%s>\n"%(self.ID,self.Fee,self.State,self.ListPrefer)

    pass