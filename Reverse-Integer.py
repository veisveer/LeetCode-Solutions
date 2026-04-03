class Solution:
    def reverse(self, x: int) -> int:
        digits = str(x)
        if x < 0:
            value = int("-" + digits[::-1][0:-1])
            if value < -2147483647:
                return 0
            return value

        else:
            value = int(digits[::-1])
            if value > 2147483647:
                return 0
            return value