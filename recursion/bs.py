

def binary_search(array, val, left, right):
	
	if left > right:
		return -1
	
	mid = (right + left) //2
	
	if array[mid] == val:
		return mid

	if array[mid] > val:
		return binary_search(array, val, 0, mid-1)
	
	if array[mid] < val:
		return binary_search(array, val, mid+1, right)

numbers = [1, 2, 4, 5, 6, 7, 8]
y = len(numbers)
print(binary_search(numbers, 8, 0, y))
