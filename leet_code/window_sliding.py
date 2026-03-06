l = [2,3,5,12,34,24,67,84,24,57,90,23,14,64,13]
max_sum = float("-inf")
window_sum = sum(l[:4])
le = 0
r = 3
while(r<len(l)-1):
    max_sum = max(window_sum,max_sum)
    #left
    window_sum -= l[le]
    le+=1
    #right
    r5+=1
    window_sum +=l[r]
print(max(window_sum,max_sum))