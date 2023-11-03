class IMC():
    def __init__(self, altura, peso, edad):
        self.altura = altura
        self.peso = peso
        self.edad = edad

    def getAltura(self):
        return self.altura
    
    def serAltura(self, altura):
        self.altura = altura

    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso

    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad