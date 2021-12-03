
m = int(input("Please enter the mass of the rotating object: "))
r = int(input("Please enter the radius of the rotating object's path: "))
v = int(input("Please enter the linear velocity of the rotating object: "))

G = 6.67 * (10**-11)
M = 5.972 * 10**24
R = 6371000

if (G * M * m)/R == (m*v**2)/r:
	print("Centripetal force is equal to the weight of the object at the surface of the earth.")
else:
	print("Centripetal force is not equal to the weight of the object at the surface of the earth.")
 
