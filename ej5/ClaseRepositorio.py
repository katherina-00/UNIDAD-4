from ClasePacientes import paciente
from ClaseObjectEncoder import ObjectEncoder
from ClaseManejador import manejador

class RespositorioPacientes(object):
    __conn=None
    __Manejador=None

    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__Manejador=self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, Paciente):
        return Paciente.getApellido(), Paciente.getNombre(), Paciente.getTelefono(), Paciente.getAltura(), Paciente.getPeso()

    def obtenerListaPacientes(self):
        return self.__Manejador.getListaPacientes()

    def agregarPaciente(self, Paciente):
        self.__Manejador.agregarPaciente(Paciente)
        return Paciente

    def modificarPaciente(self, Paciente):
        self.__Manejador.updatePaciente(Paciente)
        return Paciente

    def borrarPaciente(self, Paciente):
        self.__Manejador.deletePaciente(Paciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__Manejador.toJSON())
        