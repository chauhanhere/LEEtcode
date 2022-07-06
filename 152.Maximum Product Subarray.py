def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)#if there is single number in nums, then 0 is not a good choise for initialising
        curr_min,curr_max=1,1
        
        for n in nums:
            tmp=n*curr_max
            curr_max=max(n*curr_max, n*curr_min, n)
            curr_min=min(tmp, n*curr_min, n)
            res=max(res,curr_max)
            print('tmp=%d & curr_max=%d & res=%d'%(tmp,curr_max,res))
        return res
