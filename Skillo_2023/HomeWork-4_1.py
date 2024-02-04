def sum_elements(arr):
    result = 0
    if len(arr) == 0:
        print("Empty arr")
        exit(0)
    for elements in arr:
        # print("elem", elements)
        result = elements + result
    return result


test_element = [1, 2, 3, 4]
# test_element = [0]
# test_element = []
# test_element = [-1 , 1]

print(sum_elements(test_element))
