nums = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
	count = 0
	test = None
	for index, num in enumerate(nums):
		print ("index: " + str(count))
		print ("num: " + str(num))
		if num == test:
			print ("test value: " + str(test))
			print ("popping")
			nums.pop(count)
		else:
			print ("test value before: " + str(test))
			test = num
			print ("test value after: " + str(test))
			count += 1
			print ("new index:" + str(count))
	return nums

print(removeDuplicates(nums))