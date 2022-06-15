def containsDuplicate(nums: list[int]) -> bool:
    s=set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False
print(containsDuplicate([12,340,34,5,5]))        


