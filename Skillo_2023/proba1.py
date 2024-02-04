# HW - 5 - 1-4

# my_list = list(range(1, 10+1))
# print(my_list)
# # my_list.reverse()
# # print(my_list)
#
#
# def sum_even_list(my_list_1):
#     result = 0
#     for proba in my_list:
#         if proba %2 == 0:
#             result = result + proba
#     return result
#
#
# print("Total sum of even is : ", sum_even_list(my_list))

###################################################################
# HW - 5 - 5

# my_tuple_1 = (9, -6, 7, 1, 2, 3, 4, 5, 6, 7, 8)
# my_max = my_tuple_1[0]
# my_min = my_tuple_1[0]
# for num in my_tuple_1:
#     if num > my_max:
#         my_max = num
#     elif num <= my_min:
#         my_min = num
# print(f"The max number in tuple is : {my_max}")
# print(f"The min number in tuple is : {my_min}")

###################################################################
# HW - 5 - 6

# # Global variable representing the queue
# my_queue = []
#
#
# def enqueue(item):
#     # Add item to the end of the queue
#     my_queue.append(item)
#     print(f"Enqueued: {item}")
#
#
# def dequeue():
#     if my_queue:
#         # Remove and return the item from the front of the queue
#         item = my_queue.pop(0)
#         print(f"Dequeued: {item}")
#         return item
#     else:
#         print("Queue is empty")
#
#
# # Example usage:
# enqueue(10)
# enqueue(20)
# enqueue(3)
# print(my_queue)
# dequeue()
# dequeue()
# dequeue()
# dequeue()  # Trying to dequeue from an empty queue

##########################################################
# HW - 5 - 7

# # Dictionary mapping students to their bank account numbers
# students_accounts = {
#     "Student1": ["123456789", "987654321"],
#     "Student2": ["456789123"],
#     "Student3": ["111223344", "554433221"]
# }
#
# # Example usage:
# # Adding a new bank account for Student1
# students_accounts["Student1"].append("555555555")
# # Delite a bank acc for St1
# students_accounts["Student1"].pop(0)
#
# # Printing the dictionary
# for student, accounts in students_accounts.items():
#     print(f"{student}'s bank accounts: {', '.join(accounts)}")

############################################################################
# HW - 5 - 9

def count_word_frequency(text_1):
    words = input_text.split()
    my_word_freq = {}
    for word in words:
        my_word_freq[word] = my_word_freq.get(word, 0)
        for key in my_word_freq:
            if key == word:
                my_word_freq.update({word: my_word_freq[word] + 1})

        # print(my_word_freq.keys())
    # print("Pr1", my_word_freq)
    return my_word_freq

input_text = "apple banana orange apple banana apple"
print("The count is : ", count_word_frequency(input_text))

