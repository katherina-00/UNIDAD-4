from claseRepositorioProvincia import RespositorioProvincia
from vistaProvincia import ProvinciaView
from claseControladorProvincia import ControladorProvincias
from claseObjectEncoder import ObjectEncoder

def main():
    prov=ObjectEncoder('datos.json')
    repo=RespositorioProvincia(prov)
    vista=ProvinciaView()
    
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()