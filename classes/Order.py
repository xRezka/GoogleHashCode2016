class Order:
    def __init__(self, order_id: int, location: tuple, order_products: list[int]):
        self.order_id = order_id
        self.location = location
        self.order_products = order_products
        self.is_deliver = False

    def __str__(self):
        return f"Order {self.order_id} at {self.location} with {self.order_products} deliver {self.is_deliver}"
