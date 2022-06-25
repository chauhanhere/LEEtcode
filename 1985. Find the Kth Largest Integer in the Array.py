def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n=list(map(int,nums))
        n.sort()
        return(str(n[-k]))
        
        # OR but slower compared to above
        '''
        s=[]
        for i in nums:
            s.append(int(i))
        s.sort()
        print(s)
        res=s[-k]
        return(str(res))
        '''
