__author__ = 'TriNguyenDang'
from Vehicle import *

class ManagerVehicle(object):
    ListVehicle = None
    Destination = None
    def __init__(self,Data):
        self.Destination = Data[0]
        self.ListVehicle = Data[1]

    def __getitem__(self, item):
        if(item == D):
            return self.Destination
        elif(item == 'LV'):
            return self.ListVehicle
    def __setitem__(self, key, value):
        if(key == D):
            self.Destination = value
        elif(key == 'LV'):
            self.ListVehicle = value

