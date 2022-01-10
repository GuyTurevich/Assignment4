class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Suppliers:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, supplierDTO):
        self.connection.execute("""
        INSERT INTO suppliers (id, name)
        VALUES(?, ?)      
        """, [supplierDTO.id, supplierDTO.name])

    def get_supplier(self, supplier_id):
        cursor = self.connection.cursor()
        cursor.execute("""
                SELECT name FROM suppliers WHERE id = ?
                """, [supplier_id])
        supplier = cursor.fetchone()
        return supplier
