import csv
import timeSeries
import model_fit
import numpy
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





f = file("../../part3_final/result/result_final.csv","ab+")
write_f = csv.writer(f)

f_No1 = file('../../part3_final/result/fit_spring.csv')
f_No1_lines = csv.reader(f_No1)
for line in f_No1_lines:
    if line[0] == "hotelid":
        continue
    train_x,train_y = timeSeries.get_data(line[0],7,1)
    if len(train_y[1])<3:
        continue
    Param = model_fit.get_Param_7(train_x,train_y)
    #result = timeSeries.predict_fit(train_data,Param)[0:30]
    result = []

    for i in range(365+31,365+31+29):
        result.append(Param[(i+4)%7][0][0]*float(line[1])+Param[(i+4)%7][0][1])
    result[5:14] = line[6:15]
    result_end =  (numpy.array(result,dtype = 'float')/3+numpy.array(line[1:],dtype = 'float')/3*2).tolist()
    result_end[4] = result_end[3]
    write_f.writerow([line[0]]+result_end)

f.close()