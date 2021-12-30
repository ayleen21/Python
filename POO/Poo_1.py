#Propiedades

class Coche():
    
    def __init__(self): #Metodo constructor

        #con el self se agregan las propiedades al estado inicial

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__Ruedas=4
        self.__enmarcha=False #Por defecto el coche detenido

#----------------COMPORTAMIENTOS-------------------
    def arrancar(self,arrancamos): #-->Objeto perteneciente de la clase
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo==False):  
            return" Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche esta parado"
            
    def estado(self):
        print("El coche tiene " , self.__Ruedas, " ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ",self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
#---------------------------------------------------------------------
miCoche=Coche() #Instancia


print(miCoche.arrancar(True))

miCoche.estado()

print ("-----------------A continuacion creamos el segundo objeto--------------------")

miCoche2=Coche()

print (miCoche2.arrancar(False))
miCoche2.estado()

