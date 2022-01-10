class Hat:

    def __init__(self, id, topping, supplier, quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Hats:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, hatDTO):
        self.connection.execute("""
        INSERT INTO hats (id, topping, supplier, quantity)
        VALUES(?, ?, ?, ?)      
        """, [hatDTO.id, hatDTO.topping, hatDTO.supplier, hatDTO.quantity])
