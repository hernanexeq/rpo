class alquiler:
    __nomalq: str
    __idcancha: str
    __hs: str
    __min: str
    __duralq: int
    def __init__(self,nom,id,hs,min,durac):
        self.__nomalq=nom
        self.__idcancha=id
        self.__hs=hs
        self.__min=min
        self.__duralq=durac
    def __repr__(self):
        return f'{self.__nomalq} {self.__idcancha} ({self.__hs}) {self.__min} {self.__duralq}'
    def __str__(self):
        return "%s %s %s %s %s"%(self.__nomalq,self.__idcancha,self.__hs,self.__min,self.__duralq)
    def getNom(self):
        return self.__nomalq
    def getId(self):
        return self.__idcancha
    def getHs(self):
        return self.__hs
    def getMin(self):
        return self.__min
    def getDura(self):
        return self.__duralq