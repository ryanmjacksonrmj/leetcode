class Solution(object):
	def isHappy(self, n):
		seen_already = {n}
		while True:
			number = 0
			while n > 0:
				number += (n % 10) ** 2
				n //= 10
			if number == 1:
				return True
			elif number in seen_already:
				return False
			else:
				seen_already.add(number)
				n = number
        