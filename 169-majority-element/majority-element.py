class Solution(object):
    def majorityElement(self, nums):
        length = len(nums)
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
                if hash[num] >= (length / 2) + 1:
                    majority = num
                    return majority
            else:
                hash[num] = 1
                majority = num
        return majority        
        