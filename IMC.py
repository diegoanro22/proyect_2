class IMC():
    def __init__(self, altura, peso, edad):
        """
         Inicializa el objeto altura y peso y el edad. En caso de que se haya necesarios para cada estructura de este clase
         
         @param altura - La altura al que pertenece el objeto
         @param peso - La peso al que pertenece el objeto
         @param edad - La edad al que pertenece el obj
        """
        self.altura = altura
        self.peso = peso
        self.edad = edad

    def getAltura(self):
        """
         Retorna el altura de la ventana. Devuelve el altura correspondiente al punto de la ventana.
         
         
         @return L'altura de la ventana ( str ) o None si no existe ( no altura
        """
        return self.altura
    
    def serAltura(self, altura):
        """
         Set the altura of the serpentine. It is used to determine the type of serpentine
         
         @param altura - The altura of the ser
        """
        self.altura = altura

    def getPeso(self):
        """
         Returns the peso associated with this event. This is a property so it can be used in subclasses that need to know what is the peso for a given event.
         
         
         @return a list of peso associated with this event or None if there is no peso associated
        """
        return self.peso
    
    def setPeso(self, peso):
        """
         Set the peso of this TapiOduOduMipPeso. Note that this does not update the tapiOduOduMipPeso property of the object.
         
         @param peso - The peso of this TapiOduOdu
        """
        self.peso = peso

    def getEdad(self):
        """
         Returns edad information. This is a read - only property. It can be used to read the data that is stored in the EDIC file or to write a new EDIC file.
         
         
         @return a L { Deferred } which fires with a list of C { str } s that represent the EDAD
        """
        return self.edad
    
    def setEdad(self, edad):
        """
         Set the edad to use for this channel. This is a bit tricky because we don't have a way to know what is going on on the EDAD and it's easier to do it in one place.
         
         @param edad - The edad to use for this channel
        """
        self.edad = edad