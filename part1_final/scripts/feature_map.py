import sys
import os

def featuremap(inputfile,outputfile,featuremap):
    fea_map = dict()
    feaNum = 0
    f = file(outputfile,"w+")
    f1 = file(outputfile+"_sampleid","w+")
    if os.path.exists(featuremap):
        with open(featuremap) as fin:
            for line in fin:
                tmpkey,tmpval = line.strip().split("\t")
                fea_map.setdefault(tmpkey,tmpval)
                feaNum += 1
    with open(inputfile) as fin:
        f1.write("sampleid\n")
        for line in fin:
            data = line.strip().split("\t#")
            tmpdata = data[0].split("\t")
            sampleid = data[1]
            f1.write("%s\n"%sampleid)
            f.write(tmpdata[0]+"\t")
            for i in xrange(1,len(tmpdata)-1):
                tmpkey,tmpval = tmpdata[i].split(":")
                if tmpkey in fea_map:
                    f.write("%d:%s\t"%(int(fea_map[tmpkey]),tmpval))
                else:
                    fea_map[tmpkey] = feaNum
                    f.write("%d:%s\t"%(feaNum,tmpval))
                    feaNum += 1
            tmpkey,tmpval = tmpdata[len(tmpdata)-1].split(":")
            if tmpkey in fea_map:
                f.write("%d:%s\n"%(int(fea_map[tmpkey]),tmpval))
            else:
                fea_map[tmpkey] = feaNum
                f.write("%d:%s\n"%(feaNum,tmpval))
                feaNum += 1
    f.close()
    f1.close()
    f2 = file(featuremap,"w+")
    for key in fea_map:
        f2.write("%s\t%s\n"%(key,fea_map[key]))
    f2.close()

if __name__ == '__main__':
    featuremap(sys.argv[1],sys.argv[2],sys.argv[3])

