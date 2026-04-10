def selection_sort(arr):
    for i in range(0,len(arr)-1):
        mini = i
        for j in range(i,len(arr)):
            if arr[mini]>arr[j]:
                mini = j
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    return arr
arr = [5,4,3,98,65] 
print (selection_sort(arr))