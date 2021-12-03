

from math import sqrt, atan

point1  = input("enter your coordinate in the form x,y: ")
point2  = input("enter your coordinate in the form x,y: ")

point1 = tuple(map(int, point1.split(',')))

point2 = tuple(map(int, point2.split(','))) 

def distance_to_the_origin(a):
	distance = sqrt(a[0]**2 + a[1]**2)
	return distance

def are_points_equidistant_to_origin(point1, point2):

	distance1 = distance_to_the_origin(point1)
	distance2 = distance_to_the_origin(point2)

	if distance1 == distance2:
		print("the points are the same distance from the origin")
	else:
		print("the points are not the same distance from the origin")

def x_distance(point1, point2):
	Xdistance = sqrt(point1[0]**2 + point2[0]**2)
	return Xdistance

def y_distance(point1, point2):
	Ydistance = sqrt(point1[1]**2 + point2[1]**2)
	return Ydistance

def angle_to_the_origin(point1, point2):
	y = y_distance(point1, point2)
	x = x_distance(point1, point2)
	angle = atan(y/x)
	return angle

are_points_equidistant_to_origin(point1, point2)
print(angle_to_the_origin(point1, point2))
