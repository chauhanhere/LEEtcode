'''
def Circukar(head:Optional[ListNode]):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=slow.next.next
        if slow==fast:
            return True
    return False
print(Circular([13,2,0,-4]))
  '''  
s=[2,4,5]
print(len(s))

def mergeTwoLists(list1, list2):
    m=len(list1)
    n=len(list2)
    while m>0 and n>0:
        if list1[m-1]>=list2[n-1]:
            list1[m+n-1]=list1[m-1]
            m-=1
        else:
            list1[m+n-1]=list2[n-1]
            n-=1
    if n>0:
        list1[:n]=list2[:n]
print(mergeTwoLists([1,2,4],[1,3,4]))
