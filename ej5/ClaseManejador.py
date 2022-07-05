from ClasePacientes import paciente

class manejador:
    indice=0
    __pacientes = None

    def __init__(self):
        self.__pacientes = []

    def agregarPaciente(self, Paciente):
        Paciente.rowid = manejador.indice
        manejador.indice += 1
        self.__pacientes.append(Paciente)

    def getListaPacientes(self):
        return self.__pacientes

    def deletePaciente(self, Paciente):
        indice = self.obtenerIndicePaciente(Paciente)
        self.__pacientes.pop(indice)

    def updatePaciente(self, Paciente):
        indice=self.obtenerIndicePaciente(Paciente)
        self.__pacientes[indice] = Paciente

    def obtenerIndicePaciente(self, Paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == Paciente.rowid:
                bandera=True
            else:
                i+=1
        return i
        
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                pacien=[Paciente.toJSON() for Paciente in self.__pacientes]
                )
        return d
