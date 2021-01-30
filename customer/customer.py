


class Customer: # Con mayúsculas y palabras pegadas
  # Usar siempre docstrings
  """" 
  Clase para usar de ejemplo y plantilla
  """
  # ATRIBUTOS DE CLASE 
  #  - Global constants related to the class shared among all instances
  #     - minimal/maximal values for attributes
  #     - commonly used values and constants
  MIN_SALDO = 0
  
  # MÉTODOS DE CLASE
  @classmethod
  def my_class_method(cls): # <---cls argument refers to the class
    # Can't use any instance attributes :(
    return 0
  
  # Por ejemplo: CONSTRUCTOR ALTERNATIVO
  @classmethod
  def from_file(cls, filename):
    with open(filename, "r") as f:
      nombre = f.readline()
      
    return cls(nombre) # cls(...) will call __init__(...)
  
  # CONSTRUCTOR
  def __init__(self, nombre, saldo = 0):
    
    # Inicialización de atributos de instancia
    # - Nombres en minúscula, separando palabras con "_"
    self.nombre = nombre
    
    if (saldo < Customer.MIN_SALDO):
      self.saldo = Customer.MIN_SALDO
    else:
      self.saldo = saldo
    
  # OTROS MÉTODOS
  # - Nombres en minúscula, separando palabras con "_"
