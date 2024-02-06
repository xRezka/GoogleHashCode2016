from classes.Warehouse import Warehouse
from utils.products import weight


class Drone:

    def __init__(self, drone_id: int, location: tuple, current_load: list[int]):
        self.drone_id = drone_id
        self.location = location
        self.current_load = current_load

    def __str__(self):
        return (f"Id: : {self.drone_id}\nLocation: {self.location}"
                f"\nCurrent load: {self.current_load}")

    def load(self, warehouse: Warehouse, challenge, product_type: int, quantity: int):
        if weight(self.current_load, challenge.product_weights) <= challenge.max_load:
            if warehouse.warehouse_products[product_type] >= quantity:
                self.current_load[product_type] += quantity
                warehouse.warehouse_products[product_type] -= quantity
                return True

            elif (quantity >= warehouse.warehouse_products[product_type]) and (
                    warehouse.warehouse_products[product_type] > 0):
                self.current_load[product_type] += warehouse.warehouse_products[product_type]
                warehouse.warehouse_products[product_type] -= warehouse.warehouse_products[product_type]

            else:
                print('Warehouse doesn\'t have enought products of this type !')

        else:
            print('Drone cannot load !')

    def deliver(self):
        pass

    def unload(self, warehouse: Warehouse, product_type: int, quantity: int):
        if self.current_load[product_type] >= quantity:
            self.current_load[product_type] -= quantity
            warehouse.warehouse_products[product_type] += quantity
            return True
        elif (quantity >= self.current_load[product_type]) and (self.current_load[product_type] > 0):
            self.current_load[product_type] -= self.current_load[product_type]
            warehouse.warehouse_products[product_type] += self.current_load[product_type]
        else:
            print('Drone doesn\'t currently have this product')

    def wait(self):
        pass

    def fly(self):
        pass
