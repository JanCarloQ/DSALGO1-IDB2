
arr1 = [23,89, 7, 56, 44]
print("1)arr1 values before Bubble sort")
print(arr1)
for i in range(len(arr1)):
    for j in range(0,len(arr1)-i-1):
        if arr1[j] > arr1[j+1]:
            arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
print("arr1 values after bubble sort")
print(arr1)


print()
arr2 =  [12, 78, 91, 34, 62]
print("2)arr2 values before Insertion sort")
print(arr2)
for i in range(1, len(arr2)):
    key = arr2[i]
    j = i - 1
    while j >= 0 and key < arr2[j]:
        arr2[j + 1] = arr2[j]
        j -= 1
    arr2[j + 1] = key
print("arr2 values after insertion sort")
print(arr2)


print()
arr3 =  [5, 99, 48, 15, 67]
print("3)arr3 values before Selection sort")
print(arr3)
for i in range(len(arr3)):
    min_idx = i
    for j in range(i+1,len(arr3)):
        if arr3[min_idx] < arr3[j]:
            min_idx = j
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
print("arr3 values after selection sort")
print(arr3)


print()
arr4 = [38, 82, 25, 74, 13]
print("4)arr4 values before Selection sort")
print(arr4)
for i in range(1, len(arr4)):
    key = arr4[i]
    j = i - 1
    while j >= 0 and key > arr4[j]:
        arr4[j + 1] = arr4[j]
        j -= 1
    arr4[j + 1] = key
print("arr4 values after insertion sort")
print(arr4)

print()
print("5)values from the second index and third index of the previous datasets into one dataset")
arr5 = [arr[2] for arr in [arr1,arr2,arr3,arr4]]
for arr in [arr1,arr2,arr3,arr4]:
    arr5.append(arr[3])
print(arr5)
print("Ascending order of the dataset")
for i in range(len(arr5)):
    min_idx = i
    for j in range(i+1,len(arr5)):
        if arr5[min_idx] > arr5[j]:
            min_idx = j
    arr5[i], arr5[min_idx] = arr5[min_idx], arr5[i]
print(arr5)
print("Descending order of the dataset")
arr6 = [arr[2] for arr in [arr1,arr2,arr3,arr4]]
for arr in [arr1,arr2,arr3,arr4]:
    arr6.append(arr[3])
print(arr6)
for i in range(len(arr6)):
    min_idx = i
    for j in range(i+1,len(arr6)):
        if arr6[min_idx] < arr6[j]:
            min_idx = j
    arr6[i], arr6[min_idx] = arr6[min_idx], arr6[i]
print(arr6)


print()
dataset = []
for arr in [arr1,arr2,arr3,arr4]:
    dataset.extend(arr)
print("6)copying all of the values from item number 1 to 4")
print(dataset)
for i in range(len(dataset)):
    min_idx = i
    for j in range(i+1,len(dataset)):
        if dataset[min_idx] > dataset[j]:
            min_idx = j
    dataset[i], dataset[min_idx] = dataset[min_idx], dataset[i]
print("dataset values after selection sort")
print(dataset)

print()
print("7)Print the even and odd values of the list/array created in item number 6.")
EvenNum = [num for num in dataset if num%2==0]
OddNum = [num for num in dataset if num%2!=0]

print("Even Numbers")
print(EvenNum)
print("Odd Numbers")
print(OddNum)

