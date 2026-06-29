from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        char_dict = defaultdict(int)
        # Construct character count dictionary
        for char in s:
            char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                return False
            elif char_dict[char] == 0:
                return False
            else:
                char_dict[char] -= 1
        return True
            
        



# What is anagram 
# - exact same characters as another string but different order


# 1/ First Check Length of strings

# 2/ Verify both strings contain same number of characters


# Hashmap 
# Space complexity of O(26) -> O(1)
# Time complexity of O(n) + (O(m) * )
# - Go through the first string
# - Increment character

# - Go through 2nd string
# - Decrement, if zero, remove

# - Check if hashmap is empty

