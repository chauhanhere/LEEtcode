#1539
def findKthPositive(arr,k):
    l,r = 0,len(arr)-1
    while l <= r:
        m = l+(r-l)//2
        diff = arr[m]-m-1
        if diff >= k:
            r = m-1
        else:
            l = m+1
    print(l,r)
    return arr[r] + (k - (arr[r]-(r)-1))
print(findKthPositive([1,2,3,4],2))
