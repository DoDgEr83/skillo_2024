import functions_proba as fp

customers = {
    "1_1":
        {
            "milk": 4,
            "eggs": 6
        },

    "1_2":
        {
            "bananas": 2,
            "meat": 15
        }

}

while True:
    print("Enter ID:")
    ID_number = input()
    if ID_number not in customers:
        print("Wrong ID !\n")
        print(f"choose between{customers.keys()}")
    else:
        break

fp.print_customer_info(customers, ID_number)
fp.calculate_total_price(customers, ID_number)
print("Witch item do you want to add: ")
item_a1 = input()
print("What's the value of the item:")
item_a2 = input()
fp.add_item_to_card(customers, ID_number, item_a1, item_a2)
fp.print_customer_info(customers, ID_number)
print("Witch item do you want to remove:")
item_r = input()
fp.remove_item_from_card(customers, ID_number, item_r)
fp.print_customer_info(customers, ID_number)


