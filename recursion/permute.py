
def swap(array, a, b):
	if a == b:
		return array
	else:
		array[a], array[b] = array[b], array[a]
		return array

def copy_array(array):
	x = []
	for i in range(len(array)):
		x.append(array[i])
	return x

def permute(array):
	x = copy_array(array)
	store = []


	n = len(x)
	for i in range(n):

		copy = copy_array(x)
		swap(copy, 0, i)
		

		for j in range(n):
			for z in range( n):
				swap(copy, j, z)
				if copy not in store:
					store += [copy]
				copy = copy_array(copy)
	return store

test = [1, 2, 3, 4]
a = permute(test)

print(a)
print(len(a))
