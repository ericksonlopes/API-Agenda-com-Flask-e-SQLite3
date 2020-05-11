
class tableInfo(object):

    def __init__(self, dic=None):
        if dic is None:
            dic = {}
        self.dic = dic

    def getComment(self):
        return self.dic["comment"]
    def setComment(self,comment):
        self.dic["comment"]=comment
    def getPoName(self):
        return self.dic["poName"]
    def setPoName(self,name):
        self.dic["poName"]=name
    def setTableName(self,a):
        self.dic["tableName"]=a
    def getTableName(self):
        return self.dic["tableName"]
    def setColCode(self,a):
        self.dic["colCode"]=a
    def getColCode(self):
        return  self.dic["colCode"]
    def getRel(self):
        return self.dic["rel"]
    def setRel(self,rel):
        self.dic["rel"]=rel





