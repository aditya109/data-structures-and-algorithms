# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        s, carry = 0, 0
        temp = None
        while l1 :
            s += l1.val + carry 
            if l2 is not None:
                s += l2.val
                l2 = l2.next
            if len(str(s)) == 2:
                carry = int(str(s)[0])
                s = int(str(s)[1])
            if result is None:
                result = ListNode(s)
                temp = result 
            else: 
                temp.next = ListNode(s)
                temp = temp.next
            s = 0
            l1 = l1.next

        while l2:
            s += l2.val
            if result is None:
                result = ListNode(s)
                temp = result 
            else: 
                temp.next = ListNode(s)
                temp = temp.next
            s = 0
            l2 = l2.next
        temp = ""
        while result :
            temp = f"{temp} -> {result.val}"
            result = result.next
        
        return temp[4:]
l1 = ListNode(2)    
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)    
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = ListNode()

print(Solution().addTwoNumbers(l3, l1))
