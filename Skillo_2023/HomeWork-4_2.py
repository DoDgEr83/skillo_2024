def simple_calculator(x, y, sign):
    result = 0
    if sign == "+":
        result = x + y
    elif sign == "-":
        result = x - y
    elif sign == "*":
        result = x * y
    elif sign == "/":
        result = x / y
    return result


# x = 5
# y = 6
# sing = "+"

x = int(input())
y = int(input())
sing = input()

if sing != "+" and sing != "-" and sing != "*" and sing != "/":
    print("Wrong sing")
    exit()

print(simple_calculator(x, y, sing))
