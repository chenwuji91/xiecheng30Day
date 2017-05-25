#!usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import datafit

def judge_func(data_y):
    list_delta = []
    for line in data_y:
        predict_value = float(line[0])
        real_value = float(line[1])
        list_delta.append(abs(real_value - predict_value))
    return  np.mean(np.array(list_delta))
import numpy
def model_function(data_x,data_y,Param_1,Param_2,Param_3):
    error_sum = 0

    for k in range(0,len(data_y[1])):
        result = []

        sum = []
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 <> 5 and (data_y[1][k][i]+4)%7+4 <> 6:
                sum.append(float(data_y[0][k][i]))
        basevalue = numpy.mean(sum)

        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 5 or (data_y[1][k][i]+4)%7 == 6:
                result.append([Param_1[data_y[1][k][i]%7]*basevalue+Param_2[data_y[1][k][i]%7]+Param_3[i],data_y[0][k][i]])

        error_sum = error_sum + (float(data_y[1][k][0])/float(365))*float(judge_func(result))
    return error_sum


def get_Param(data_x,data_y):
    error_sum = 0
    train_x_1 = []
    train_x_2 = []
    train_y_1 = []
    train_y_2 = []
    for k in range(0,len(data_y[1])):
        result = []

        sum = []
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 <> 5 and (data_y[1][k][i]+4)%7+4 <> 6:
                sum.append(float(data_y[0][k][i]))
        basevalue = numpy.mean(sum)

        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 5 :
                train_x_1.append(basevalue)
                train_y_1.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 6:
                train_x_2.append(basevalue)
                train_y_2.append(data_y[0][k][i])
    Param_1 = datafit.fitline(train_x_1,train_y_1)
    Param_2 = datafit.fitline(train_x_2,train_y_2)
    return Param_1,Param_2


def fit(data_x,Param):
    data = []
    for line in data_x:
        data.append(datafit.getallData(Param,line)[0])
    return data

def model_predict(data_x,Param_1,Param_2):
    sum = []
    for i in range(0,21):
        if (365+31-21+i+4)%7 <> 5 and (365+31-21+i+4)%7 <> 6: # and (365-21+i) <> 364-7:
            #print 'date',365+31-21+i,float(data_x[i])
            sum.append(float(data_x[i]))
    basevalue = numpy.mean(sum)
    result = []
    for i in range(365+31,365+31+31):
        if (i+4)%7 <> 5 and (i+4)%7 <> 6:
            result.append(basevalue)
        else:
            result.append(Param_1[i%7]*basevalue+Param_2[i%7])
    return result

def model_predict_fit(data_x,Param_1,Param_2):
    sum = []
    for i in range(0,21):
        if (365+31-21+i+4)%7 <> 5 and (365+31-21+i+4)%7 <> 6: # and (365-21+i) <> 364-7:
            sum.append(float(data_x[i]))
    basevalue = numpy.mean(sum)
    result = []

    for i in range(365+31,365+31+31):
        if (i+4)%7 <> 5 and (i+4)%7 <> 6:
            result.append(basevalue)
        elif (i+4)%7 <> 6:
            result.append(Param_1[0][0]*basevalue+Param_1[0][1])
        else:
            result.append(Param_2[0][0]*basevalue+Param_2[0][1])
    return result,basevalue

def judge_true(data_1,data_2,data_3):
    list_delta = []

    for i in range(0,29):
        predict_value = float(data_2[365+31+i])
        real_value = float(data_3[365+31+i])
        list_delta.append(abs(real_value - predict_value))
    data_result_3 =  np.sum(np.array(list_delta))
    return data_result_3


###############时间窗口  ARMA拟合


