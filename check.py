
import sys,getopt
import codecs


def usage():
    print "*.py input output"

def processFile(arg_dict):
    file = arg_dict["input"]
    lineList = []
    with codecs.open(file,'r','gbk') as f:
        line = f.read()
        lineList.append(line)
        #print line
    outFile = arg_dict["output"]
    with codecs.open(outFile,'w','gbk') as f:
        for line in lineList:
            f.write(line)



if __name__ == '__main__':
    opts,args = getopt.getopt(sys.argv[1:],"hi:o:")
    arg_dict = {}
    for op,value in opts:
        if op == "-i":
            arg_dict["input"] = value
        elif op == "-o":
            arg_dict["output"] = value
        elif op == "-h":
            usage()
            sys.exit()
    processFile(arg_dict)

print "test"