import sys
import numpy as np

def getdata(inputfile,inputfile2,outputfile):
    res1 = dict()
    f = file(outputfile,"w+")
    with open(inputfile) as fin, open(inputfile2) as fin2:
        firstline = fin.readline()
        #fin2.readline()
	f.write(firstline)
        for line in fin:
            data = line.strip().split(",")
            res1.setdefault(data[0],data[1:])
        for line in fin2:
            data = line.strip().split(",")
            f.write("%s"%data[0])
            for i in xrange(len(res1[data[0]])):
                if i == 5:
                    f.write(",%f"%(float(data[i+1])))
                else:
				    f.write(",%f"%((float(res1[data[0]][i])+float(data[i+1]))/2))
            f.write("\n")
    f.close()

if __name__ == '__main__':
    getdata(sys.argv[1],sys.argv[2],sys.argv[3])
