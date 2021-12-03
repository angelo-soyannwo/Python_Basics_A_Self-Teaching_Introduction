class AP:
	def __innit__(self, a, d, n):
		self.a = a 
		self.d = d
		self.n = n
		self.i = a

	def __iter__(self):
		return self
	def __next__(self):
		if self.i < self.n:
			self.i = self.i
			self.i = self.i + self.d
			return i
		else:
			raise StopIteration()
x = AP()
x.__innit__(2, 2, 5)
for i in range(x.n):
	print(x.__next__(), end=", ")
