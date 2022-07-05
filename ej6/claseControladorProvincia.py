import requests
from vistaProvincia import NewProv

class ControladorProvincias(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())

    def crearProvincia(self):
        nuevaProvincia = NewProv(self.vista).show()
        if nuevaProvincia:
            prov = self.repo.agregarProvincias(nuevaProvincia)
            self.provincias.append(prov)
            self.vista.agregarProvincia(prov)

    def seleccionarProvincia(self, index):
        self.seleccion = index
        prov = self.provincias[index]
        response=requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + prov.getCapital() + '&units=metric&appid=ed8ca0d268b1de583b1041be4616a6b3')
        response_info=response.json()
        datos = (response_info['main'])
        self.vista.verProvinciaEnForm(prov,datos)


    def start(self):
        for c in self.provincias:
            self.vista.agregarProvincia(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()