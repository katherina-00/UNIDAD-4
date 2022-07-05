from claseProvincia import provincia


class ManejadorProvincias:
    indice=0
    __provincias=None

    def __init__(self):
        self.__provincias=[]

    def agregarProvincias(self, prov):
        prov.rowid=ManejadorProvincias.indice
        ManejadorProvincias.indice+=1
        self.__provincias.append(prov)

    def getListaProvincias(self):
        return self.__provincias
    
    
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                provincias=[prov.toJSON() for prov in self.__provincias]
                )
        return d