# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_string = ""
        sum_ = 0
        carry = 0
        while l1:
            sum_ = l1.val + l2.val + carry

            if sum_ <= 9:
                sum_string = f"{sum_string} {sum_} -> "
                carry = 0
            else:
                digit = int(str(sum_)[1])
                sum_string = f"{sum_string} {digit} -> "
                carry = int(str(sum_)[0])
            l1 = l1.next
            l2 = l2.next
        return str(sum_string[:-4])

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(Solution().addTwoNumbers(l1, l2))