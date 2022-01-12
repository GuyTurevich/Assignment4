import atexit
import sqlite3
from DAO import Suppliers, Hats, Orders
import sys

from DTO import Supplier, Hat, Order


class Repository:
    def __init__(self):
        self.connection = sqlite3.connect(sys.argv[4])
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

    def read_config(self, config):
        first_line = config[0].split(',')
        config_num_of_entries = int(first_line[0])

        for i in range(config_num_of_entries + 1, len(config)):
            entry = config[i].rstrip("\n").split(',')
            supplier = Supplier(entry[0], entry[1])
            self.suppliers.insert(supplier)

        for i in range(1, config_num_of_entries + 1):
            entry = config[i].rstrip("\n").split(',')
            hat = Hat(entry[0], entry[1], entry[2], entry[3])
            self.hats.insert(hat)

    def execute_orders(self, orders):
        summary = ""
        for i in range(len(orders)):
            entry = orders[i].rstrip("\n").split(',')
            location = entry[0]
            topping = entry[1]
            order = Order(i + 1, location, self.hats.find(topping))
            self.orders.insert(order)
            supplier = self.suppliers.find(self.hats.get_supplier_id(order.hat))
            summary += topping + "," + supplier[0] + "," + location + "\n"
            self.hats.check_quantity(order.hat)
        return summary


repo = Repository()
atexit.register(repo.close)
