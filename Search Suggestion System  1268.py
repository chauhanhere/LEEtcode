def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res=[]
        products.sort()  #to sort words of products in alphabetical order
        
        l,r=0,len(products)-1
        for i in range(len(searchWord)):
            c=searchWord[i]
            
            while l<=r and (len(products[l])<=i or products[l][i]!=c):
                l+=1
            while l<=r and (len(products[r])<=i or products[r][i]!=c):
                r-=1
            res.append([])
            remain=r-l+1
            for j in range(min(3,remain)): # if the words are greater than 3 it will take 3 words a/q and less than 3 it will take according to the number of remain
                res[-1].append(products[l+j])
        return res
