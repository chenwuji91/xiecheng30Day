#!usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import csv
from datetime import datetime
def process():
    dict1 = {}
    with open('../data/inHtl_cii_compfz.csv', 'r') as csvfile:
        data1 = csv.reader(csvfile)
        for starttime,hotelid,notcancelcii in data1:
            if starttime == 'starttime':
                continue
            starttime = (datetime.strptime(starttime, "%Y-%m-%d" ) - datetime(2015,1,1)).days
            if dict1.__contains__(hotelid):
                current_dict = dict1[hotelid]
            else:
                current_dict = {}
                dict1[hotelid] = current_dict
                for i in range(400):
                    current_dict[i] = 0
            current_dict[starttime] = notcancelcii
    pass
    return dict1



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
import tools
dict1 = process()

for each_hotel in dict1:
    hotel = dict1.get(each_hotel)

    dict_sorted = sorted(hotel.items(),key = lambda x:x[0]) #datetime.strptime(x[0], "%Y/%m/%d")
    dict1[each_hotel] = dict_sorted
    data = []
    for eachs in dict_sorted:
        data.append(str(eachs[0]) + ',' + str(eachs[1])+'\n')
    tools.makeDir('intermediate_result/')
    tools.makeDir('each_hotel_fill0/')
    tools.writeToFile('each_hotel_fill0/'+ each_hotel +'.csv', data)




