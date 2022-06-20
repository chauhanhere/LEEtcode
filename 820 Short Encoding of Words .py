def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True) # sorting based on the length of words
        ans=''
        for x in words: # iterating over each words
            print(x)
            if x+'#' not in ans:   # if that particular word is not present in our reference string then we are adding it to our answer
                ans+=x+'#'
        print(ans)
        return len(ans)
