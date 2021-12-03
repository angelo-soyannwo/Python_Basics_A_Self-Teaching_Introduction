from math import acos

from Check_if_points_are_collinear import check_length

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

