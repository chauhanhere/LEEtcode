def twoSum(nums,target):
    d=dict()
    for i in range(len(nums)):
        m= target - nums[i]
        print(d)
        print(m)
        if m in d:
            return [d[m], i]
        else:
            d[nums[i]] = i
print(twoSum([2,4,7,11],9))
