def partition(array, lb, ub):

    pivot = array[ub]
    i = lb - 1

    for j in range(lb, ub):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[ub]) = (array[ub], array[i + 1])

    return i + 1

def quickSort(array, lb, ub):
    if lb < ub:
        pi = partition(array, lb, ub)

        # Sorting the elements on the left of pivot
        quickSort(array, lb, pi - 1)

        # Sorting the elements on the right of pivot
        quickSort(array, pi + 1, ub)

if __name__ == "__main__":
    arr = input().split(" ")
    quickSort(arr, 0, len(arr) - 1)
    print('Sorted array: ', arr)
