# rectangle_area.py

import math

# Get input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Use abs to ensure positive dimensions
length = abs(length)
width = abs(width)

# Calculate rectangle area
area = length * width

# Square example: square the average of length and width
avg_side = (length + width) / 2
square_area = math.pow(avg_side, 2)

# Round the results to 2 decimal places
area_rounded = round(area, 2)
square_area_rounded = round(square_area, 2)

# Print results
print("Rounded Area of Rectangle:", area_rounded)
print("Rounded Square Area from Avg Side:", square_area_rounded)
