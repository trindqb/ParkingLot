__author__ = 'TriNguyenDang'
import Location
import random
import math
import matplotlib.pyplot as plt

CONST_SUB_FEE = 1.7
CONST_INF_FEE = 2.9
CONST_COST_DRIVING=0.31
CONST_COST_WALKING=0.1
CONST_COLUMN = 10
CONST_ROW = 10
DES = [[-60,-60],[60,-60],[60,60],[-60,60]]
DA = Location(DES[0][0],DES[0][1])
DB = Location(DES[1][0],DES[1][1])
DC = Location(DES[2][0],DES[2][1])
DD = Location(DES[3][0],DES[3][1])