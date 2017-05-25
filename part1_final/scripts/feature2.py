import sys

def getData(inputfile):
    hotel_sta = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
	    if data[0] in hotel_sta:
		continue
            hotel_sta.setdefault(data[0],list())
            for i in xrange(1,len(data)):
                if(data[i] == "F"):
                    data[i] = "0"
                elif(data[i] == "T"):
                    data[i] = "1"
                hotel_sta[data[0]].append(data[i])
    return hotel_sta

def getpoint(hotel_sta,inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split("\t#")[1].split("-")
            if data[0] in hotel_sta:
                for i in xrange(len(hotel_sta[data[0]])):
                    f.write("f2_%d:%s\t"%(i,hotel_sta[data[0]][i]))
                f.write("#%s-%s\n"%(data[0],data[1]))
    f.close()

if __name__ == '__main__':
    hotel_sta = getData(sys.argv[1])
    getpoint(hotel_sta,sys.argv[2],sys.argv[3])
    
