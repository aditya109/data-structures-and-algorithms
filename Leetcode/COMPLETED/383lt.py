class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_map = {}
        magazine_map = {}
        for ch in ransomNote:
            if ch in ransomNote_map:
                ransomNote_map[ch] += 1
            else:
                ransomNote_map[ch] = 1
        print(ransomNote_map)

        for ch in magazine:
            if ch in magazine_map:
                magazine_map[ch] += 1
            else:
                magazine_map[ch] = 1
        print(magazine_map)
        for k, v in ransomNote_map.items():
            if k not in magazine_map:
                print(f"{k} not found")
                return False
            elif v > magazine_map[k]:
                return False
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

print(Solution().canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
