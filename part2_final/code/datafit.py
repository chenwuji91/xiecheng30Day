import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as pl
import copy
import numpy

def fun(x, p):
    a, b = p
    return a*x + b

def fun_2(x, p):
    a, b ,c = p
    return a*x*x+b*x + c


def residuals(p, x, y):
    return fun(x, p) - y


def residuals_2(p, x, y):
    a = p[0]
    if a<0:
        return 10000000
    return fun_2(x, p) - y


def fitline(x1,y1):
    x1 = np.array(x1, dtype=float)
    y1 = np.array(y1, dtype=float)
    r = leastsq(residuals, [1, 1], args=(x1, y1))
    return r


def fitline_2(x1,y1):
    x1 = copy.deepcopy(x1)
    y1 = copy.deepcopy(y1)
    x1 = np.array(x1, dtype=float)
    y1 = np.array(y1, dtype=float)
    r = leastsq(residuals_2, [1, 1, 1], args=(x1, y1))
    return r

def getallData(r,start,end):
    y = []
    x = []
    for x0 in range(start,end,1):
        y0 = r[0][0]*x0+r[0][1]
        x.append(x0)
        y.append(y0)
    return x,y

def getallData_2(r,start,end):
    y = []
    x = []
    y_min = 100000
    for x0 in range(start,end,1):
        y0 = r[0][0]*x0*x0+r[0][1]*x0+r[0][2]
        if y0<y_min:
            y_min = y0
        else:
            y0 = y_min
        x.append(x0)
        y.append(y0)
    return x,y

####################ARMA

def regression(x,y):
    x1 = []
    x2 = []
    x3 = []
    for line in x[0]:
        x1.append(line)
    for line in x[1]:
        x2.append(line)
    for line in x[2]:
        x3.append(line)
    x1 = np.array(x1, dtype=float)
    x2 = np.array(x2, dtype=float)
    x3 = np.array(x3, dtype=float)
    y1 = np.array(y, dtype=float)
    r = leastsq(residuals_ar, [1,1,1,1], args=(x1,x2,x3, y1))
    return r

def residuals_ar(p, x1,x2,x3, y):
    return fun_ar(x1,x2,x3, p) - y

def fun_ar(x1,x2,x3, p):
    a = p[0:3]
    b = p[3]
    return a[0]*x1+a[1]*x2+a[2]*x3+ b

def getallData_re(r,x1,x2,x3):
    y = []
    x = []
    y0 = r[0][0]*x1+r[0][1]*x2+r[0][2]*x3+r[0][1]
    return y0




