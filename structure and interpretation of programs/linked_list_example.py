

class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class node:
def __innit__(self, data=None)
	self.data = data
	self.next = None

class linked_list:
	def __init__(self):
		self.head = node()

	def append(self, value):
		new_node = node(value)
		current_node = self.head
		while self.next != None:
			current_node = self.next
		current_node.next = new_node

	def length(self):
		total = 0
		current_node = self.head
		while current_node.next != None
			total += 1
			current_node = current_node.next
		return total

	def display(self):
		elems = []
		current_node = self.head
		while current_node.next != None:
			current_node = self.next
			elems.append(current_node.data)
			count += 1
		print(elems)

	def get(self, index):
		counnt = 0
		current_node = self.head
		if index > self.length():
			print'the index is greater than the length of  the list')
			return None
		while True:
			current_node = current_node.next
			if 
		return current_node.data



class linked_list:
	def __init__(self):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next
		current_node.next = new_node


	def length(self):
		current_node = self.head
		total = 0
		while current_node.next != None:
			total += 1
			current_node = current_node.next
		return total

	def display(self):
		elems = []
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next
			elems.append(current_node.data)
		print(elems)

	def get(self, index):
		if index >= self.length():
			print('list index out of range')
			return None
		current_node = self.head
		total = 1
		while total != index:
			current_node = current_node.next
			total += 1
		return current_node.data


def main():
	my_list = linked_list()
	my_list.append(1)
	my_list.append(2)
	my_list.append(3)
	my_list.append(4)
	print(my_list.get(4))

if __name__ == '__main__':
	main()
