from claseProvincia import provincia
from claseObjectEncoder import ObjectEncoder
from claseManejadorProvincia import ManejadorProvincias

class RespositorioProvincia(object):
    __prov=None
    __manejador=None

    def __init__(self, prov):
        self.__prov = prov
        diccionario=self.__prov.leerJSONArchivo()
        self.__manejador=self.__prov.decodificarDiccionario(diccionario)
    
   
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()

    def agregarProvincias(self, prov):
        self.__manejador.agregarProvincias(prov)
        return prov
        
    def grabarDatos(self):
        self.__prov.guardarJSONArchivo(self.__manejador.toJSON())