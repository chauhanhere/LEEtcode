def isPalindrome(self, s: str) -> bool:
        #This code if pretty much efficient in terms of space and time complexity
        l,r=0,len(s)-1
        while(l<r):
            while l<r and s[l].isalnum()==False:#we can also define our own isalnum function.
                l+=1
            while r>l and s[r].isalnum()==False:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True
      
      OR
      
      #this code have slower timer complexity
        '''
        new_string=''
        for i in s:
            if i.isalnum():
                new_string+=i.lower()
        return new_string==new_string[::-1]
        '''

        
        Valid Palindrome II (We can delete a character to make the string palindrome)
        
        def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL,skipR=s[l + 1:r +1],s[l:r]
                return (skipL==skipL[::-1] or skipR==skipR[::-1])
            l,r=l+1,r-1
        return True
        
        
        
