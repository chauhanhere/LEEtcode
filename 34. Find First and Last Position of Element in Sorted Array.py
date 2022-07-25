def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        res=[]
        for i in nums:
            if target==i:
                res.append(nums.index(i))
                break
        for i in range(len(nums)-1,-1,-1):
            #print(i)
            if nums[i]==target:
                res.append(i)
                break
        return res
