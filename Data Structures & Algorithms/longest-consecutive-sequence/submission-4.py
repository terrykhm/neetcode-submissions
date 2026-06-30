class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        if len(nums) == 0:
            return 0

        longestConsecutive = 1

        for num in nums:
            curLength = 1

            lowerBound = num
            while (lowerBound - 1) in numSet:
                lowerBound -= 1
                numSet.remove(lowerBound)

            upperBound = num
            while (upperBound + 1) in numSet:
                upperBound += 1
                numSet.remove(upperBound)
            
            longestConsecutive = max(longestConsecutive, upperBound - lowerBound + 1)

        return longestConsecutive 
        