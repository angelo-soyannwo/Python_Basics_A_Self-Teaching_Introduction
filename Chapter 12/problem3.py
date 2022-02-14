class Distance:
	def getdata(self):
		self.meters = int(input("Enter the meters component of the length: "))
		self.centimeters =  int(input("Enter the centimeters component of the length: "))
		if self.centimeters > 100:
			self.meters += self.centimeters // 100
			self.centimeters = self.centimeters % 100

	def putdata(self):
		txt = "The length is {meters:d} meters and {cm:.2f} cm"
		print(txt.format(meters = self.meters, cm=self.centimeters))

	def __add__(self, other):
		result = Distance()
		result.meters = self.meters + other.meters
		cm = self.centimeters + other.centimeters
		if cm >= 100:
			result.meters += cm//100
			result.centimeters = cm%100
		else:
			result.centimeters = cm
		return result

	def __sub__(self, other):
		result = Distance()
		cm = self.meters * 100 + self.centimeters - (other.meters * 100 + other.centimeters)
		result.meters = cm//100
		result.centimeters = cm%100
		return result


	def __idd__(self, other):
		self.meters = self.meters + other.meters
		self.centimeters = self.centimeters + other.centimeters


def main():
	a = Distance()
	a.getdata()
	b = Distance()
	b.getdata()
	a += b
	a.putdata()
if __name__ == '__main__':
	main()
