def weight(product_quantity: list[int], products_weights: list[int]):
    total_weight = 0
    for i in range(len(products_weights)):
        total_weight += product_quantity[i] * products_weights[i]
    return total_weight
