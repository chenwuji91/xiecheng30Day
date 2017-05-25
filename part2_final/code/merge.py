#!usr/bin/python#coding=utf-8
import csv
import timeSeries
import numpy




data1 = []

f_No1 = file('intermediate_result/base_data.csv')
f_No1_lines = csv.reader(f_No1)
for line in f_No1_lines:
    data1.append(line)




data2 = []
f_No2 = file('intermediate_result/spring_days.csv')
f_No2_lines = csv.reader(f_No2)
for line in f_No2_lines:
    data2.append(line)

for i in range(0,len(data1)):
	data1[i][6:6+8] = data2[i][1:]


f = file("intermediate_result/part2result.csv","ab+")
write_f = csv.writer(f)
write_f.writerows(data1)