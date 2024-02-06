class Order:
    def __init__(self, id: int, location: tuple, order_products: list[int]):
        self.id = id
        self.location = location
        self.order_products = order_products

    def __str__(self):
        return (f"Id: {self.id}\nLocation: {self.location}\nOrder products: {self.order_products}")
