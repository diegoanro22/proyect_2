class Dieta():
    def __init__(self, tipo, desayuno, almuerzo, cena):
        self.tipo = tipo
        self.desayuno = desayuno
        self.almuerzo = almuerzo
        self.cena = cena

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getDesayuno(self):
        return self.desayuno
    
    def setDesayuno(self, desayuno):
        self.desayuno = desayuno
    
    def getAlmuerzo(self):
        return self.almuerzo
    
    def setAlmuerzo(self, almuerzo):
        self.almuerzo = almuerzo

    def getCena(self):
        return self.cena
    
    def setCena(self, cena):
        self.cena = cena