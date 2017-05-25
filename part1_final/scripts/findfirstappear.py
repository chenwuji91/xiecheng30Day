import sys
import datetime
start = datetime.datetime.strptime("20150101","%Y%m%d")
def getday(time):
    return (datetime.datetime.strptime(time,"%Y/%m/%d") - start).days

def getData(inputfile):
    hotel_pri = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            hotel_pri.setdefault(data[0],[0]*365)
            if(getday(data[1]) < 365):
                hotel_pri[data[0]][getday(data[1])] = float(data[2])
    return hotel_pri

def getfirstappear(hotel_pri,outputfile):
    f = file(outputfile,"w+")
    for hotel in hotel_pri:
        for i in xrange(365):
            if hotel_pri[hotel][i] != 0:
                f.write("%s-%d\n"%(hotel,i))
                break
    f.close()

if __name__ == '__main__':
    hotel_pri = getData(sys.argv[1])
    getfirstappear(hotel_pri,sys.argv[2])
