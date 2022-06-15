#removeNthFromEnd function is working in(L) but the total code is not working.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd( head, n):
        dummy=ListNode(0,head)
        left=dummy
        right=head
        k=1
        while k<n and right:
            #print("1 times")
            #print(right)
            right=right.next
            left=left.next
            k+=1
        #while right:
            #print("2 times")
            #left=left.next
            #right=right.next
        #delete
        left.next=left.next.next
        return dummy.next
        
s=Solution.removeNthFromEnd([1,2,3,4,23],2)
print(s)
