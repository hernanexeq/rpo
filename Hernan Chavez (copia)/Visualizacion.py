class visualizacion:
    __id:str
    __idpel:  str
    __f: str
    __hs: str
    __min: int
    def __init__(self,id,idpel,f,hs,min):
        self.__id=id
        self.__idpel=idpel
        self.__f=f
        self.__hs=hs
        self.__min=min
    def getid(self):
        return self.__id
    def getmin(self):
        return int(self.__min)
    def __eq__(self, otro):
        if isinstance(otro,visualizacion):
            return self.__id== otro.__id and self.__f==otro.__f and self.__hs==otro.__hs
        return False