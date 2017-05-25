#!usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import numpy
import model_fit

#读取原始文件  获得需要预测的酒店列表
def read_hotel_need_predict():
    list1 = []
    with open('../data/HtlPredList_new.csv', 'r') as csvfile:
        data1 = csv.reader(csvfile)
        for hotelid in data1:
            hotelid = hotelid[0]
            if hotelid != 'hotelid':
                list1.append(hotelid)
    return list1


def read_known_intersection_id( file, list_lost_some_data):
    list1 = []
    if not os.path.exists( 'each_hotel_fill0/' + file+ '.csv'):

        #list_lost_some_data.add(file)
        return
    f = open('each_hotel_fill0/' + file+ '.csv')
    for eachline in f:
        list1.append(int(float(eachline.strip('\r').strip('\n').split(',')[1])))
    if list1.__contains__(''):
        list1.remove('')
    return list1



def get_data(hotelid,start_day,inter):

    lost_hotel_list = []

    list_need_to_predict = [hotelid]
    list_lost_some_data = set()
    holiday_list = [0,1,21,22,23,47,48,49,50,51,52,53,92,93,94,120,121,170,171,245,246,273,274,275,276,277,278,358,359,364,365,366]
    all_data = {}
    train_data = []
    test_data = []
    data_mid = []
    train_y_final = []
    train_x_final = []
    train_id_y_final = []
    train_id_x_final = []
    for hotelid in list_need_to_predict:
        week_data = {}
        for i in range(0,7):
            week_data[i] = []
        if hotelid not in lost_hotel_list:
            data_mid = read_known_intersection_id(hotelid,list_lost_some_data)
        if data_mid == []:
            continue
        for i in range(0,len(data_mid)):
            if i not in holiday_list:
                week_data[i%7].append(data_mid[i])
        for i in range(0,len(data_mid)):
            if i in holiday_list:
                data_mid[i] = numpy.mean(numpy.array(week_data[i%7]))
        #all_data[hotelid] = data_mid


        for i in range(start_day,365+31-7,inter):
            train_y = data_mid[i:i+7]
            train_x = data_mid[i-7:i]
            train_x_final.append(train_x)
            train_y_final.append(train_y)
            train_id_y_final.append(range(i,i+7))
            train_id_x_final.append(range(i-7,i))

    return [train_x_final]+[train_id_x_final],[train_y_final]+[train_id_y_final]


def CalDis(train_x_final,train_y_final,Param):
    Param_1 = Param[0:7]
    Param_2 = Param[7:14]
    Param_3 = Param[14:14+31]
    Param_3 = numpy.zeros(31)
    return model_fit.model_function(train_x_final,train_y_final,Param_1,Param_2,Param_3)





def get_train_data(hotelid):
    lost_hotel_list = []
    #读取所有文件记录
    info_dict = {}
    f_info = file('../data/hotelstaticinfo_comp.csv')
    f_info_lines = csv.reader(f_info)
    for line in f_info_lines:
        info_dict[line[0]] = line[1]
    list_need_to_train = info_dict.keys()
    #list_need_to_predict = read_hotel_need_predict()
    list_need_to_predict = [hotelid]
    list_lost_some_data = set()
    holiday_list = [0,1,21,22,23,47,48,49,50,51,52,53,92,93,94,120,121,170,171,245,246,273,274,275,276,277,278,358,359,364]
    all_data = {}
    train_data = []
    test_data = []
    data_mid = []
    train_x = []
    for hotelid in list_need_to_predict:
        week_data = {}
        for i in range(0,7):
            week_data[i] = []
        if hotelid not in lost_hotel_list:
            data_mid = read_known_intersection_id(hotelid,list_lost_some_data)
        if data_mid == []:
            continue
        for i in range(0,len(data_mid)):
            if i not in holiday_list:
                week_data[i%7].append(data_mid[i])
        for i in range(0,len(data_mid)):
            if i in holiday_list:
                data_mid[i] = numpy.mean(numpy.array(week_data[i%7]))
        i = 365+31
        train_x = data_mid[i-21:i]
    return train_x

