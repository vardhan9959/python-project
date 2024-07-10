def calculate_rectangle_area(length,width):
    return length*width
def calculate_rectangle_perimeter(length,width):
    return 2*(length+width)
length = 3
width = 6
area=calculate_rectangle_area(length,width)
perimeter=calculate_rectangle_perimeter(length,width)
print(f"The area of rectangle : {area}")
print(f"The perimeter of rectangle : {perimeter}")