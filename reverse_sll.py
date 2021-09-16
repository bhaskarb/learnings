class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        assert left >= 0
        assert left <= right
        #There is no reversal here
        if left == right: 
            return head
        #This is an empty list
        if not head:
            return head
        curr, prev = head, None
        for i in range(1, left):
            prev, curr = curr, curr.next
            if not curr:
                return head #Nothing to do, since left exceeds ll size
        follow, prev_head, prev_tail = curr, prev, curr
        for i in range(right - left + 1):
            follow = follow.next
            curr.next, prev, curr = prev, curr, follow
            if not curr: #right exceeds end of array, reverse immediately
                break
        prev_tail.next = curr
        if prev_head: #left is not the first element, head stays the same
            prev_head.next = prev
            return head
        return prev
