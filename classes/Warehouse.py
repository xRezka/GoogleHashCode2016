class Warehouse:
    def __init__(self, warehouse_id: int, location: tuple, warehouse_products: list[int]):
        self.warehouse_id = warehouse_id
        self.location = location
        self.warehouse_products = warehouse_products

    def __str__(self):
        return (f"Id: {self.warehouse_id}\nLocation: {self.location}"
                f"\nWarehouse products: {self.warehouse_products}")
