from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lenOfList = len(nums)

        frequencyDict = defaultdict(int)
        for value in nums:
            frequencyDict[value] += 1
        
        sortedFrequencyList = self.bucketSort(lenOfList, frequencyDict)
        #print (sortedFrequencyList)
        numOfDistinctElements = 0
        mostFrequentElements = []
        
        # Better to use reversed(items) instead of [::-1]
        # slicing will create a shallow copy
        for numList in reversed(sortedFrequencyList):
            for num in numList:
                mostFrequentElements.append(num)
                numOfDistinctElements +=1
                if numOfDistinctElements == k:
                    return mostFrequentElements
        return mostFrequentElements



        
    def bucketSort(self, numsLength: int, frequencyDict: Dict) -> List[List[int]]:
        sortedFrequencyList = [[] for _ in range(numsLength + 1)]        
        for key, frequency in frequencyDict.items():
            sortedFrequencyList[frequency].append(key)
            
        return sortedFrequencyList

