import sys
import datetime

start = datetime.datetime.strptime("20150101","%Y%m%d")
def getday(time):
    return (datetime.datetime.strptime(time,"%Y-%m-%d") - start).days

def getData(inputfile):
    hotel_pri = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            hotel_pri.setdefault(data[0],[0]*425)
            hotel_pri[data[0]][getday(data[1])] = float(data[2])
    return hotel_pri

def getfea(hotel_pri,inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split("\t#")[1].split("-")
            if data[0] in hotel_pri:
                f.write("f3:%f\t#%s-%s\n"%(hotel_pri[data[0]][int(data[1])],data[0],data[1]))
    f.close()
if __name__ == '__main__':
    hotel_pri = getData(sys.argv[1])
    getfea(hotel_pri,sys.argv[2],sys.argv[3])
