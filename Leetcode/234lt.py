# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         temp = head
#         result = ""
#         reversed_result = ""
#         while temp:
#             result = result + str(temp.val) + " "
#             temp = temp.next
#         length = len(result)
#         number = ""
#         for ch in result:
#             if ch == " ":
#                 reversed_result = number + " " + reversed_result
#                 number = ""
#             else:
#                 number = number + ch
#         return reversed_result == result

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        result = ""
        reversed_result = ""
        while temp:
            result = result + str(temp.val) + " "
            temp = temp.next
        return " ".join(result[:len(result)-1].split(" ")[::-1]) == result[:len(result)-1]


ll = ListNode(-129)
ll.next = ListNode(-129)
# ll.next.next = ListNode(2)
# ll.next.next.next = ListNode(1)

print(Solution().isPalindrome(ll))