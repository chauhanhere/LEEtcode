453. Minimum Moves to Equal Array Elements

def minMoves(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        for i in range(len(nums)-1,0,-1):
            res+=nums[i]-nums[0]
        return res
      
    
    
462. Minimum Moves to Equal Array Elements II    

def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median=len(nums)//2
        #print(len(nums))
        res=0
        for i in range(len(nums)):
            #print(nums[i])
            res+=abs(nums[i]-nums[median])
        return res
