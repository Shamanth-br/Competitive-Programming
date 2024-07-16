class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x<0:
			return False
	   
	   # second approach:
		res = 0
		temp = x
		while x:
			res = res*10 + x%10
			x = x//10
		if res == temp:
			return True
		else:
			return False