__author__ = 'TriNguyenDang'
from Prefer import *
class ManagerPrefer(object):
    ListPrefer = None

    def __init__(self):
        self.ListPrefer = []

    def add(self,value):
        self.ListPrefer.append(value)

    def __getitem__(self, i):
        return self.ListPrefer[i]

    def getLen(self):
        return len(self.ListPrefer)

    def Delete(self,ID):
        for sub in self.ListPrefer:
            if(sub['ID']==ID):
                self.ListPrefer.remove(sub)


    def __str__(self):
        return "%s"%(self.ListPrefer)
    def __repr__(self):
        return "<%s>"%(self.ListPrefer)
