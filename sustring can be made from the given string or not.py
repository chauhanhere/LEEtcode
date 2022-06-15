import collections
def canConstruct(ransomNote: str, magazine: str) -> bool:
    print((collections.Counter(ransomNote),collections.Counter(magazine)))
    return not collections.Counter(ransomNote) - collections.Counter(magazine)
print(canConstruct('aab','aba'))
