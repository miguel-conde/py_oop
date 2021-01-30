import os

import customer


# Create instance of MyClass
my_customer = customer.Customer(nombre = 'Pepe Pérez')

# Print out class attribute value
print(my_customer.nombre)
print(my_customer.saldo)

my_customer_2 = customer.Customer(nombre = 'Juan Cano', saldo = -5000)

print(my_customer_2.nombre)
print(my_customer_2.saldo)

my_customer_3 = customer.Customer.from_file(os.path.join(".", "cliente_data.txt"))
print(my_customer_3.nombre)
print(my_customer_3.saldo)

# SOLUCIÓN 1
app_path = os.path.join(".", "src", "PYTHON")
os.environ["PYTHONPATH"] += os.pathsep + app_path

import accounts

# SOLUCIÓN 2
# import src.PYTHON.accounts as accounts

account_1 = accounts.BankAccount(1000)
account_2 = accounts.SavingsAccount(2000)

print(account_1.balance)
account_1.withdraw(100)
print(account_1.balance)

print(account_2.balance)
account_2.withdraw(200)
print(account_2.balance)

isinstance(account_1, accounts.BankAccount)
isinstance(account_1, accounts.SavingsAccount)
isinstance(account_2, accounts.BankAccount)
isinstance(account_2, accounts.SavingsAccount)
