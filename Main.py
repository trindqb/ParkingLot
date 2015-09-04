__author__ = 'TriNguyenDang'
from ParkingLot import *
from ManagerVehicle import *
import numpy as np
import matplotlib.pyplot as plt
import copy
class Main(object):
    PLA = None
    PLB = None
    PLC = None
    PLD = None
    VA = None
    VB = None
    VC = None
    VD = None
    def __init__(self,numVA,numVB,numVC,numVD):

        self.PLA = Parkinglot(Parkinglot.InitData('A'))
        self.PLB = Parkinglot(Parkinglot.InitData('B'))
        self.PLC = Parkinglot(Parkinglot.InitData('C'))
        self.PLD = Parkinglot(Parkinglot.InitData('D'))
        #---------------------------------------------#
        self.VA = ManagerVehicle(ManagerVehicle.InitData(numVA,'A'))
        for subVA in self.VA['LV']:
            subVA.CalculatePrefer(self.PLA,subVA[D])

        self.VB = ManagerVehicle(ManagerVehicle.InitData(numVB,'B'))
        for subVB in self.VB['LV']:
            subVB.CalculatePrefer(self.PLB,subVB[D])

        self.VC = ManagerVehicle(ManagerVehicle.InitData(numVC,'C'))
        for subVC in self.VC['LV']:
            subVC.CalculatePrefer(self.PLC,subVC[D])

        self.VD = ManagerVehicle(ManagerVehicle.InitData(numVD,'D'))
        for subVD in self.VD['LV']:
            subVD.CalculatePrefer(self.PLD,subVD[D])

    def Processing(self):
        self.VA.Acceptation()
        self.VB.Acceptation()
        self.VC.Acceptation()
        self.VD.Acceptation()

    def MiddlePoint(self):
        self.VA.MiddlePoint()
        self.VB.MiddlePoint()
        self.VC.MiddlePoint()
        self.VD.MiddlePoint()

    def LastPoint(self):
        self.VA.LastPoint()
        self.VB.LastPoint()
        self.VC.LastPoint()
        self.VD.LastPoint()

    def getData(self):
        DataVA = []
        DataVB = []
        DataVC = []
        DataVD = []
        for subVA in self.VA['LV']:
            DataVA.append(subVA[C])
        for subVB in self.VB['LV']:
            DataVB.append(subVB[C])
        for subVC in self.VC['LV']:
            DataVC.append(subVC[C])
        for subVD in self.VD['LV']:
            DataVD.append(subVD[C])
        #Ascending(DataVA)
        #Ascending(DataVB)
        #Ascending(DataVC)
        #Ascending(DataVD)
        return DataVA+DataVB+DataVC+DataVD

    def Draw(self,Data,Corlor,Marker,Label):

        plt.plot(x,Data,color = Corlor,marker = Marker, label = Label)



M = Main(100,100,100,100)
N = copy.deepcopy(M)
L = copy.deepcopy(M)
M.Processing()
N.MiddlePoint()
L.LastPoint()
DT = M.getData()
Ascending(DT)
DT2 = N.getData()
Ascending(DT2)
DT3 = L.getData()
Ascending(DT3)
x = np.arange(0,len(DT))
M.Draw(DT,'b','o','First')
N.Draw(DT2,'g','1','Middle')
L.Draw(DT3,'r','*','Last')
avg = sum(DT)/len(DT)
y = []

for i in x:
    y.append(avg)
plt.plot(x,y,'r-',label = 'AVG')
#M.Draw(DT[1],'r','o','PLB')
#M.Draw(DT[2],'g','o','PLC')
#M.Draw(DT[3],'y','o','PLD')

plt.legend(loc = 0)
plt.grid(True)
plt.show()
