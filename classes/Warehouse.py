class Warehouse:
    def __init__(self, warehouse_id: int, location: tuple, warehouse_products: list[int]):
        self.warehouse_id = warehouse_id
        self.location = location
        self.warehouse_products = warehouse_products

    def __str__(self):
        return f"Warehouse {self.warehouse_id} at {self.location} with {self.warehouse_products}"
