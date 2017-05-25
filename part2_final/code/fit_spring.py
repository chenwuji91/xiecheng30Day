#!usr/bin/python#coding=utf-8
import csv
import timeSeries
import model_fit
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
    sum = y_1_mid + y_2_mid + y_3_mid + y_4_mid + y_5_mid + y_6_mid + y_7_mid
    if sum <> 0:
        y_1.append(float(y_1_mid)/float(sum))
        y_2.append(float(y_2_mid)/float(sum))
        y_3.append(float(y_3_mid)/float(sum))
        y_4.append(float(y_4_mid)/float(sum))
        y_5.append(float(y_5_mid)/float(sum))
        y_6.append(float(y_6_mid)/float(sum))
        y_7.append(float(y_7_mid)/float(sum))


y_1_mean = numpy.mean(y_1)
y_2_mean = numpy.mean(y_2)
y_3_mean = numpy.mean(y_3)
y_4_mean = numpy.mean(y_4)
y_5_mean = numpy.mean(y_5)
y_6_mean = numpy.mean(y_6)
y_7_mean = numpy.mean(y_7)


f = file("../../part3_final/result/fit_spring.csv","ab+")
write_f = csv.writer(f)


f_No1 = file('../../part3_final/result/part3_base.csv')
f_No1_lines = csv.reader(f_No1)
for line in f_No1_lines:
    if line[0] == "hotelid":
        continue
    sum_num = numpy.sum(numpy.array(line[7:7+7],dtype='float'))
    week_1 = float(sum_num)*float(y_1_mean)
    week_2 = float(sum_num)*float(y_2_mean)
    week_3 = float(sum_num)*float(y_3_mean)
    week_4 = float(sum_num)*float(y_4_mean)
    week_5 = float(sum_num)*float(y_5_mean)
    week_6 = float(sum_num)*float(y_6_mean)
    week_7 = float(sum_num)*float(y_7_mean)
    write_f.writerow(line[0:7]+
            [float(line[7])/3*2+week_1/3]+
            [float(line[8])/3*2+week_2/3]+
            [float(line[9])/3*2+week_3/3]+
            [float(line[10])/3*2+week_4/3]+
            [float(line[11])/3*2+week_5/3]+
            [float(line[12])/3*2+week_6/3]+
            [float(line[13])/3*2+week_7/3]+
            line[14:])

f.close()