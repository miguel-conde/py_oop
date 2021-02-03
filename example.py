import os

import customer
help(customer)

# https://python-para-impacientes.blogspot.com/2017/04/internacionalizacion-del-codigo-i.html
import locale
loc = locale.getlocale()  # get current locale
# use German locale; name might vary with platform
locale.setlocale(locale.LC_ALL, 'esp.utf8')


# Create instance of MyClass
my_customer = customer.Customer(nombre = 'Pepe Pérez')

print(my_customer)
my_customer

# Print out class attribute value
print(my_customer.nombre)
print(my_customer.saldo)
# 'id' is internal and read-only
print(my_customer._id)
print(my_customer.id)
my_customer.id = 77
# 'credito' is internal but read-write
print(my_customer.credito)
my_customer.credito = 100
print(my_customer.credito)
my_customer.credito = -100

try:
  my_customer.credito = -100
except CreditError:
  my_customer.credito = 0

my_customer_2 = customer.Customer(nombre = 'Juan Cano', saldo = -5000)

my_customer_2 == my_customer
my_customer_2 == my_customer_2

print(my_customer_2.nombre)
print(my_customer_2.saldo)
print(my_customer_2.id)

my_customer_3 = customer.Customer.from_file(os.path.join(".", "cliente_data.txt"))
print(my_customer_3.nombre)
print(my_customer_3.saldo)

# SOLUCIÓN 1 - Mejor en .Renviron
app_path = os.path.join(".", "src", "PYTHON")
os.environ["PYTHONPATH"] += os.pathsep + app_path

import accounts

# SOLUCIÓN 2
# import src.PYTHON.accounts as accounts

account_1 = accounts.BankAccount(1000)
account_2 = accounts.SavingsAccount(2000, 0.03)

print(account_1.balance)
account_1.withdraw(100)
print(account_1.balance)

print(account_2.balance)
print(account_2.interest_rate)
account_2.withdraw(200)
print(account_2.balance)

isinstance(account_1, accounts.BankAccount)
isinstance(account_1, accounts.SavingsAccount)
isinstance(account_2, accounts.BankAccount)
isinstance(account_2, accounts.SavingsAccount)
