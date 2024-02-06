class Warehouse:
    def __init__(self, id: int, location: tuple, warehouse_products: list[int]):
        self.id = id
        self.location = location
        self.warehouse_products = warehouse_products

    def __str__(self):
        return (f"Id: {self.id}\nLocation: {self.location}\nWarehouse products: {self.warehouse_products}")