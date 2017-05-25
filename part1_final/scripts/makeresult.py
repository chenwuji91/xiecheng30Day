import sys

def makeresult(inputfile,outputfile):
    f = file(outputfile,"w+")
    hotel_val = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            val = float(data[1])
            if val < 0:
                val = 0
            hotelid,day = data[0].split("-")
            hotel_val.setdefault(hotelid,[0]*29)
            hotel_val[hotelid][int(day)-396] = val
        for hotelid in hotel_val:
            f.write("%s"%hotelid)
            for i in xrange(len(hotel_val[hotelid])):
                f.write(",%f"%hotel_val[hotelid][i])
            f.write("\n")
    f.close()
if __name__ == '__main__':
    makeresult(sys.argv[1],sys.argv[2])
