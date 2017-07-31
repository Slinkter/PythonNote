class MiClase(object):
    """
    Mi clase doc
    """
    class_prop = "Propiedad de clase"

    def __init__(self, nombre=None, verbose=False) :
        """
        Documentacion de constructor
        """
        self.data = []
        self._private_data = []
        self._nombre = nombre
    
    def __del__(self):
        pass
    
    def __add__(self, a):
        pass
    
    def __getitem__(self, key):
        pass
    
    def function(self):
        """
        Documentacion de methodo
        """
        self._privada()
        print("Este mensaje se imprime desde la clase")
    
    def _privada(self):
        """
        Documentacion de methodo
        """
        print("Este mensaje se imprime desde la clase")
        
    @staticmethod
    def metodo_estatico():
        print("Statico, no tiene acceso a 'self'")
    
    @classmethod
    def verboso(cls):
        print("Metodo de clase")
        a = cls(verbose=False)
        del a.data
    
    @property
    def nombre(self):
        print("Calling nombre")
        return self._nombre
    
    @nombre.setter
    def nombre(self, a):
        self._nombre = a
        print("Calling setter")
    
    def algo(self):
        """
        doc de lo que hago
        """
        raise NotImplementedError()
        
        
mi_lista = [1,2,3,"hola",5]
mi_lista.count("hola")
mi_lista.append("Nuevo")
print(mi_lista)


