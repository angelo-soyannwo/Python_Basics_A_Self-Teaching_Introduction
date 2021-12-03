

class Base1:
	def method1(self, message):
		print(message)
	def method2(self):
		self.action()

class derived2(Base1):
	def action():
		print('action complete')

class derived1(Base1):
	def method1():
		print('derived method 1')

class operation():
	def __init__(self, num):
		self.num = num
	def sqroot(self):
		return self.num**0.5
	def cuberoot(self):
		return self.num**(1/3)

class employee():
	def getdata(self, name, age):
		name = name
		age = age
		print('name: ', name, 'age: ', str(age))

	def getdata1(self, name, age):
		self.name = name
		self.age = age


def main():
	num1 = operation(3)
	num2 = operation(3)
	list1 = [num1.sqroot, num2.sqroot, num1.cuberoot, num2.cuberoot]
	print(list1)
	for i in list1:
		print(i())

	me = employee()
	myname = 'Angelo'
	myage = 18
	me.getdata(myname, myage)

if __name__ == '__main__':
	main()

