def get_pivot(array, i, j):
	pivot = array[j]
	item = i - 1

	for k in range(i, j):
		if array[k] <= pivot:
			item = item + 1
			(array[item], array[k]) = (array[k], array[item])

	array[item + 1], array[j] = array[j], array[item + 1]

	return item + 1


def quick_sort(array, i=None, j=None):
    if i == None:
        i = 0
    if j == None:
        j = len(array) - 1
        
    if i < j:
        pivot = get_pivot(array, i, j)
        quick_sort(array, i, pivot - 1)
        quick_sort(array, pivot + 1, j)

def inserion_sort(array):
    for i in range(1, len(array)):
        cons = array[i]
        j = i-1

        while (j >=0 and cons < array[j]) :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = cons

def bubble_sort(array):

    length = len(array)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

def selection_sort(array):
    for i in range(len(array)):
        
        minum = i
        for j in range(i+1, len(array)):
            if array[minum] > array[j]:
                minum = j

        array[i], array[minum] = array[minum], array[i]