#!usr/bin/python#coding=utf-8
import csv
import timeSeries
import numpy


f_region = file('../data/hotelstaticinfo_comp.csv')
f_region_lines = csv.reader(f_region)
region_dict = {}
regions = {}
for line in f_region_lines:
    region_dict[line[0]] = line[1]
    regions[line[1]] = []

def read_hotel_need_predict():
    list1 = []
    with open('../data/HtlPredList_new.csv', 'r') as csvfile:
        data1 = csv.reader(csvfile)
        for hotelid in data1:
            hotelid = hotelid[0]
            if hotelid != 'hotelid':
                list1.append(hotelid)
    return list1
list_need_to_predict = read_hotel_need_predict()

train_x = []
train_x_pre = []
train_x_avg = []
train_x_avg_pre = []
train_x_week = []
train_x_week_pre = []
y_0 = []
y_1 = []
y_2 = []
y_3 = []
y_4 = []
y_5 = []
y_6 = []
y_7 = []


###生成验证集
for hotelid in list_need_to_predict:
    hotelid = str(hotelid)
    train_x_mid,train_x_avg_mid,train_x_week_mid,y_0_mid,y_1_mid,y_2_mid,y_3_mid,y_4_mid,y_5_mid,y_6_mid,y_7_mid,train_x_pre_mid,train_x_avg_pre_mid,train_x_week_pre_mid = timeSeries.get_data_spring(hotelid)
    
    if train_x_mid <> 0 and train_x_avg_mid <> 0 :
        train_x.append(train_x_mid)
        train_x_avg.append(train_x_avg_mid)
        train_x_week.append(train_x_week_mid)
        y_0.append(y_0_mid)
        y_1.append(y_1_mid)
        y_2.append(y_2_mid)
        y_3.append(y_3_mid)
        y_4.append(y_4_mid)
        y_5.append(y_5_mid)
        y_6.append(y_6_mid)
        y_7.append(y_7_mid)

    train_x_week_pre.append(train_x_week_pre_mid)
    train_x_pre.append(train_x_pre_mid)
    train_x_avg_pre.append(train_x_avg_pre_mid)


import datafit
r_0 = datafit.regression([train_x,train_x_avg,train_x_week],y_0)
r_1 = datafit.regression([train_x,train_x_avg,train_x_week],y_1)
r_2 = datafit.regression([train_x,train_x_avg,train_x_week],y_2)
r_3 = datafit.regression([train_x,train_x_avg,train_x_week],y_3)
r_4 = datafit.regression([train_x,train_x_avg,train_x_week],y_4)
r_5 = datafit.regression([train_x,train_x_avg,train_x_week],y_5)
r_6 = datafit.regression([train_x,train_x_avg,train_x_week],y_6)
r_7 = datafit.regression([train_x,train_x_avg,train_x_week],y_7)
for i in range(0,len(list_need_to_predict)):
    pre_0 = datafit.getallData_re(r_0,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_1 = datafit.getallData_re(r_1,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_2 = datafit.getallData_re(r_2,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_3 = datafit.getallData_re(r_3,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_4 = datafit.getallData_re(r_4,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_5 = datafit.getallData_re(r_5,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_6 = datafit.getallData_re(r_6,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])
    pre_7 = datafit.getallData_re(r_7,train_x_pre[i],train_x_avg_pre[i],train_x_week_pre[i])

    f = file("intermediate_result/spring_days.csv","ab+")
    write_f = csv.writer(f)
    write_f.writerow([list_need_to_predict[i]]+[pre_0,pre_1,pre_2,pre_3,pre_4,pre_5,pre_6,pre_7])
    f.close()
