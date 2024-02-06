from classes.Drone import Drone
from classes.Warehouse import Warehouse
from utils.parser import parse


def load_test():
    drone = Drone(0, (1, 1), [0, 0, 0])
    warehouse = Warehouse(0, (0, 0), [5, 1, 0])
    file_path = 'C:\\Users\\auffretb\Documents\GoogleHashCode2016\challenges\\a_example.in'
    challenge = parse(file_path)
    print(drone.load(warehouse, challenge, 0, 3))
    print(drone.current_load, warehouse.warehouse_products)


def unload_test():
    drone = Drone(0, (1, 1), [5, 1, 0])
    warehouse = Warehouse(0, (0, 0), [0, 1, 0])
    print(drone.unload(warehouse, 0, 5))
    print(drone.current_load, warehouse.warehouse_products)


