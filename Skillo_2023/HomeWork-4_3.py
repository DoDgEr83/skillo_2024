import functions_proba as fp

print("Enter square size:")
square_a = int(input())
print("The area of square is : ", fp.area_square(square_a))
print()

print("Enter rectangle side one size:")
rectangle_a = int(input())
print("Enter rectangle side two size:")
rectangle_b = int(input())
print("The area of rectangle is : ", fp.area_rectangle(rectangle_a, rectangle_b))
print()

print("Enter triangle side one size:")
triangle_a = int(input())
print("Enter triangle side two size:")
triangle_b = int(input())
print("Enter triangle side three size:")
triangle_c = int(input())
print("The area of rectangle is : ", fp.area_triangle(triangle_a, triangle_b, triangle_c))
print()

print("Enter circle radius size:")
radius = int(input())
print("The area of circle is : ", fp.area_circle(radius))
