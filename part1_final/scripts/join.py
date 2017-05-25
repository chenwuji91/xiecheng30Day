import sys
def join(mainfile,vicefile,outputfile):
    vicedata = dict()
    with open(vicefile) as fin:
        for line in fin:
            tmpkey = line.strip().split("\t#")
            vicedata.setdefault(tmpkey[1],tmpkey[0])
    maindata = dict()
    with open(mainfile) as fin:
        for line in fin:
            tmpkey = line.strip().split("\t#")
            maindata.setdefault(tmpkey[1],tmpkey[0])
    for key,val in vicedata.iteritems():
        if key in maindata:
            maindata[key] += "\t"+val
    f = file(outputfile,"w+")
    for key,val in maindata.iteritems():
        f.write(val+"\t#"+key+"\n")

if __name__ == '__main__':
    join(sys.argv[1],sys.argv[2],sys.argv[3])