def get_Param_AR(data_x,data_y):
    train_x_1 = []
    train_y_1 = []
    for k in range(0,len(data_y[1])):

        sum_1 = []
        sum_2 = []
        sum_3 = []
        sum_4 = []
        for i in range(0,7):
            if (data_x[1][k][i]+4)%7 <> 5 and (data_x[1][k][i]+4)%7+4 <> 6:
                sum_1.append(float(data_x[0][k][i]))
        for i in range(7,14):
            if (data_x[1][k][i]+4)%7 <> 5 and (data_x[1][k][i]+4)%7+4 <> 6:
                sum_2.append(float(data_x[0][k][i]))
        for i in range(14,21):
            if (data_x[1][k][i]+4)%7 <> 5 and (data_x[1][k][i]+4)%7+4 <> 6:
                sum_3.append(float(data_x[0][k][i]))
        basevalue_1 = numpy.mean(sum_1)
        basevalue_2 = numpy.mean(sum_2)
        basevalue_3 = numpy.mean(sum_3)
        train_x_1.append([basevalue_1,basevalue_2,basevalue_3])


        for i in range(0,28):
            if (data_y[1][k][i]+4)%7 <> 5 and (data_y[1][k][i]+4)%7+4 <> 6:
                sum_4.append(float(data_y[0][k][i]))
        y_value = numpy.mean(sum_4)
        train_y_1.append(y_value)

    Param = datafit.regression(train_x_1,train_y_1)

    return Param

def model_predict_fit_AR(data_x,Param_1):

    sum_1 = []
    sum_2 = []
    sum_3 = []
    for i in range(0,7):
        if (365+31-21+i+4)%7 <> 5 and (365+31-21+i+4)%7 <> 6: # and (365-21+i) <> 364-7:
            sum_1.append(float(data_x[i]))
    for i in range(7,14):
        if (365+31-21+i+4)%7 <> 5 and (365+31-21+i+4)%7 <> 6: # and (365-21+i) <> 364-7:
            sum_2.append(float(data_x[i]))
    for i in range(14,21):
        if (365+31-21+i+4)%7 <> 5 and (365+31-21+i+4)%7 <> 6: # and (365-21+i) <> 364-7:
            sum_3.append(float(data_x[i]))
    basevalue_1 = numpy.mean(sum_1)
    basevalue_2 = numpy.mean(sum_2)
    basevalue_3 = numpy.mean(sum_3)

    result = []

    basevalue = Param_1[0]*basevalue_1+Param_1[1]*basevalue_2+Param_1[2]*basevalue_3+Param_1[3]
    for i in range(365+31,365+31+31):
        result.append(basevalue)
    return result



#####seven days


def get_Param_7(data_x,data_y):
    error_sum = 0
    train_x_1 = []
    train_x_2 = []
    train_x_3 = []
    train_x_4 = []
    train_x_5 = []
    train_x_6 = []
    train_x_0 = []

    train_y_1 = []
    train_y_2 = []
    train_y_3 = []
    train_y_4 = []
    train_y_5 = []
    train_y_6 = []
    train_y_0 = []
    for k in range(0,len(data_y[1])):
        result = []

        sum = []
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 <> 5 and (data_y[1][k][i]+4)%7+4 <> 6:
                sum.append(float(data_y[0][k][i]))
        basevalue = numpy.mean(sum)
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 0 :
                train_x_0.append(basevalue)
                train_y_0.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 1:
                train_x_1.append(basevalue)
                train_y_1.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 2 :
                train_x_2.append(basevalue)
                train_y_2.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 3:
                train_x_3.append(basevalue)
                train_y_3.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 4:
                train_x_4.append(basevalue)
                train_y_4.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 5 :
                train_x_5.append(basevalue)
                train_y_5.append(data_y[0][k][i])
        for i in range(0,7):
            if (data_y[1][k][i]+4)%7 == 6:
                train_x_6.append(basevalue)
                train_y_6.append(data_y[0][k][i])
    Param_1 = datafit.fitline(train_x_1,train_y_1)
    Param_2 = datafit.fitline(train_x_2,train_y_2)
    Param_3 = datafit.fitline(train_x_3,train_y_3)
    Param_4 = datafit.fitline(train_x_4,train_y_4)
    Param_5 = datafit.fitline(train_x_5,train_y_5)
    Param_6 = datafit.fitline(train_x_6,train_y_6)
    Param_0 = datafit.fitline(train_x_0,train_y_0)
    return Param_0,Param_1,Param_2,Param_3,Param_4,Param_5,Param_6