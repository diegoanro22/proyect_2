class Dieta():
    def __init__(self, tipo, desayuno, almuerzo, cena):
        """
         Inicializa el objeto de clase para crear una nueva parte de la informacion
         
         @param tipo - Tipo del elemento a mostrar
         @param desayuno - Direccion del elemento a mostrar
         @param almuerzo - Almuerzo del elemento a mostrar
         @param cena - Conteudo de la cabecera que contiene el
        """
        self.tipo = tipo
        self.desayuno = desayuno
        self.almuerzo = almuerzo
        self.cena = cena

    def getTipo(self):
        """
         Returns the tipo of the object. This is used to distinguish between objects that are part of a group and those that are in an other group.
         
         
         @return tipo of the object as a C { str } or C { None } if there is no
        """
        return self.tipo
    
    def setTipo(self, tipo):
        """
         Set the Tipo of the LilyPond object. This is a setter method to avoid having to call it every time it is accessed.
         
         @param tipo - The Tipo of the LilyPond
        """
        self.tipo = tipo

    def getDesayuno(self):
        """
         Retorna el desayuno del cual se encuentra en la ventana
         
         
         @return Devuelve el desayuno del cual se encuentra en la vent
        """
        return self.desayuno
    
    def setDesayuno(self, desayuno):
        """
         Set desayuno of the planet. This is a setter and should be used by subclasses to set the desayuno of the planet
         
         @param desayuno - a boolean indicating whether or
        """
        self.desayuno = desayuno
    
    def getAlmuerzo(self):
        """
         Returns the almuerzo associated with this object. This is a wrapper around the : py : attr : ` almuerzo ` attribute.
         
         
         @return an instance of : py : class : ` ~montreal_forced_aligner. almuerzo. Almuerzo
        """
        return self.almuerzo
    
    def setAlmuerzo(self, almuerzo):
        """
         Set the almuerzo of the object. It is used to create a link between the object and the database
         
         @param almuerzo - The almuerzo of the
        """
        self.almuerzo = almuerzo

    def getCena(self):
        """
         Returns the cena of the object. This is a copy of the object that was passed to the constructor.
         
         
         @return the cena of the object ( instance of : class : ` openquake. hazardlib. geo. coa. Point `
        """
        return self.cena
    
    def setCena(self, cena):
        """
         Set the cena of this V1FeatureHyperv. This is a setter method. You can use it to set the value of the feature hypervisor.
         
         @param cena - The value of the cena of this V1FeatureHyperv
        """
        self.cena = cena