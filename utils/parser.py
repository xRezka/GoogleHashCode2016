from classes.Challenge import Challenge
from classes.Warehouse import Warehouse
from classes.Order import Order


def parse(filename: str) -> Challenge:
    """
    Read input file data set to extract challenge information
    """
    with open(filename, 'r') as file:
        nb_rows, nb_columns, nb_drones, max_turns, max_load = map(int, file.readline().split())
        product_types = int(file.readline())
        product_weights = list(map(int, file.readline().split()))
        nb_warehouses = int(file.readline())

        warehouses = list()
        for i in range(nb_warehouses):
            id = i
            location = tuple(map(int, file.readline().split()))
            warehouse_products = list(map(int, file.readline().split()))
            warehouses.append(Warehouse(id, location, warehouse_products))

        nb_orders = int(file.readline())

        orders = list()
        for i in range(nb_orders):
            order_products = [0 for i in range(product_types)]
            id = i
            location = tuple(map(int, file.readline().split()))
            nb_products_in_order = int(file.readline())

            for i in range(nb_products_in_order):
                order_products.append()
            order_products = list(map(int, file.readline().split()))
            orders.append(Order(id, location, order_products))

    challenge = Challenge(nb_rows, nb_columns, nb_drones, max_turns, max_load, product_types, product_weights,
                          nb_warehouses, warehouses, orders)

    return challenge


file_path = 'D:\Projects\GoogleHashCode2016\challenges\\a_example.in'
print(parse(file_path))
