from ClasePacientes import paciente
from ClaseManejador import manejador
from ClaseObjectEncoder import ObjectEncoder
from ClaseControlador import ControladorPacientes
from ClaseRepositorio import RespositorioPacientes
from claseVista import PacienteView


def main():
    conn = ObjectEncoder('pacientes.json')
    repo = RespositorioPacientes(conn)
    vista = PacienteView()
    ctrl = ControladorPacientes(repo,vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__=='__main__' :
    main()

##if __name__=='__main__':
##    jF = ObjectEncoder('pacientes.json')
##    Manejador = manejador()
##    testPacientes(Manejador)
##    diccionario = jF.leerJSONArchivo()
##    Manejador = jF.decodificarDiccionario(diccionario)
##    Manejador.mostrarPacientes()
##    diccionarioManejador = Manejador.toJSON()
##    jF.guardarJSONArchivo(diccionarioManejador, 'pacientes.json')
