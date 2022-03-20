class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        for i in range(len(str_num)):
            if str_num[i] != str_num[len(str_num)-i-1]:
                return False
        return True
        