from math import ceil
width = float(input("Wall width in meters: "))
height = float(input("Wall height in meters: "))
print(f"Its wall has the dimension of {width}x{height} and its area is {width*height}m2.")
print(f"To paint this wall, you'll need {ceil((width*height)/2)}l of paint.")