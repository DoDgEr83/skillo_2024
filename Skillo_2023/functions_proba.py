import math


def area_square(a):
    result = 0
    result = a * a
    return result


def area_rectangle(a, b):
    result = 0
    result = a * b
    return result


def area_triangle(a, b, c):
    result = 0
    s = (a + b + c) / 2
    result = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return result


def area_circle(r):
    result = 0
    result = 3.14 * (r * r)
    return result


# Za poslednata zadacha s shoping karts
def print_customer_info(customers, customer_id):
    if customer_id in customers:
        print("For customer ", customer_id, ":", customers[customer_id])
    else:
        print("Customer not found.")


def calculate_total_price(customers, customer_id):
    if customer_id in customers:
        print("Total Price for customer ", customer_id, "is :", sum(customers[customer_id].values()))
    else:
        print("Customer not found.")


def add_item_to_card(customers, customer_id, item_1, value_1):
    if customer_id in customers:
        customers[customer_id][item_1] = value_1
        print(f"You add {item_1} with value {value_1}")
    else:
        print("Customer not found.")


def remove_item_from_card(customers, customer_id, item_1):
    if customer_id in customers and item_1 in customers[customer_id]:
        customers[customer_id].pop(item_1)
        print(f"You remove {item_1}")
    else:
        print("Customer not found.")

