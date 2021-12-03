

class complex:

	def __init__(self, real, complex):
		if type(real) != int:
			t = 'this function only takes in integers not: {}, {}'.format(str(type(real)), str(real))
			print(t)
		elif type(complex) != int:	
			t = 'Value error: this function only takes in integers not: {}, {}'.format(str(complex), str(type(complex)))
			print(t)


		else:
			self.real = real
			self.complex = complex
			if complex > 0:
				self.representation = str(self.real) + '+' + str(self.complex) + 'i'
			else:
				self.representation = str(self.real) + str(self.complex) + 'i'

def add(comp_1, comp_2):
	real_result = comp_1.real + comp_2.real
	complex_result = comp_1.complex + comp_2.complex

	return complex(real_result, complex_result).representation 


def sub(comp_1, comp_2):
	real_result = comp_1.real - comp_2.real
	complex_result = comp_1.complex - comp_2.complex

	return complex(real_result, complex_result).representation 

def mul(comp_1,comp_2):
	real_result = comp_1.complex * comp_2.complex - comp_1.real * comp_2.real
	complex_result = comp_1.complex * comp_2.real + comp_1.real * comp_2.complex
	return complex(real_result, complex_result).representation

def div(comp_1, comp_2):
	conjugate = complex(comp_1.real, -comp_2.complex)
	numerator = mul(comp_1, conjugate)
	denominator = mul(comp_2, conjugate)
	return [numerator, denominator]


def main():

	e = complex(5, -32)
	t = complex(-1, -4)
	print(div(e, t))


if __name__ == '__main__':
	main()
