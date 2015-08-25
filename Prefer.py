__author__ = 'TriNguyenDang'
class Prefer(object):
    ID = None
    Cost = None
    def __init__(self,ID,Cost):
        self.ID = ID
        self.Cost = Cost
    def __getitem__(self, item):
        if(item == 'ID'):
            return self.ID
        elif(item == 'Cost'):
            return self.Cost
    def __setitem__(self, key, value):
        if(key == 'ID'):
            self.ID = value
        elif(key == 'Cost'):
            self.Cost =value
    def __lt__(self, other):
        return self.Cost < other.Cost

    def __gt__(self, other):
        return self.Cost > other.Cost

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return "%s,%s"%(self.ID,self.Cost)
    def __repr__(self):
        return "<%s,%s>"%(self.ID,self.Cost)

    def __le__(self, other):
        return self.Cost <= other.Cost

    def __ge__(self, other):
        return self.Cost >= other.Cost


    pass