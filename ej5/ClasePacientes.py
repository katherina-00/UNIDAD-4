import json
from pathlib import Path

class paciente:
    __nombre = None
    __apellido = None
    __telefono = None
    __altura = None
    __peso = None

    def __init__(self, nombre, apellido, telefono, altura, peso):
        self.__nombre = self.requerido(nombre, 'Nombre es una vlor requerido')
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        self.__telefono = telefono
        self.__altura = self.requerido(altura, 'La altura es un valor requerido')
        self.__peso = self.requerido(peso, 'El peso es un valor requerido')

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso
    
    def getIMC(self):
        altura=float(float(self.getAltura()/100))
        peso=float(self.getPeso())
        imc= float(peso / (altura * altura))
        return imc
        
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                telefono = self.__telefono,
                altura = self.__altura,
                peso = self.__peso
            )
        )
        