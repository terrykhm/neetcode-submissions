class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDiffDict = dict()

        for index, num in enumerate(nums):
            sumDiff = target - num
            if sumDiff in sumDiffDict:
                idx = sumDiffDict[sumDiff]
                return [idx, index]
            else:
                sumDiffDict[num] = index
        return []

