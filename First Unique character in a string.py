# this function is case sensitive
import collections
def firstUniqChar(s: str):
    c=collections.Counter(list(s))
    for i in range(len(s)):
        if c.get(s[i])==1:
            return i
    return -1
print('Index of first unicharacter in the string=',firstUniqChar('Loveleetcode'))
#if value of string is passed ='Leetcode' then the answer =0 because index of 'L'=0











