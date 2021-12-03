
def sort(x):
	array = x
	n = len(array)
	for i in range(n):
		for j in range(n):
			if array[j] > array[i]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return array

def median(x):
	array = sort(x)
	n = len(x)
	if n % 2 == 0:
		mid1 = n/2
		mid2 = n/2 + 1
		median = (array[mid1]+array[mid2]) / 2
		result = "The median numbers are " + str(array[mid1]) + " and " + str(array[mid2])
	else:
		result = array[int(n/2 + 0.5)]
	return result

print(median([2, 2, 3, 2]))


