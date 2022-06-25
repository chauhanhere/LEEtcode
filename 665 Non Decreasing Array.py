def checkPossibility(self, nums: List[int]) -> bool:
        cnt_violations=0        
        for i in range(1, len(nums)):                       
            if nums[i]<nums[i-1]:
                if cnt_violations==1:
                    return False
                cnt_violations+=1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]                       
        return True
        
        
        '''
        changed=False #To keep track we have updated our one value or not
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            if changed:
                return False
            if i==0 or nums[i+1]>=nums[i-1]:#[2,4],[3,4,2]
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            changed=True
        return True
        '''
        Tc=O(n)
        sc=O(1)
