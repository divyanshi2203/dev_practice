def bin_search(arr,target):
    l = 0
    r = len(arr)-1
    while(l<=r):
        mid = l+(r-l)//2
        if target == arr[mid]:
            return mid
        elif target<arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1
l = [2,4,6,8,9,34,56,77,79,90,102]
t = 8
print(bin_search(l,t))
        
