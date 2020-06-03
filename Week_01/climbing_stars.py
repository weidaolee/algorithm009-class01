class Solution:
    def climbStairs(self, n: int) -> int:
        s = {1:1, 2:2}
        if n <= 2:
            return n
        else:
            for i in range(3, n + 1):
                s[i] = s[i - 1] + s[i - 2]
            return s[i]
