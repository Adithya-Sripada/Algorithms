def quickSort(list):
    if len(list) == 0:
        return list
    pivot = list[-1]
    less = []
    more = []
    for i in list[0:len(list)-1]:
        if i >= pivot:
            more.append(i)
        if(i < pivot):
            less.append(i)
    return quickSort(less) + [pivot] + quickSort(more)


def fileToArray(filename):
    arr = []
    file = open(filename, "r")
    for i in file.readlines():
        arr.append(int(i.strip()))
    file.close()
    return arr


arr1 = fileToArray("qs_test1.txt")
arr2 = fileToArray("qs_test2.txt")
arr3 = fileToArray("qs_test3.txt")
j = 1
for i in [arr1, arr2, arr3]:
    print("Test Case", j)
    print("Original Array:", i)
    print("Sorted Array:", quickSort(i))
    j+= 1
    
