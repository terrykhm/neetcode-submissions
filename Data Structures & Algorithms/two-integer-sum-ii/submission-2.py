from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sumDict = defaultdict(int)
        i = 1
        sumDict[numbers[0]] = i

        i += 1
        while i <= len(numbers):
            targetDiff = target - numbers[i - 1]

            if targetDiff in sumDict:
                return [sumDict[targetDiff], i]
            else:
                sumDict[numbers[i - 1]] = i
                i +=1
        
        return []

# Since the list is sorted, we can actually improve the space complexity here by
# using two pointers