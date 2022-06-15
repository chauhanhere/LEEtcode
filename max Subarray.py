def maxSubArray(nums: list[int]):
    s=nums[0]
    curSum=0
    for i in nums:
        if curSum<0:
            curSum=0
        curSum+=i
        s=max(s,curSum)
    return s
print("maximum subarray sum =",maxSubArray([5,4,-1,7,8]))
