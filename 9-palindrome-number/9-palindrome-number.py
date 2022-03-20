class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        num = x
        while num > 0:
            reverse *= 10
            reverse += num % 10
            num = num // 10
        if reverse == x:
            return True
        else:
            return False
        