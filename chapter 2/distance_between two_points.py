from math import sqrt

x1 = int(input("Please enter the first x coordinate: "))
y1 = int(input("Please enter the first y coordinate: "))

x2 = int(input("Please enter the second x coordinate: "))
y2 = int(input("Please enter the second y coordinate: "))

distance = sqrt((x2 -x1)**2 + (y2 - y1)**2)

print(distance)