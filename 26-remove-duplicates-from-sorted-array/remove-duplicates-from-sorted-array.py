class Solution(object):
		def removeDuplicates(self, nums):
			indices = []
			test = None
			for index, num in enumerate(nums):
				if num == test:
					indices.append(index)
				else:
					test = num
			count = 0
			for index in indices:
				nums.pop(index - count)
				count += 1
			return len(nums)
        