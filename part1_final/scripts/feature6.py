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

def getmax(hotel_cii):
    hotel_max =  dict()
    for hotel in hotel_cii:
        htlmax = max(hotel_cii[hotel])
        hotel_max[hotel] = htlmax
    return hotel_max

def getfea(hotel_max,inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split("\t#")[1].split("-")
            if(hotel_max.has_key(data[0])):
                f.write("f6:%f\t#%s-%s\n"%(hotel_max[data[0]],data[0],data[1]))
    f.close()

if __name__ == '__main__':
    hotel_cii = getData(sys.argv[1])
    hotel_max = getmax(hotel_cii)
    getfea(hotel_max,sys.argv[2],sys.argv[3])
