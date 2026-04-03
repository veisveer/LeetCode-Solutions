class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            new_num = 0
            for char in num_str:
                new_num += int(char)
            num_str = str(new_num)
        return int(num_str)