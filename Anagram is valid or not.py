
from collections import Counter
def Anargam(s: str,d:str):
    if (len(s)==len(d)):
        if Counter(s)==Counter(d):
            return True
        else:
            return False
    else:
        return False
print(Anargam('listen','silent'))

#the string is sorted in the dictionary order and then comparing both the strings
def Anargam(s: str,d:str):
    if (len(s)==len(d)):
        if sorted(s)==sorted(d):
            return True
        else:
            return False
    else:
        return False
print(Anargam('Lis10en','siL1en0'))
