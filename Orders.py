class Order:
    def __init__(self, id, location, hat):
        self.id = id
        self.location = location
        self.hat = hat


class Orders:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, orderDTO):
        self.connection.execute("""
        INSERT INTO orders (id, location, hat)
        VALUES(?, ?, ?)      
        """, [orderDTO.id, orderDTO.location, orderDTO.hat])
