class Car:
    def __init__(self, make, model, year, cost):
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Cost: {self.cost:,}"

def mergeSort(arrayA, comparison_function):
    """
    A kind of divide and conquer algorithm that breaks down a list into several
    sublists until each sublist contains a single element.
    Then merge those sublists until one sorted list is left.
    Pseudocode taken from: https://en.wikipedia.org/wiki/Merge_sort
    """
    # Setup for the recursive call. ArrayA is our main array. ArrayB is the working array.
    arrayB = arrayA.copy()
    n = len(arrayB)
    split(arrayB, 0, n, arrayA, comparison_function)
    return arrayA

def split(arrayB, left_idx, right_idx, arrayA, comparison_function):
    """
    Split arrayA into two runs. Recursively sort these two runs into arrayB.
    """
    if right_idx - left_idx <= 1:
        return
    mid_idx = (right_idx + left_idx) // 2
    split(arrayA, left_idx, mid_idx, arrayB, comparison_function)
    split(arrayA, mid_idx, right_idx, arrayB, comparison_function)
    merge(arrayB, left_idx, mid_idx, right_idx, arrayA, comparison_function)

def merge(arrayA, left_idx, mid_idx, right_idx, arrayB, comparison_function):
    """
    Merge both runs from arrayA and arrayB. Use the comparison function here.
    """
    j = left_idx
    k = mid_idx

    # While there are elements in either left or right runs...
    for i in range(right_idx)[left_idx:]:
        # If the left run head exists and is less than or equal to the right run head...
        # Insert the comparison function here rather than statically compare two objects.
        if (j < mid_idx and (k >= right_idx or comparison_function(arrayA[j], arrayA[k]))):
            arrayB[i] = arrayA[j]
            j = j + 1
        else:
            arrayB[i] = arrayA[k]
            k = k + 1

def main():
    carList = []
    carList.append(Car("Porsche", "911 Carrera S", 2021, 117_000))
    carList.append(Car("Ford", "Mustang GT", 2021, 40_100))
    carList.append(Car("Honda", "Civic EX", 2021, 24_400))
    carList.append(Car("Honda", "CR-V EX", 2021, 27_800))
    carList.append(Car("Mazda", "Mazda3 Select", 2021, 22_900))
    carList.append(Car("Tesla", "Model 3 Performance", 2021, 55_690))
    carList.append(Car("Chevy", "Camaro SS 1LE", 2021, 46_500))
    
    print("Cars sorted from least to greatest cost:")
    mergeSort(carList, lambda carA, carB: carA.cost < carB.cost)
    for car in carList:
        print(car)
    
    print()

    print("Cars sorted by Make in alphabetical order:")
    mergeSort(carList, lambda carA, carB: carA.make < carB.make)
    for car in carList:
        print(car)
    
if __name__ == "__main__":
    main()
    