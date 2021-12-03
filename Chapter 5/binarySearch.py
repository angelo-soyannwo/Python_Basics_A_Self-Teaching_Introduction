

from sort import sort

def binary_search(array, val, left, right):
	x = array 
	mid = (right + left) //2

	if left > right:
		return -1
	
	if x[mid] == val:
		return mid

# left side of binary search
	if val < x[mid]:
		return binary_search(x, val, left=0, right=mid-1)
	
	return binary_search(x, val, mid+1, right)

numbers = [1, 2, 3, 4, 5, 10] 
y = len(numbers) - 1

print(binary_search(numbers, 10, 0, y))
