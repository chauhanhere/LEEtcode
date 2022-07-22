def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right=ListNode(),ListNode()#dummy node
        ltail,rtail=left,right
        while head:
            if head.val<x:
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            head=head.next
        # print(ltail)
        # print(rtail)
        ltail.next=right.next
        rtail.next=None
        return left.next
