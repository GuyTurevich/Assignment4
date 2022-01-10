import atexit
import sqlite3


class PersistenceLayer:

    def __init__(self):
        self.connection = sqlite3.connect('database.db')

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


psl = PersistenceLayer()
atexit.register(psl.close)
