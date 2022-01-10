import atexit
import sqlite3

from Hats import Hats
from Orders import Orders
from Suppliers import Suppliers
import os


class Repository:

    def __init__(self):
        if os.path.exists('database.db'):
            os.remove('database.db')
        self.connection = sqlite3.connect('database.db')
        self.hats = Hats(self.connection)
        self.suppliers = Suppliers(self.connection)
        self.orders = Orders(self.connection)

    def close(self):
        self.connection.commit()
        self.connection.close()

    def create_tables(self):
        self.connection.executescript("""
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


repo = Repository()
atexit.register(repo.close)
