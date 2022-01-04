import pickle

class Persona:

    def   __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        listadePersonas=open("ficheroExterno","ab+") #Agregar informacion binaria
        listadePersonas.seek(0) #Desplazar a la posicion cero

        try:
                self.personas=pickle.load(listadePersonas)
                print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
                 print("El fichero esta vacio")

        finally:
                listadePersonas.close()
                del(listadePersonas)

    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasenFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasenFicheroExterno(self):
        listadePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,listadePersonas)
        listadePersonas.close()
        del(listadePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas:
         print (p)

miLista=ListaPersonas()
persona=Persona("Antonio","Masculino",49)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

