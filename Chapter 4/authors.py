
continue_v = "True"

def check_continue(a):
	global continue_v	
	if a == 'y':
		continue_v = "True"
		return  
	elif a == 'n':
		continue_v = "False"
		return
	else:
		a = input("Do you want to add more authors ('y'/'n'):\t")

	return check_continue(a)


books = []
while continue_v == "True":

	book = input("Enter the name of the book:\t") 
	publisher = input("Enter the name of the publisher:\t")
	year = input("Enter the year:\t")
	ISSN = input("Enter the ISSN:\t")
	city = input("Enter the city:\t")

	temp = [book, publisher, year, ISSN, city]
	
	books.append(temp)
	x = input("Do you want to add more authors ('y'/'n'):\t")
	check_continue(x)	
