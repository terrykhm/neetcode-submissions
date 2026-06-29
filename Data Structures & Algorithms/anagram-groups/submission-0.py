from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for string in strs:
            charDict = self.constructCharDict(string)
            anagramDict[charDict].append(string)
        
        return list(anagramDict.values())

    
    def constructCharDict(self, string: str) -> tuple:
        count = [0] * 26
        for char in string:
            print(ord(char))
            count[ord(char)- ord('a')] += 1
        return tuple(count)

