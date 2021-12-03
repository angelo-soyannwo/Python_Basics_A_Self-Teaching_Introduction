from math import sqrt, acos

def calculate_angle(a, b, c):
	length1 = check_length(a,b)
	length2 = check_length(a,c)
	length3 = check_length(c,b)
	
	angle_1 = acos((length2**2 + length3**2 - length1**2)/(2*length3*length2))
	angle_2 = acos((length1**2 + length3**2 - length2**2)/(2*length3*length1))
	angle_3 = acos((length2**2 + length1**2 - length3**2)/(2*length1*length2))

	print('angle one is: ' + str(angle_1))
	print('angle two is: ' + str(angle_2))
	print('angle three is: ' + str(angle_3))


m1 = 0
m2 = 0

point1 = input("enter x and y coordinates in the form x,y: ")
point2 = input("enter x and y coordinates in the form x,y: ")
point3 = input("enter x and y coordinates in the form x,y: ")

point1 = tuple(map(int, point1.split(',')))
point2 = tuple(map(int, point2.split(',')))
point3 = tuple(map(int, point3.split(',')))

if point2[0] != point1[0]:
    m1 = (point2[1] - point1[1])/(point2[0] - point1[0])
else: 
    m1 == 'infinite gradient' 

if point3[0] != point2[0]:
    m2 = (point3[1] - point2[1])/(point3[0] - point2[0])
else:
    m2 = 'infinite gradient'

def check_length(a, b):
    length = sqrt((a[1]-b[1])**2 + (a[0]-b[0])**2)
    return length

length_1 = check_length(point2, point1)
length_2 = check_length(point3, point2)
length_3 = check_length(point3, point1)

print("length 1: " + str(length_1))
print("length 2: " + str(length_2))
print("length 3: " + str(length_3))

def check_type_of_triangle(a, b, c):
    triangle_type = ''
    length1 = 0
    lenght2 = 0
    length3 = 0

    lenght1 = check_length(a, b)
    length2 = check_length(c, b)
    length3 = check_length(c, a)

    if length1 == length_2 == length3:
        triangle_type = 'Equilateral'

    elif (lenght1 == length2 != length3) or (lenght1 == length3 != length2) or (length3 == length2 != lenght1):
        triangle_type = "Isoscelese"

    else:
        triangle_type = 'Scalene'

    return triangle_type

def check_if_right_angled(a, b, c):
	x1 = check_length(a, b)
	x2 = check_length(a, c)
	x3 = check_length(c, b)
	triangle_sides = [x1, x2, x3]
	longest_side = max(x1, x2, x3)

	smaller_sides = [triangle_sides[i] for i in range(0, len(triangle_sides)) if triangle_sides[i] != longest_side]

	pythagorean_check = longest_side**2 - (smaller_sides[0]**2 + smaller_sides[1]**2)
	
	if pythagorean_check < 0.000001:
		print('The triangle is right angled')
	else:
		print('The triangle is not right angled')

if type(m1) == type(m2) and m1 == m2:
    print("The points are collinear")
else:
    print("The points are not collinear")
    print(check_type_of_triangle(point1, point2, point3))
    check_if_right_angled(point1, point2, point3)
    calculate_angle(point1,point2, point3)
