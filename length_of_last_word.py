class Solution(object):
# https://leetcode.com/problems/length-of-last-word/description/
	def lengthOfLastWord(self, s):
		s = s.split()
		return len(s.pop())

s = "   fly me   to   the moon  "
answer = Solution()
print (answer.lengthOfLastWord(s))    



