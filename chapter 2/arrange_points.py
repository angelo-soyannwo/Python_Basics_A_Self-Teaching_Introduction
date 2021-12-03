from math import sqrt

point1 = input("enter point 1 coordinates in the form x,y: ")
point2 = input("enter point 2 coordinates in the form x,y: ") 
point3 = input("enter point 3 coordinates in the form x,y: ") 
point4 = input("enter point 4 coordinates in the form x,y: ")

point1 = tuple(map(int, point1.split(',')))
point2 = tuple(map(int, point2.split(',')))
point3 = tuple(map(int, point3.split(','))) 
point4 = tuple(map(int, point4.split(','))) 

points = [point1, point2, point3, point4]

def distance_to_origin(point):
	distance = sqrt(point[0]**2 + point[1]**2)
	return distance

def arrange(array):
        for i in range(0, len(array)):
                j = i + 1
                for j in range(j, len(array)):
                        if array[i][0] > array[j][0]:
                                temp = array[i]
                                array[i] = array[j]
                                array[j] = temp

        return array


print(arrange(points))
