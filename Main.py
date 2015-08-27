__author__ = 'TriNguyenDang'
from ParkingLot import *
from ManagerVehicle import *
import numpy as np
import matplotlib.pyplot as plt

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
VB.Acceptation()
VC.Acceptation()
VD.Acceptation()
DataVA = [0]
DataVB = [0]
DataVC = [0]
DataVD = [0]
for subVA in VA['LV']:
    DataVA.append(subVA[C])

for subVB in VB['LV']:
    DataVB.append(subVB[C])

for subVC in VC['LV']:
    DataVC.append(subVC[C])

for subVD in VD['LV']:
    DataVD.append(subVD[C])

Ascending(DataVA)
Ascending(DataVB)
Ascending(DataVC)
Ascending(DataVD)

x = np.arange(0,len(DataVA))
plt.plot(x,DataVA,'b1-',label = 'TypeA')
plt.plot(x,DataVB,'r2-',label = 'TypeB')
plt.plot(x,DataVC,'g*-',label = 'TypeC')
plt.plot(x,DataVD,'ko-',label = 'TypeD')
plt.legend(loc = 0)
plt.grid(True)
plt.show()