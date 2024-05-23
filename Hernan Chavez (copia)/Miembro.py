class miembro:
    __id: str
    __apyn:str
    __correo:str
    def __init__(self,id,apyn,correo):
        self.__id=id
        self.__apyn=apyn
        self.__correo=correo
    def getcorreo(self):
        return self.__correo
    def getid(self):
        return self.__id
    def getayn(self):
        return self.__apyn