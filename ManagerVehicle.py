__author__ = 'TriNguyenDang'
from Vehicle import *

class ManagerVehicle(object):
    ListVehicle = None
    NumVehicle = None
    def __init__(self,Data):
        self.NumVehicle = Data[0]
        self.ListVehicle = Data[1]

    def __getitem__(self, item):
        if(item == 'NV'):
            return self.NumVehicle
        elif(item == 'LV'):
            return self.ListVehicle
    def __setitem__(self, key, value):
        if(key == 'NV'):
            self.NumVehicle = value
        elif(key == 'LV'):
            self.ListVehicle = value
    @staticmethod
    def InitData(NumVehicle,Type):
        tmp = []
        for x in range(NumVehicle):
            tmp.append(Vehicle(Vehicle.InitVehicle(Type)))
        return NumVehicle,tmp

