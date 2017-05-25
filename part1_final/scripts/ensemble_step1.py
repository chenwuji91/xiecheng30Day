import sys

def ensemble(inputfile,filenum,outputfile):
    res = dict()
    for i in xrange(filenum):
        with open(inputfile+"_"+str(i)+".csv") as fin:
            for line in fin:
                data = line.strip().split(",")
                if res.has_key(data[0]):
                    res[data[0]] = map(lambda y,z:y+z,res[data[0]],map(lambda x:float(x),data[1:]))
                else:
                    res.setdefault(data[0],map(lambda x:float(x),data[1:]))
    f = file(outputfile,"w+")
    for hotel in res:
        f.write("%s"%hotel)
        for i in xrange(len(res[hotel])):
            f.write(",%f"%(res[hotel][i]/filenum))
        f.write("\n")
    f.close()

if __name__ == '__main__':
    ensemble(sys.argv[1],int(sys.argv[2]),sys.argv[3])
