import csv
import timeSeries
import model_fit

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


result = []

for hotelid in list_need_to_predict:

    train_x,train_y = timeSeries.get_data(hotelid,7,1)
    if len(train_y[1])<3:
        print hotelid
        continue
    Param = model_fit.get_Param(train_x,train_y)
    train_data = timeSeries.get_train_data(hotelid)

    if len(train_data)<3:
        print hotelid
        continue
    result.append([hotelid]+timeSeries.predict_fit(train_data,Param)[0][0:29])

f = file("intermediate_result/base_data.csv","ab+")
write_f = csv.writer(f)
write_f.writerows(result)
f.close()