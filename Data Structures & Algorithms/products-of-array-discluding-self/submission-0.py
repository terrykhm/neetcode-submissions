class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        for idx in range(1, len(nums)):
            prefixProduct[idx] = prefixProduct[idx - 1] * nums[idx - 1]

        suffixProduct = [1] * len(nums)
        for idx in range(1, len(nums)):
            suffixProduct[idx] = (suffixProduct[idx - 1]) * nums[len(nums) - idx]

        print (suffixProduct)    
        # Aggregate
        productExcept = [0] * len(nums)
        for idx in range(len(nums)):
            productExcept[idx] = prefixProduct[idx] * suffixProduct[len(nums) - 1 - idx]
        
        return productExcept

        

# Naive solution (using division)
# O(n) multiply whole list
# O(n) take product and divide by current index

# Lets Optimize
# 1,2,3,4,5
# [1 ,2 ,6 , 24, 120]

# [120, 120, 60, 20, 5]
# [5, 20, 60, 120, 120]

# [120, 60, 40, 30, 60]


# Edge-Cases
# divide by zero
# negative integers
# space constraints

# Size of two 
