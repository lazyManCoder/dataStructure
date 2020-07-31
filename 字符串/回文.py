class Solution:
    def isPalindrome(self, x: int):
        x = str(x)
        n = len(x)
        if n == 1:
            return True
        print(n)
        print(x)
        for i in range(n // 2):

            if x[i] != x[n-i-1]:
                return False
        return True

n = 123123
a = Solution()
print(a.isPalindrome(n))
