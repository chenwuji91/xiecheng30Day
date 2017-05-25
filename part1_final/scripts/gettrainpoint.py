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

def getfirst(inputfile):
    hotel_star = dict()
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split("-")
            hotel_star[data[0]] = int(data[1])
    return hotel_star

def gettrainpoint(hotel_cii,hotel_list,hotel_star,outputfile):
    f = file(outputfile,"w+")
    for hotel in hotel_cii:
        if hotel not in hotel_list:
            if(not hotel_star.has_key(hotel) or hotel_star[hotel] != 0):
                continue
            if(sum(hotel_cii[hotel][getday("2015-02-18"):getday("2015-02-25")]) == 0):
                continue
            for i in xrange(getday("2015-02-18"),getday("2015-02-25")):
                f.write("%f\t#%s-%s\n"%(hotel_cii[hotel][i],hotel,i))
    f.close()


if __name__ == '__main__':
    hotel_cii = getData(sys.argv[1])
    firstline,hotel_list = getTarget(sys.argv[2])
    hotel_star = getfirst(sys.argv[3])
    gettrainpoint(hotel_cii,hotel_list,hotel_star,sys.argv[4])
