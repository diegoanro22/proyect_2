class Ejercicio():
    def __init__(self, grupoMusculo, nombre, sets, reps):
        """
         Inicializa el objeto de clase CapturaMusculo. En caso de que se pueden reproducir la informacion de los valores a partir desde el objeto CapturaMusculo.
         
         @param grupoMusculo - Los valores que tienen cambiar el objeto CapturaMusculo.
         @param nombre - Nombre del objeto CapturaMusculo.
         @param sets - Lista de los valores que contiene la informacion de los valores a partir de la informacion de los valores a part
         @param reps
        """
        self.grupoMusculo = grupoMusculo
        self.nombre = nombre
        self.sets = sets
        self.reps = reps

    def getGrupoMusculo(self):
        """
         Retorna el grado de musculo que corresponde dentro del registro.
         
         
         @return Cadena de musculo que corresponde dentro del registro de mus
        """
        return self.getGrupoMusculo
    
    def setGrupoMusculo(self, grupoMusculo):
        """
         Set el grupo de musculo del objeto Cadena. Es la informacion de este metodo se encarga de realizar el valor de la clase Cadena.
         
         @param grupoMusculo - El grupo de muscul
        """
        self.grupoMusulo = grupoMusculo

    def getNombre(self):
        """
         Devuelve el nombre de la ventana. Creada los parametros establecidos en el archivo de manera que haya la ventana.
         
         
         @return Nombre de la ventana ( int ) or None if no existe ( bool ). False si no existe
        """
        return self.nombre
    
    def setNombre(self, nombre):
        """
         Set el nombre de la pantalla. Luego de esta clase se encuentra en el archivo CADA_NOMBRE
         
         @param nombre - La cadena de la pantall
        """
        self.nombre = nombre
    
    def getSets(self):
        """
         Returns the set of sets that this rule applies to. This is a copy of the sets attribute but with the addition of the set itself as a new attribute.
         
         
         @return a list of sets that this rule applies to in the same order as the sets attribute of the Rule
        """
        return self.sets
    
    def setSets(self, sets):
        """
         Set the sets to be used in this test. This is a convenience method for overriding the set method in the unittest. TestCase.
         
         @param sets - A list of sets to be used in this test
        """
        self.sets = sets

    def getReps(self):
        """
         Get reps of the test. This is a getter. Do not use it for production code.
         
         
         @return The list of tests to run in this test case. If there are no tests to run returns an empty list
        """
        return self.reps
    
    def setReps(self, reps):
        """
         Set reps for this job. This is a setter and should be called before submitting jobs to the job queue
         
         @param reps - A list of job
        """
        self.reps = reps