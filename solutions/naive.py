from classes.Challenge import Challenge
from utils.parser import parse


def naive(challenge: Challenge):
    all_prodcuts = [0 for i in range(challenge.product_types)]
    for order in challenge.orders:
        for i in range(len(order.order_products)):
            all_prodcuts[i] += order.order_products[i]

    for warehouse in challenge.warehouses:
        for drone in challenge.drones:
            for i in range(len(all_prodcuts)):
                if drone.load(warehouse, challenge, i, all_prodcuts[i]) and all_prodcuts[i] != 0:
                    all_prodcuts[i] -= drone.current_load[i]
            drone.fly(challenge.warehouses[1].location)

    for order in challenge.orders:
        for drone in challenge.drones:
            drone.fly(order.location)
            drone.deliver(order)


file_path = 'C:\\Users\\auffretb\Documents\GoogleHashCode2016\challenges\\a_example.in'
challenge = parse(file_path)
print(naive(challenge))
