class visualizacion:
    __id:str
    __idpel:  str
    __fyhs: str
    __min: int
    def __init__(self,id,idpel,fyh,min):
        self.__id=id
        self.__idpel=idpel
        self.__fyhs=fyh
        self.__min=min
    def getid(self):
        return self.__id
    def getmin(self):
        return self.__min
    def __eq__(self, otro):
        if isinstance(otro,visualizacion):
            return self.__id== otro.__id and self.__fyhs==otro.__fyhs
        return False