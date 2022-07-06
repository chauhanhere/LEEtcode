

def containsDuplicate(self, nums: List[int]) -> bool:
        #Most Efficient solution
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
        
        
        #takes more time
        '''if len(nums)!=len(set(nums)):
            return True
        return False'''
        
        #consumes much space 
        '''s=Counter(nums)
        print(s)
        for i in nums:
            if (s.get(i))>1:
                return True
        return False'''
