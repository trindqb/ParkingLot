__author__ = 'TriNguyenDang'
def Descending(List):
    QuickSortPartition(List,0,len(List)-1)
def Partition(List,First,Last):
    Pivot = List[First] #Key
    Left = First + 1
    Right = Last
    Done = False
    while not(Done):
        while(Left <= Right)and(List[Left] >= Pivot):
            Left+=1
        while (List[Right] <= Pivot)and(Right>=Left):
            Right-=1
        if(Right<Left):
            Done =True
        else:
            Ltmp = List[Left]
            List[Left] = List[Right]
            List[Right] = Ltmp
    Ftmp = List[First]
    List[First] = List[Right]
    List[Right] = Ftmp
    return Right
def QuickSortPartition(List,First,Last):
    if(First<Last):
        MidlePoint = Partition(List,First,Last)
        QuickSortPartition(List,First,MidlePoint-1)
        QuickSortPartition(List,MidlePoint+1,Last)