from classes.Drone import Drone
from classes.Warehouse import Warehouse
from classes.Order import Order
from utils.parser import parse


def load_test():
    file_path = 'C:\\Users\\auffretb\Documents\GoogleHashCode2016\challenges\\a_example.in'
    parse(file_path)


def deliver_test():
    drone = Drone(0, (1, 1), [3, 1, 0])
    order = Order(0, (1, 1), [1, 1, 0])
    drone.deliver(order)


def unload_test():
    drone = Drone(0, (1, 1), [5, 1, 0])
    warehouse = Warehouse(0, (0, 0), [0, 1, 0])
    drone.unload(warehouse, 0, 5)


def fly_test():
    drone = Drone(0, (1, 1), [5, 1, 0])
    order = Order(0, (3, 3), [1, 1, 0])
    drone.fly(order.location)
