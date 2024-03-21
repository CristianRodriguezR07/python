class Bedida:

    def __init__(self, nombre):
        self.__nombre = nombre

    def getObtenerNombre(self):
        return f"la bedida es {self.__nombre}"
    
class Cerveza(Bedida):
    def __init__(self, nombre,  marca, alcohol): 
        super().__init__(nombre)
        self.__marca = marca
        self.__alcohol = alcohol

    def getObtenerNombre(self):
        return f"{super().getObtenerNombre()} de la marca {self.__marca} de grado de alcohol {self.__alcohol}"

cerveza = Cerveza("poker", "bavaria", 4.0)
print(cerveza.getObtenerNombre())


