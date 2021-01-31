class CreditError(Exception): pass


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
  
  # - Starts with a single _ → "internal"
  # - Not a part of the public API
  # - As a class user: "don't touch this"
  # - As a class developer: use for implementation details, helper functions..
  _NEW_CUSTOMER_ID = 0 
  
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
  def __init__(self, nombre, credito = 0, saldo = 0):
    
    # Inicialización de atributos de instancia
    # - Nombres en minúscula, separando palabras con "_"
    self.nombre = nombre
    
    # 'saldo' is a part of the public API
    if (saldo < Customer.MIN_SALDO):
      self.saldo = Customer.MIN_SALDO
    else:
      self.saldo = saldo
      
    Customer._NEW_CUSTOMER_ID += 1
    # Use "protected" attribute with leading '_' to store data - INTERNAL
    self._id = Customer._NEW_CUSTOMER_ID
    
    if credito >= 0:
      self._credito = credito
    else:
      print("Forzando a 0 !")
      self._credito = 0
    
  # OTROS MÉTODOS
  # - Nombres en minúscula, separando palabras con "_"
  
  # "Getters" and "Setters"
  
  # Use @property on a method whose name is exactly the name of the restricted 
  # attribute; return the internal attribute
  # _id is internal read-only => NO @id.setter
  @property
  def id(self):
    return self._id
  
  # _credito is internal read-write
  @property
  def credito(self):
    return self._credito
  
  @credito.setter
  def credito(self, new_credito):
    if new_credito < 0:
      raise CreditError("Nuevo credito inválido")
    
    self._credito = new_credito
    
    
  # Overloading - comparison
  
  def __eq__(self, other):
    return ((self._id == other._id) and 
            (self.nombre == other.nombre) and 
            (self._credito == other._credito) and 
            (self.saldo == other.saldo))
  
  # Overloading - Métodos para imprimir el objeto
  
  # Leading and trailing __ are only used for built-in Python methods 
  # ( __init__() , __repr__() )!
  
  # Informal, for end user
  # STRing representation
  def __str__(self):
    
    cust_str = """
    Cliente:
      Nombre: {nombre}
      Credito: {credito}
      Saldo: {saldo}
    """.format(nombre = self.nombre, credito = self._credito, saldo = self.saldo)
    
    return cust_str
  
  # Formal, for developer
  # REPRoducible REPResentation
  # Fallback for print
  def __repr__(self):
    
    # Notice the '...' around name
    cust_repr = """
    Customer('{nombre}', {credito}, {saldo})
    """.format(nombre = self.nombre, credito = self._credito, saldo = self.saldo)
    
    return cust_repr
