class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        for i in s :
            if i.isalnum():
                temp = temp+i
        return (temp == temp[::-1])


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))