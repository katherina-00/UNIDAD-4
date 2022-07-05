class fraccion:
    __numerador=0
    __denominador=0

    def __init__(self,num,den):
        self.__numerador : float = num
        if den == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")
        self.__denominador: float = den
    
    def __str__(self):
        return ("{}/{}".format(self.__numerador, self.__denominador)) 

    def __add__(self, other):
        num = (self.__numerador * other.__denominador) + (other.__numerador * self.__denominador)
        den = self.__denominador * other.__denominador
        resultado = fraccion(num,den)
        resultado.simplify()
        return resultado

    def __sub__(self , other):
        num = (self.__numerador * other.__denominador) - (other.__numerador * self.__denominador)
        den = self.__denominador * other.__denominador
        resultado = fraccion(num, den)
        resultado.simplify()
        return resultado
    
    def __mul__(self , other):
        num = self.__numerador * other.__numerador
        den = self.__denominador * other.__denominador
        resultado = fraccion(num, den)
        resultado.simplify()        
        return resultado
    
    def __truediv__(self , other):
        
        if other.__numerador == 0:
            raise ZeroDivisionError("Division por cero")
        
        num = self.__numerador * other.__denominador
        den = self.__denominador * other.__numerador
        resultado = fraccion(num, den)
        resultado.simplify()
        return resultado
    
    def simplificar(self):
        gcd = self.mcd(self.__numerador, self.__denominador)
        self.__numerador = int(self.__numerador / gcd)
        self.__denominador = int(self.__denominador / gcd)

    def mcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1