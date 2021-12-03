
def sort(x):
        array = x
        n = len(array)
        for i in range(n):
                for j in range(n):
                        if array[j] > array[i]:
                                temp = array[i]
                                array[i] = array[j]
                                array[j] = temp

