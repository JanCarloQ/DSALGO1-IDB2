#Insertion sort
print("arr1 values before insertion sort")
arr1 = [10,2,3,1,1,4,89,21]
print(arr1)
def InsertionSort(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1

        # move element of arr1[0..i-1]
        # that are greater than the key
        # to one position ahead of
        # their current position

        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1

        arr1[j + 1] = key
print("arr1 values after insertion sort")
print(arr1)
#selection sort
print()
print("arr2 values before selection sort")
arr2 = [10,2,3,1,1,4,89,21]
print(arr2)
for i in range(len(arr2)):
    min_idx = i
    for j in range(i+1,len(arr2)):
        #if arr2[min_idx] > arr2[j]:
        if arr2[min_idx] > arr2[j]:
            min_idx = j
        #swappping values from our array
    arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
print("arr2 values after selection sort")
print(arr2)


#Bubble sort
arr3 = [10,2,3,1,1,4,89,21]
#
print()
print("arr3 values before bubble sort")
print(arr3)

for i in range(len(arr3)):
    for j in range(0,len(arr3)-i-1):
        if arr3[j] > arr3[j+1]:
            arr3[j],arr3[j+1] = arr3[j+1],arr3[j]

print("arr3 values after bubble sort")
print(arr3)


