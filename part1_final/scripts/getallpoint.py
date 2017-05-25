import sys

def getpoint(trainfile,validfile,testfile,outputfiel):
    f = file(outputfiel,"w+")
    with open(trainfile) as fin,open(validfile) as fin2,open(testfile) as fin3:
        for line in fin:
            f.write(line)
        for line in fin2:
            f.write(line)
        for line in fin3:
            f.write(line)
    f.close()

if __name__ == '__main__':
    getpoint(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
