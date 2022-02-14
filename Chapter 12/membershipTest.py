


class Lists:
	def __init__(self):
		self.cars = ["Double R", "Ferrari", "Tesla"]
		self.houses = ["Banana Island", "London", "New york"]
		self.places = [1, 2, 3]
		self.classLists = [self.cars, self.houses, self.places]
	def __contains__(self, value):
		if value in self.classLists[1] or value in self.classLists[2] or value in self.classLists[3]:
			return True
		else:
			return False
		

def main():
	a = Lists()
	print(1 in a)

if __name__ == '__main__':
	main()
