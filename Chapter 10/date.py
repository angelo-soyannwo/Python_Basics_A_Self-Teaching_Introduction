

class date:
	def getData(self):
		self.day = input('Please enter the day: ')
		self.month = input('Please enter the month: ')
		self.year = input('Please enter the year: ')

	def putData(self):
		print(self.day)
		print(self.month)
		print(self.year)

def main():
	day = date()
	day.getData()
	day.putData()


if __name__ == '__main__':
	main()
