import sys

def getbaseres(inputfile):
    hotel_base = dict()
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split(",")
            hotel_base.setdefault(data[0],data[1:])
    return hotel_base

def getensres(inputfile):
    hotel_ens = dict()
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split(",")
            hotel_ens.setdefault(data[0],data[1:])
    return hotel_ens

def makeresult(hotel_base,hotel_ens,outputfile):
    f = file(outputfile,"w+")
    f.write("hotelid,2016/2/1,2016/2/2,2016/2/3,2016/2/4,2016/2/5,2016/2/6,2016/2/7,2016/2/8,2016/2/9,2016/2/10,2016/2/11,2016/2/12,2016/2/13,2016/2/14,2016/2/15,2016/2/16,2016/2/17,2016/2/18,2016/2/19,2016/2/20,2016/2/21,2016/2/22,2016/2/23,2016/2/24,2016/2/25,2016/2/26,2016/2/27,2016/2/28,2016/2/29\n")
    for hotel in hotel_base:
        f.write("%s"%hotel)
        hotel_base[hotel][6:13] = hotel_ens[hotel][6:13]
        for i in xrange(len(hotel_base[hotel])):
            f.write(",%s"%hotel_base[hotel][i])
        f.write("\n")
    f.close()

if __name__ == '__main__':
    hotel_base = getbaseres(sys.argv[1])
    hotel_ens = getensres(sys.argv[2])
    makeresult(hotel_base,hotel_ens,sys.argv[3])
