__author__ = 'TriNguyenDang'
from ParkingLot import *
from ManagerVehicle import *

ListVehicle = []
PLA = Parkinglot(Parkinglot.InitData('A'))
PLB = Parkinglot(Parkinglot.InitData('B'))
PLC = Parkinglot(Parkinglot.InitData('C'))
PLD = Parkinglot(Parkinglot.InitData('D'))
VA = ManagerVehicle(ManagerVehicle.InitData(100,'A'))
for subVA in VA['LV']:
    subVA.CalculatePrefer(PLA,subVA[D])

for subVA in VA['LV']:
    print subVA