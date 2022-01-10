import sqlite3

from Hats import Hat
from Repository import repo
from Suppliers import Supplier

with open('config.txt', 'r') as file:
    config = file.readlines()
firstLine = config[0].split(',')
configNumOfEntries = int(firstLine[0])
configNumOfSuppliers = int(firstLine[1])
repo.create_tables()

for i in range(configNumOfEntries + 1, len(config)):
    entry = config[i].split(',')
    supplier = Supplier(entry[0], entry[1])
    repo.suppliers.insert(supplier)

for i in range(1, configNumOfEntries + 1):
    entry = config[i].split(',')
    hat = Hat(entry[0], entry[1], entry[2], entry[3])
    repo.hats.insert(hat)