def predict(train_x,Param):
    Param_1 = Param[0:7]
    Param_2 = Param[7:14]
    Param_3 = Param[14:]
    Param_3 = numpy.zeros(31)
    return model_fit.model_predict(train_x,Param_1,Param_2,Param_3)

def predict_fit(train_x,Param):
    Param_1 = Param[0]
    Param_2 = Param[1]
    return model_fit.model_predict_fit(train_x,Param_1,Param_2)

###### AR

def get_data_AR(hotelid,start_day,inter):

    list_need_to_predict = [hotelid]
    list_lost_some_data = set()
    holiday_list = [0,1,21,22,23,47,48,49,50,51,52,53,92,93,94,120,121,170,171,245,246,273,274,275,276,277,278,358,359,364,365,366]
    all_data = {}
    train_data = []
    test_data = []
    data_mid = []
    train_y_final = []
    train_x_final = []
    train_id_y_final = []
    train_id_x_final = []
    for hotelid in list_need_to_predict:
        week_data = {}
        for i in range(0,7):
            week_data[i] = []
        if hotelid not in lost_hotel_list:
            data_mid = read_known_intersection_id(hotelid,list_lost_some_data)
        if data_mid == []:
            continue
        for i in range(0,len(data_mid)):
            if i not in holiday_list:
                week_data[i%7].append(data_mid[i])
        for i in range(0,len(data_mid)):
            if i in holiday_list:
                data_mid[i] = numpy.mean(numpy.array(week_data[i%7]))
        #all_data[hotelid] = data_mid

        for i in range(start_day,365+31-28,inter):
            train_y = data_mid[i:i+28]
            train_x = data_mid[i-21:i]
            train_x_final.append(train_x)
            train_y_final.append(train_y)
            train_id_y_final.append(range(i,i+28))
            train_id_x_final.append(range(i-21,i))

    return [train_x_final]+[train_id_x_final],[train_y_final]+[train_id_y_final]

def predict_fit_AR(train_x,Param):
    Param_1 = Param[0]
    return model_fit.model_predict_fit_AR(train_x,Param_1)


#Spring

def get_data_spring(hotelid):
    list_lost_some_data = []
    data_mid = read_known_intersection_id(hotelid,list_lost_some_data)
    if data_mid == None:
        return [],[],[],[],[],[],[],[],[],[],[]
    train_x_pre = data_mid[365]+data_mid[366]
    train_x = data_mid[1]+data_mid[0]
    sum_train = []
    sum_pre = []
    sum_week_train =[]
    sum_week_pre =[]
    for i in range(48-7-21,48-7):
        if (i+4)%7 <> 5 and (i+4)%7 <> 6:
            sum_train.append(data_mid[i])
    basevalue_train = numpy.mean(sum_train)

    for i in range(48-7-21,48-7):
        if (i+4)%7 == 5 or (i+4)%7 == 6:
            sum_week_train.append(data_mid[i])
    basevalue_week = numpy.sum(sum_week_train)

    for i in range(365+31-21,365+31):
        if (i+4)%7 <> 5 and (i+4)%7 <> 6 :
            sum_pre.append(data_mid[i])
    basevalue_pre = numpy.mean(sum_pre)

    for i in range(365+31-21,365+31):
        if (i+4)%7 == 5 or (i+4)%7 == 6 :
            sum_week_pre.append(data_mid[i])
    basevalue_week_pre = numpy.sum(sum_week_pre)

    y_0 = data_mid[47]
    y_1 = data_mid[48]
    y_2 = data_mid[49]
    y_3 = data_mid[50]
    y_4 = data_mid[51]
    y_5 = data_mid[52]
    y_6 = data_mid[53]
    y_7 = data_mid[54]
    return train_x,basevalue_train,basevalue_week,y_0,y_1,y_2,y_3,y_4,y_5,y_6,y_7,train_x_pre,basevalue_pre,basevalue_week_pre





def predict_fit_spring(train_x,Param):
    Param_1 = Param[0]
    return model_fit.model_predict_fit_AR(train_x,Param_1)



