class Order:
    def __init__(self, order_id: int, location: tuple, order_products: list[int]):
        self.order_id = order_id
        self.location = location
        self.order_products = order_products
        self.deliver = False

    def __str__(self):
        return (f"Id: {self.order_id}\nLocation: {self.location}\nOrder products: {self.order_products}"
                f"Deliver: {self.deliver}")
