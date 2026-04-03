class Solution:
    def myAtoi(self, s: str) -> int:
        positive = True
        integer = ""
        allow_sign = True
        allow_whitespace = True

        for char in s:
            if char == " " and allow_whitespace:
                continue
            elif char == "-" and not integer and allow_sign:
                positive = False
                allow_sign = False
                allow_whitespace = False
            elif char == "+" and not integer and allow_sign:
                positive = True
                allow_sign = False
                allow_whitespace = False
            elif not integer and char == "0":
                allow_sign = False
                allow_whitespace = False
                continue
            elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                integer += char
                allow_whitespace = False
            else:
                break

        if not integer:
            return 0

        if not positive and int("-" + integer) < -2147483648:
            return -2147483648
        elif positive and int(integer) >= 2147483647:
            return 2147483647
        else:
            if not positive:
                return int("-" + integer)
            return int(integer)