class provincia(object):
    __capital=None
    __nombre=None
    __cantHabitantes=None
    __cantDepPar=None
    
    def __init__(self, nombre,capital, cantHabitantes, cantDepPar):
        self.__nombre =self.requerido(nombre, 'Nombre es un valor requerido')
        self.__capital=self.requerido(capital, 'Capital es un valor requerido')
        self.__cantHabitantes = self.requerido(cantHabitantes,'Cantidad de habitantes es un valor requerido')
        self.__cantDepPar = self.requerido(cantDepPar,'Cantidad de departamentos/partidos es un valor requerido')
    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getCantHabitantes(self):
        return self.__cantHabitantes
    def getCantDepPar(self):
        return self.__cantDepPar
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    nombre=self.__nombre,
                                    capital=self.__capital,
                                    cantHabitantes=self.__cantHabitantes,
                                    cantDepPar=self.__cantDepPar
                                )
                )
        return d