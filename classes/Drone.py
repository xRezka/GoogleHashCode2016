from classes.Warehouse import Warehouse
from classes.Order import Order
from utils.products import weight
from utils.distance import distance


class Drone:

    def __init__(self, drone_id: int, location: tuple, current_load: list[int]):
        self.drone_id = drone_id
        self.location = location
        self.current_load = current_load
        self.turns = 0
        self.available = True

    def __str__(self):
        return f"Drone {self.drone_id} at {self.location} with {self.current_load}"

    def load(self, warehouse: Warehouse, challenge, product_type: int, quantity: int):
        if self.location == warehouse.location:
            drone_weight = weight(self.current_load, challenge.product_weights)
            if drone_weight <= challenge.max_load:

                if (drone_weight + quantity * challenge.product_weights[product_type]) <= challenge.max_load and (
                        drone_weight + quantity * challenge.product_weights[product_type]) != 0 and (
                        quantity * challenge.product_weights[product_type]) != 0:
                    self.current_load[product_type] += quantity
                    warehouse.warehouse_products[product_type] -= quantity
                    return True

                else:
                    max_possible_quantity = (challenge.max_load - drone_weight) // challenge.product_weights[
                        product_type]
                    if 0 < max_possible_quantity <= warehouse.warehouse_products[product_type]:

                        self.current_load[product_type] += max_possible_quantity
                        warehouse.warehouse_products[product_type] -= max_possible_quantity
                        return True
                    else:
                        print("Drone cannot load this product because the product isn't in warehouse !")
            else:
                print("The maximum load of the drone has been exceeded.")
        else:
            print("Drone cannot load he doesn't have the same location as warehouse !")

    def deliver(self, order: Order):
        for i in range(len(self.current_load)):
            if self.current_load[i] > 0 and order.order_products[i] > 0 and (
                    self.current_load[i] >= order.order_products[i]):

                self.current_load[i] -= order.order_products[i]
                order.order_products[i] -= order.order_products[i]
                self.turns += 1

            else:
                continue

        if sum(order.order_products) == 0:
            order.deliver = True
        return True

    def unload(self, warehouse: Warehouse, product_type: int, quantity: int):
        if self.current_load[product_type] >= quantity:
            self.current_load[product_type] -= quantity
            warehouse.warehouse_products[product_type] += quantity
            self.turns += 1
            return True

        elif (quantity >= self.current_load[product_type]) and (self.current_load[product_type] > 0):
            self.current_load[product_type] -= self.current_load[product_type]
            warehouse.warehouse_products[product_type] += self.current_load[product_type]
            self.turns += 1

        else:
            print('Drone doesn\'t currently have this product')

    def wait(self, nb_turns: int):
        while self.turns <= (self.turns + nb_turns):
            self.available = False
            self.turns += 1
        self.available = True
        return self.turns

    def fly(self, destination: tuple):
        self.turns += distance(self.location, destination)
        self.location = destination
        return self.location, self.turns
