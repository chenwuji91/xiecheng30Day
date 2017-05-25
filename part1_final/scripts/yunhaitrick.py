import sys
import numpy as np
import datetime

fes = ["2015-01-01","2015-01-02","2015-02-18","2015-02-19","2015-02-20","2015-02-21","2015-02-22","2015-02-23"\
,"2015-04-04","2015-04-05","2015-05-01","2015-05-02","2015-06-20","2015-06-21","2015-09-03"\
,"2015-09-04","2015-09-26","2015-09-27","2015-10-01","2015-10-02","2015-10-03","2015-10-04","2015-10-05","2015-10-06"\
,"2016-01-01","2016-01-02","2015-02-14","2015-12-24","2015-12-25","2015-02-17","2015-04-03","2015-04-30","2015-06-19","2015-09-02",\
"2015-09-25","2015-09-30","2015-12-31"]

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

def getfeslist(fesdays):
    feslist = list()
    map(lambda x:feslist.append(getday(x)),fesdays)
    return feslist

def getfirst(inputfile):
    hotel_star = dict()
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split("-")
            hotel_star[data[0]] = int(data[1])
    return hotel_star

def getTarget(inputfile):
    hotel_list = list()
    with open(inputfile) as fin:
        firstline = fin.readline()
        for line in fin:
            data = line.strip()
            hotel_list.append(data)
    return firstline,hotel_list

def getmean(hotel_list,hotel_cii,feslist,hotel_star,outputfile):
    hotel_mean = dict()
    hotel_mean_5 = dict()
    hotel_mean_6 = dict()
    f = file(outputfile,"w+")
    for hotel in hotel_list:
        # if hotel not in hotel_cii:
        #     continue
        sum14 = list()
        sum5 = list()
        sum6 = list()
        for i in xrange(getday("2015-12-01"),getday("2016-02-01")):
	    if not hotel_star.has_key(hotel):
		print("There is no hotelid:%s in htlprice.csv"%hotel) 
		print("The result may wrong!")
		continue
            if i in feslist or i < hotel_star[hotel]:
                continue
            tmpval = hotel_cii[hotel][i]
            wday = getweekday(int(i)) + 1
            if wday != 5 and wday != 6:
                sum14.append(tmpval)
            elif wday == 5:
                sum5.append(tmpval)
            elif wday == 6:
                sum6.append(tmpval)
        hotel_mean[hotel] = np.mean(sum14)
        hotel_mean_5[hotel] = np.mean(sum5)
        hotel_mean_6[hotel] = np.mean(sum6)
        
        f.write("%s"%hotel)
        for i in xrange(getday("2016-02-01"),getday("2016-03-01")):
            wday = getweekday(int(i)) + 1
            if wday != 5 and wday != 6:
                f.write(",%f"%hotel_mean[hotel])
            elif wday == 5:
                f.write(",%f"%hotel_mean_5[hotel])
            elif wday == 6:
                f.write(",%f"%hotel_mean_6[hotel])
        f.write("\n")
    f.close()
if __name__ == '__main__':
    hotel_cii = getData(sys.argv[1])
    feslist = getfeslist(fes)
    hotel_star = getfirst(sys.argv[2])
    firstline,hotel_list = getTarget(sys.argv[3])
    getmean(hotel_list,hotel_cii,feslist,hotel_star,sys.argv[4])
