import sys
import datetime

start = datetime.datetime.strptime("20150101","%Y%m%d")
def getday(time):
    return (datetime.datetime.strptime(time,"%Y-%m-%d") - start).days

def getData(inputfile):
    hotel_cii = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            hotel_cii.setdefault(data[1],[0]*396)
            hotel_cii[data[1]][getday(data[0])] = float(data[2])
    return hotel_cii

def getTarget(inputfile):
    hotel_list = list()
    with open(inputfile) as fin:
        firstline = fin.readline()
        for line in fin:
            data = line.strip()
            hotel_list.append(data)
    return firstline,hotel_list


def gettrainpoint(hotel_cii,hotel_list,outputfile):
    f = file(outputfile,"w+")
    for hotel in hotel_list:
        for i in xrange(getday("2016-02-07"),getday("2016-02-14")):
            f.write("%f\t#%s-%s\n"%(0,hotel,i))
    f.close()


if __name__ == '__main__':
    hotel_cii = getData(sys.argv[1])
    firstline,hotel_list = getTarget(sys.argv[2])
    gettrainpoint(hotel_cii,hotel_list,sys.argv[3])
