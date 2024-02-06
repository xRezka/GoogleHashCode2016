from classes.Challenge import Challenge
from classes.Warehouse import Warehouse
from classes.Order import Order


def parse(filename: str) -> Challenge:
    """
    Read input file data set to extract challenge information.
    """
    with open(filename, 'r') as file:
        first_line = file.readline().split()
        grid = tuple(map(int, first_line[:2]))
        nb_drones, max_turns, max_load = map(int, first_line[2:])

        product_types = int(file.readline())
        product_weights = list(map(int, file.readline().split()))
        nb_warehouses = int(file.readline())

        warehouses = list()
        for i in range(nb_warehouses):
            warehouse_id = i
            location = tuple(map(int, file.readline().split()))
            warehouse_products = list(map(int, file.readline().split()))
            warehouses.append(Warehouse(warehouse_id, location, warehouse_products))

        nb_orders = int(file.readline())

        orders = list()
        for i in range(nb_orders):
            order_products = [0 for i in range(product_types)]
            order_id = i
            location = tuple(map(int, file.readline().split()))

            nb_products_in_order = int(file.readline())
            product_types_in_order = list(map(int, file.readline().split()))

            for i in range(nb_products_in_order):
                value = product_types_in_order[i]
                order_products[value] += 1

            orders.append(Order(order_id, location, order_products))

    challenge = Challenge(grid, nb_drones, max_turns, max_load, product_types, product_weights,
                          nb_warehouses, warehouses, nb_orders, orders)

    return challenge
