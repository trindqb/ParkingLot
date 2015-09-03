__author__ = 'TriNguyenDang'
from ParkingLot import *
from ManagerVehicle import *
import numpy as np
import matplotlib.pyplot as plt

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
        x = np.arange(0,len(Data))
        plt.plot(x,Data,color = Corlor,marker = Marker, label = Label)



M = Main(1000,1000,1000,1000)
M.Processing()
DT = M.getData()
#Ascending(DT)
M.Draw(DT,'b','o','PLA')
avg = sum(DT)/len(DT)
y = []
x = np.arange(0,len(DT))
for i in x:
    y.append(avg)
plt.plot(x,y,'r-',label = 'AVG')
#M.Draw(DT[1],'r','o','PLB')
#M.Draw(DT[2],'g','o','PLC')
#M.Draw(DT[3],'y','o','PLD')

plt.legend(loc = 0)
plt.grid(True)
plt.show()
