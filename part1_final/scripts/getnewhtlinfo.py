import sys

def getnewhtlinfo(inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip().split(",")
            if data[1] != "NULL" and data[3] != "NULL" and data[4] != "NULL":
                f.write(line)
    f.close()
if __name__ == '__main__':
    getnewhtlinfo(sys.argv[1],sys.argv[2])