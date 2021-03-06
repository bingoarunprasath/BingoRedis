
class BingoDataHandler:
    myfile = ''
    mydict = {}
    def __init__(self,myfile):
        self.myfile=open(myfile,"ab+")
        self.convertToDict()

    def convertToDict(self):
        try:
            self.mydict={}
            for i in self.myfile:
                i=i.rstrip().split('\t')
                self.mydict[i[0]]=i[1]
            print self.mydict
        except:
            print "Some Error"


    def getData(self,mykey):
        '''
        for i in self.myfile:
            i = i.rstrip().split('\t')
            if i[0]==mykey:
                return i[1]
        return "No data found"
        '''
        try:
            return self.mydict[mykey.rstrip()]
        except KeyError,e:
            return "No value found for this key\n"

    def putData(self,mykey,myvalue):
        self.mydict[mykey]=myvalue

    def writeToFile(self):
        for key in self.mydict:
            self.myfile.write(key+'\t'+self.mydict[key]+'\n')

