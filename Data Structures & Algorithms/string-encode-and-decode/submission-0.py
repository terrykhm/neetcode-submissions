class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + '#' + string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decodedList = []
        idx = 0
        
        while idx < len(s):

            # Get # of characters to count
            countStartIdx = idx
            while s[idx].isdigit():
                idx +=1
            readCountStr = s[countStartIdx:idx]        

            if not readCountStr.isdecimal() or s[idx] != '#':
                # Invalid String
                return []
            
            idx += 1
            readCount = int(readCountStr)
            word = s[idx:idx + readCount]
            decodedList.append(word)

            idx += readCount

        return decodedList

            



# Naive Approach
# Take string, add a ",", return string
# 100 * 200 = 20,000 which far less than the limitations of a 64-bit or 32-bit system
# Fails for non ASCII character

# Generic Approach
# Create a rule that adds "_#" infront of each string which tells
# the decode method how many characters it should read



