Dp 

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def sol(s,dict,memo):
            if s in memo: return memo[s]
            if s == "": return True

            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if sol(new_s, wordDict,memo): # if we find  even one possible way we can stop because the question asks if possible only.
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return sol(s,wordDict,{})
