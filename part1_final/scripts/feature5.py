import sys
import datetime
import numpy as np
start = datetime.datetime.strptime("20150101","%Y%m%d")
def getday(time):
    return (datetime.datetime.strptime(time,"%Y-%m-%d") - start).days
def getweekday(time):
    delt = datetime.timedelta(days=time)
    day = start + delt
    return day.weekday()

def getData(inputfile):
    hotel_cii = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            hotel_cii.setdefault(data[1],[0]*396)
            hotel_cii[data[1]][getday(data[0])] = float(data[2])
    return hotel_cii

def gethtl_train(hotel_cii,hotelid):
    sum4 = list()
    sum5 = list()
    sum6 = list()
    sum7 = list()
    s4 = list()
    s5 = list()
    s6 = list()
    s7 = list()
    if hotelid in hotel_cii:
        for i in xrange(getday("2015-01-03"),getday("2015-02-01")):
            if(getweekday(i)+1 == 5):
                sum5.append(hotel_cii[hotelid][i])
            elif(getweekday(i)+1 == 6):
                sum6.append(hotel_cii[hotelid][i])
            elif(getweekday(i)+1 == 7):
                sum7.append(hotel_cii[hotelid][i])
            else:
                sum4.append(hotel_cii[hotelid][i])
    s1 = sum(hotel_cii[hotelid][0:2])
    for i in xrange(getday("2015-02-18")-8-21,getday("2015-02-18")-8):
        if(getweekday(i)+1 == 5):
            s5.append(hotel_cii[hotelid][i])
        elif(getweekday(i)+1 == 6):
            s6.append(hotel_cii[hotelid][i])
        elif(getweekday(i)+1 == 7):
            s7.append(hotel_cii[hotelid][i])
        else:
            s4.append(hotel_cii[hotelid][i])
    return [s1,np.sum(s4),np.sum(s5),np.sum(s6),np.sum(s7),np.mean(s4),np.mean(s5),np.mean(s6),np.mean(s7),np.var(s4),np.var(s5),np.var(s6),np.var(s7),np.sum(sum4),np.sum(sum5),np.sum(sum6),np.sum(sum7),np.mean(sum4),np.mean(sum5),np.mean(sum6),np.mean(sum7),np.var(sum4),np.var(sum5),np.var(sum6),np.var(sum7)]

def gethtl_test(hotel_cii,hotelid):
    sum4 = list()
    sum5 = list()
    sum6 = list()
    sum7 = list()
    s4 = list()
    s5 = list()
    s6 = list()
    s7 = list()
    if hotelid in hotel_cii:
        for i in xrange(getday("2016-01-03"),getday("2016-02-01")):
            if(getweekday(i)+1 == 5):
                sum5.append(hotel_cii[hotelid][i])
            elif(getweekday(i)+1 == 6):
                sum6.append(hotel_cii[hotelid][i])
            elif(getweekday(i)+1 == 7):
                sum7.append(hotel_cii[hotelid][i])
            else:
                sum4.append(hotel_cii[hotelid][i])
    s1 = sum(hotel_cii[hotelid][getday("2016-01-01"):getday("2016-01-03")])
    for i in xrange(getday("2015-02-7")-8-21,getday("2015-02-7")-8):
        if(getweekday(i)+1 == 5):
            s5.append(hotel_cii[hotelid][i])
        elif(getweekday(i)+1 == 6):
            s6.append(hotel_cii[hotelid][i])
        elif(getweekday(i)+1 == 7):
            s7.append(hotel_cii[hotelid][i])
        else:
            s4.append(hotel_cii[hotelid][i])
    return [s1,np.sum(s4),np.sum(s5),np.sum(s6),np.sum(s7),np.mean(s4),np.mean(s5),np.mean(s6),np.mean(s7),np.var(s4),np.var(s5),np.var(s6),np.var(s7),np.sum(sum4),np.sum(sum5),np.sum(sum6),np.sum(sum7),np.mean(sum4),np.mean(sum5),np.mean(sum6),np.mean(sum7),np.var(sum4),np.var(sum5),np.var(sum6),np.var(sum7)]

def getpoint(hotel_cii,inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split("\t#")[1].split("-")
            if data[0] in hotel_cii:
                if(int(data[1]) < 100):
                    htl_train = gethtl_train(hotel_cii,data[0])
                    for i in xrange(len(htl_train)):
                        f.write("f5_%d:%f\t"%(i,htl_train[i]))
                    f.write("#%s-%s\n"%(data[0],data[1]))
                else:
                    htl_test = gethtl_test(hotel_cii,data[0])
                    for i in xrange(len(htl_test)):
                        f.write("f5_%d:%f\t"%(i,htl_test[i]))
                    f.write("#%s-%s\n"%(data[0],data[1]))
    f.close()

if __name__ == '__main__':
    hotel_cii = getData(sys.argv[1])
    getpoint(hotel_cii,sys.argv[2],sys.argv[3])