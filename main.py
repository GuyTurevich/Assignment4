import sqlite3

connection = sqlite3.connect('database.db')
with open('config.txt', 'r') as file:
    config = file.readlines()
firstLine = config[0].split(',')
configNumOfEntries = firstLine[0]
configNumOfSuppliers = firstLine[1]


