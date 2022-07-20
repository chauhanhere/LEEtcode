def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    result = len(words)
    for word in words:
        index = -1
        for w in word:
            index = s.find(w, index + 1)#find return -1 if the value not found
            if index == -1:#then decrement 1 from the len(s) because the current w is not a matching subsequence
                result -= 1
                break
    return result
