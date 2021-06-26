def mergeSort(arrayA):
    """
    A kind of divide and conquer algorithm that breaks down a list into several
    sublists until each sublist contains a single element.
    Then merge those sublists until one sorted list is left.
    Pseudocode taken from: https://en.wikipedia.org/wiki/Merge_sort
    """
    # Setup for the recursive call. ArrayA is our main array. ArrayB is the working array.
    arrayB = arrayA.copy()
    n = len(arrayB)
    split(arrayB, 0, n, arrayA)
    return arrayA

def split(arrayB, left_idx, right_idx, arrayA):
    """
    Split arrayA into two runs. Recursively sort these two runs into arrayB.
    """
    if right_idx - left_idx <= 1:
        return
    mid_idx = (right_idx + left_idx) // 2
    split(arrayA, left_idx, mid_idx, arrayB)
    split(arrayA, mid_idx, right_idx, arrayB)
    merge(arrayB, left_idx, mid_idx, right_idx, arrayA)

def merge(arrayA, left_idx, mid_idx, right_idx, arrayB):
    """
    Merge both runs from arrayA and arrayB.
    """
    j = left_idx
    k = mid_idx

    # While there are elements in either left or right runs...
    for i in range(right_idx)[left_idx:]:
        # If the left run head exists and is less than or equal to the right run head...
        if (j < mid_idx and (k >= right_idx or arrayA[j] <= arrayA[k])):
            arrayB[i] = arrayA[j]
            j = j + 1
        else:
            arrayB[i] = arrayA[k]
            k = k + 1

def main():
    myList = [5, 8, 10, 3, 4, 22, 7, 12, 6]
    print(mergeSort(myList))
    
if __name__ == "__main__":
    main()
    