import sys
import datetime
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

def getfea1(hotel_cii,outputfile):
    f = file(outputfile,"w+")
    for hotel in hotel_cii:
        for i in xrange(getday("2016-02-07"),getday("2016-02-14")):
            f.write("f1:%d\t#%s-%s\n"%(i-getday("2016-02-07")+1,hotel,i))
        for i in xrange(getday("2015-02-18"),getday("2015-02-25")):
            f.write("f1:%d\t#%s-%s\n"%(i-getday("2015-02-18")+1,hotel,i))
    f.close()

if __name__ == '__main__':
    # print getweekday(275)
    hotel_cii = getData(sys.argv[1])
    getfea1(hotel_cii,sys.argv[2])
