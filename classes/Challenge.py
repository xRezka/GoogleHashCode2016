from classes.Warehouse import Warehouse
from classes.Order import Order
from classes.Drone import Drone


class Challenge:
    def __init__(self, grid: tuple, nb_drones: int, max_turns: int,
                 max_load: int, product_types: int, product_weights: list[int], nb_warehouses: int,
                 warehouses: list[Warehouse], nb_orders: int, orders: list[Order], drones: list[Drone]):

        self.grid = grid
        self.nb_drones = nb_drones
        self.max_turns = max_turns
        self.max_load = max_load
        self.product_types = product_types
        self.product_weights = product_weights
        self.nb_warehouses = nb_warehouses
        self.warehouses = warehouses
        self.nb_orders = nb_orders
        self.orders = orders
        self.drones = drones

    def __str__(self):
        return (f"Grid size: {self.grid}"f"\nNumber of drones: {self.nb_drones}\nNumber of turns: {self.max_turns}"
                f"\nMaximum load: {self.max_load}\nNumber of product types: {self.product_types}"
                f"\nWeight of each product types are: {self.product_weights}"
                f"\nNumber of warehouses: {self.nb_warehouses}"
                f"\nList of warehouses: {self.warehouses}\nNumber of orders: {self.nb_orders}"
                f"\nList of orders: {self.orders}\nList of drones: {self.drones}")
