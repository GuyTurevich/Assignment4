from Hats import Hat, Hats
from Orders import Order, Orders
from Repository import repo
from Suppliers import Supplier, Suppliers

with open('config.txt', 'r') as file:
    config = file.readlines()
firstLine = config[0].split(',')
configNumOfEntries = int(firstLine[0])
configNumOfSuppliers = int(firstLine[1])
repo.create_tables()
Hats(repo.connection)
Suppliers(repo.connection)
Orders(repo.connection)
summary = ""

for i in range(configNumOfEntries + 1, len(config)):
    entry = config[i].rstrip("\n").split(',')
    supplier = Supplier(entry[0], entry[1])
    repo.suppliers.insert(supplier)

for i in range(1, configNumOfEntries + 1):
    entry = config[i].rstrip("\n").split(',')
    hat = Hat(entry[0], entry[1], entry[2], entry[3])
    repo.hats.insert(hat)

with open('orders.txt', 'r') as file:
    orders = file.readlines()

for i in range(len(orders)):
    entry = orders[i].rstrip("\n").split(',')
    location = entry[0]
    topping = entry[1]
    order = Order(i+1, location, repo.hats.get_hat_id(topping))
    repo.orders.insert(order)
    supplier = repo.suppliers.get_supplier(repo.hats.get_supplier_id(order.hat))
    summary += topping + "," + supplier + "," + location + "\n"
    repo.hats.check_quantity(order.hat)

with open('summary.txt', 'w') as file:
    file.write(summary)
