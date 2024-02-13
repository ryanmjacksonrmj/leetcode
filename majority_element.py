nums = [5, 2, 4, 5, 6, 5, 5, 5, 5]

def majorityElement(nums):
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

print (majorityElement(nums))