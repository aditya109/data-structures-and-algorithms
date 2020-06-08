from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key= lambda person: person[0], reverse = True)        
        print(people)
        for person in people:
            result.insert(person[1], person)
            print(f"{person} -> {result}")
        return result

inputArray = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
print(Solution().reconstructQueue(inputArray))