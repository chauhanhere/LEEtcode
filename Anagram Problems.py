242.valid Anagram

def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        return False
     
2273.Find resultant Array after removing Anagrams

def removeAnagrams(self, words: List[str]) -> List[str]:
  #consumes Less Time
        res = [words[0]]
        for i in range(len(words)):
        #check anagram
            if sorted(res[-1])!=sorted(words[i]): # Here need some attention
                res.append(words[i])
        return res
        
        #Consumes More time
        '''res, i = [], 0
        while i < len(words):
            j = i+1
            while j < len(words) and Counter(words[i]) == Counter(words[j]):
                j += 1
            res.append(words[i])
            i = j
        return res'''
