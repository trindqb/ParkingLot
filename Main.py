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

VB = ManagerVehicle(ManagerVehicle.InitData(100,'B'))
for subVB in VB['LV']:
    subVB.CalculatePrefer(PLB,subVB[D])

VC = ManagerVehicle(ManagerVehicle.InitData(100,'C'))
for subVC in VC['LV']:
    subVC.CalculatePrefer(PLC,subVC[D])

VD = ManagerVehicle(ManagerVehicle.InitData(100,'D'))
for subVD in VD['LV']:
    subVD.CalculatePrefer(PLD,subVD[D])

VA.Acceptation()
for subVA in VA['LV']:
    print subVA