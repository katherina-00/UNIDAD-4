from claseMiAplicacion import Aplicacion
import requests
import json
def testAPP():
    response=requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
    response_info = response.json()
    v=response_info[0]['casa']['venta'].replace(",", ".")
    cotizacion=float(v)
    
    mi_app = Aplicacion(cotizacion)
if __name__ == '__main__':
    testAPP()
