1class Solution:
2    def reverse(self, x: int) -> int:
3        digits = str(x)
4        if x < 0:
5            value = int("-" + digits[::-1][0:-1])
6            if value < -2147483647:
7                return 0
8            return value
9
10        else:
11            value = int(digits[::-1])
12            if value > 2147483647:
13                return 0
14            return value
15        