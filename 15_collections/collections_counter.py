def solution():
    n_shoes = 10
    list_shoe_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18, ]
    n_customers = 6
    shoe_size_and_price = [{6: 55}, {6: 45}, {6: 55}, {4: 40}, {18: 60}, {10: 50}]
    total = 0

    for sz_and_price in shoe_size_and_price:
        shoe_size = list(sz_and_price.keys())[0]
        price = list(sz_and_price.values())[0]
        if shoe_size in list_shoe_sizes:
            total += price
            list_shoe_sizes.remove(shoe_size)
    return print(total)
