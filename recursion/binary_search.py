

def sort(array):
	n = len(array)
	for i in range(n):
		for j in range(n):
			if array[j] > array[i]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return array

def binarySearch(array, left, right, x):

	sorted = sort(array):
	
	if left > right:
		return -1
	mid = int(right + left)/ 2
	
	if x == sorted[mid]:
		return mid

	if x < sortd[mid]:
		return binarySearch(sorted, left, mid-1, x)

	return binarySearch(sorted, mid+1, right, x)


