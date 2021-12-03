def arrange(array):
        for i in range(0, len(array)):
		j = i + 1
                for j  in range(j, len(array)):
                        if array[i] > array[j]:
                                temp = array[i]
                                array[i] = array[j]
                                array[j] = temp
	return array

print(arrange([1,3,4,2]))

