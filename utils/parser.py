from classes.Challenge import Challenge


def parse(filename: str) -> Challenge:
    """
    Read input file data set to extract challenge information
    """
    with open(filename, 'r') as file:
        nb_rows, nb_columns, nb_drones, max_turns, max_load = map(int, file.readline().split())
        product_types = int(file.readline())
        product_weights = list(map(int, file.readline().split()))
        nb_warehouses = int(file.readline())

    challenge = Challenge(nb_rows, nb_columns, nb_drones, max_turns, max_load, product_types, product_weights,
                          nb_warehouses)

    return challenge


file_path = 'C:\\Users\\auffretb\Documents\GoogleHashCode2016\challenges\\a_example.in'
print(parse(file_path))
