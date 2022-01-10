import sqlite3

connection = sqlite3.connect('database.db')
with open('config.txt', 'r') as file:
    config = file.readlines()
firstLine = config[0].split(',')
configNumOfEntries = firstLine[0]
configNumOfSuppliers = firstLine[1]


def createTables():
    connection.executescript("""
    CREATE TABLE suppliers (
    id      INT   PRIMARY KEY,
    name    TEXT   NOT NULL 
    );
    
    CREATE TABLE hats (
    id        INT     PRIMARY KEY,
    topping   TEXT    NOT NULL,
    supplier  INT             ,
    quantity  INT     NOT NULL,
    FOREIGN KEY(supplier)    REFERENCES suppliers(id)
    ); 
    
    CREATE TABLE orders (
    id          INT     PRIMARY KEY,
    location    TEXT    NOT NULL,
    hat         INT             ,
    FOREIGN KEY(hat)    REFERENCES hats(id)
    );
    """)

