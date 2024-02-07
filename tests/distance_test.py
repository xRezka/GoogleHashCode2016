from classes.Drone import Drone
from classes.Order import Order
from utils.distance import distance


def distance_test():
    drone = Drone(0, (1, 1), [5, 1, 0])
    order = Order(0, (3, 3), [1, 1, 0])
    distance(drone.location, order.location)
