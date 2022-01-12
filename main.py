from Repository import repo
import sys


repo.create_tables()

with open(sys.argv[1], 'r') as config_file:
    config = config_file.readlines()
repo.read_config(config)

with open(sys.argv[2], 'r') as orders_file:
    orders = orders_file.readlines()
summary = repo.execute_orders(orders)

with open(sys.argv[3], 'w') as output_file:
    output_file.write(summary)
