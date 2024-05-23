class cancha:
    __id: str
    __tipopis: str
    __impxhs: float
    def __init__(self,id,tip,imp):
        self.__id=id
        self.__tipopis=tip
        self.__impxhs=imp
    def __str__(self):
        return "%s %s %f"%(self.__id,self.__tipopis,self.__impxhs)
    def getid(self):
        return self.__id
    def getimp(self):
        return self.__impxhs
    