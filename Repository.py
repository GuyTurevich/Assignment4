import atexit
import sqlite3


class Repository:

    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.students = Hats(self.connection)
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

    def insert_hat(self, id, topping, supplier, quantity):
        self.connection.execute("""
        INSERT INTO hats (id, topping, supplier, quantity)
        VALUES(?, ?, ?, ?)      
        """, [id, topping, supplier, quantity])

    def insert_supplier(self, id, name):
        self.connection.execute("""
        INSERT INTO suppliers (id, name)
        VALUES(?, ?)      
        """, [id, name])

    def insert_order(self, id, location, hat):
        self.connection.execute("""
        INSERT INTO orders (id, location, hat)
        VALUES(?, ?, ?)      
        """, [id, location, hat])

repo = Repository()
atexit.register(repo.close)
