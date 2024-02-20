from classes.Challenge import Challenge
from utils.distance import distance
from utils.sorting_drones import sort_by_turns


def naive(challenge: Challenge):
    necessary_products = [0 for i in range(challenge.product_types)]
    score = 0
    count = 0
    for order in challenge.orders:
        for i in range(challenge.product_types):
            necessary_products[i] += order.order_products[i]

    while not all(order.is_deliver for order in challenge.orders):

        for warehouse in challenge.warehouses:

            if sum(warehouse.warehouse_products) == 0:
                continue

            drones_sorted_by_turns = sorted(challenge.drones, key=sort_by_turns)

            for drone in drones_sorted_by_turns:

                if drone.location != warehouse.location:

                    if sum(drone.current_load) > 0:
                        orders_between = list()
                        dist_to_next_warehouse = distance(drone.location, warehouse.location)

                        for order in challenge.orders:
                            if distance(drone.location, order.location) < dist_to_next_warehouse:
                                orders_between.append(order)

                        for order in orders_between:
                            drone.fly(order.location)
                            drone.deliver(order)

                            if order.is_deliver:
                                score += ((challenge.max_turns - drone.turns) / challenge.max_turns) * 100
                                orders_between.remove(order)
                                count += 1
                                print(drone.turns, count)

                    drone.fly(warehouse.location)

                for i in range(challenge.product_types):
                    if necessary_products[i] == 0:
                        continue

                    if warehouse.warehouse_products[i] == 0:
                        continue

                    if drone.load(warehouse, challenge, i, necessary_products[i]):
                        necessary_products[i] -= drone.current_load[i]

        for order in challenge.orders:
            for drone in challenge.drones:
                if not order.is_deliver:

                    if sum(drone.current_load) == 0:
                        continue

                    for i in range(challenge.product_types):
                        if drone.current_load[i] >= order.order_products[i] != 0:
                            drone.fly(order.location)
                            drone.deliver(order)

                        if order.is_deliver:
                            score += ((challenge.max_turns - drone.turns) / challenge.max_turns) * 100
                            count += 1
                            print(drone.turns, count)
                            break

        print(score)
