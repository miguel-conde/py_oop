
# Class BankAccount ---------------------------------------------------------

class BankAccount: # Con mayúsculas y palabras pegadas
  # Usar siempre docstrings
  """" 
  Clase para usar de ejemplo y plantilla
  """
  # ATRIBUTOS DE CLASE 
  #  - Global constants related to the class shared among all instances
  #     - minimal/maximal values for attributes
  #     - commonly used values and constants
    
  # MÉTODOS DE CLASE
  
  # CONSTRUCTOR
  
  def __init__(self, balance):
    
    # Inicialización de atributos de instancia
    # - Nombres en minúscula, separando palabras con "_"
    self.balance = balance
    
  # OTROS MÉTODOS
  # - Nombres en minúscula, separando palabras con "_"
  def withdraw(self, amount):
    self.balance -= amount
  
# Class SavingAccount -------------------------------------------------------

# Class inherited from BankAccount
class SavingsAccount(BankAccount): # Con mayúsculas y palabras pegadas
  # Usar siempre docstrings
  """" 
  Clase derivada de BankAccount
  """
  # ATRIBUTOS DE CLASE 
  #  - Global constants related to the class shared among all instances
  #     - minimal/maximal values for attributes
  #     - commonly used values and constants
    
  # MÉTODOS DE CLASE
  
  # CONSTRUCTOR
  
  # Constructor speficially for SavingsAccount with an additional parameter
  # Can run constructor of the parent class BUT don't _have to_ call the parent 
  # constructors
  def __init__(self, balance, interest_rate):
    
    # Call the parent constructor using ClassName.__init__()
    BankAccount.__init__(self, balance) # <--- self is a SavingsAccount but also a BankAccount
    
    # Add more functionality
    self.interest_rate = interest_rate
    
  # OTROS MÉTODOS
  # - Nombres en minúscula, separando palabras con "_"
  
  def compute_interest(self, n_periods = 1):
    
    return self.balance * ( (1 + self.interest_rate) ** n_periods - 1)
  
# Class CheckingAccount ---------------------------------------------------

class CheckingAccount(BankAccount):
  
  def __init__(self, balance, limit):
    BankAccount.__init__(self, content)
    self.limit = limit
    
  def deposit(self, amount):
    self.balance += amount
      
    # Can change the signature (add parameters)
  def withdraw(self, amount, fee=0):
    # Call a method from the parent class
    if fee <= self.limit:
      BankAccount.withdraw(self, amount - fee)
    else:
      BankAccount.withdraw(self, amount - self.limit)
