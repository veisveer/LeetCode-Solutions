1class Solution:
2    def myAtoi(self, s: str) -> int:
3        positive = True
4        integer = ""
5        allow_sign = True
6        allow_whitespace = True
7
8        for char in s:
9            if char == " " and allow_whitespace:
10                continue
11            elif char == "-" and not integer and allow_sign:
12                positive = False
13                allow_sign = False
14                allow_whitespace = False
15            elif char == "+" and not integer and allow_sign:
16                positive = True
17                allow_sign = False
18                allow_whitespace = False
19            elif not integer and char == "0":
20                allow_sign = False
21                allow_whitespace = False
22                continue
23            elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
24                integer += char
25                allow_whitespace = False
26            else:
27                break
28
29        if not integer:
30            return 0
31
32        if not positive and int("-" + integer) < -2147483648:
33            return -2147483648
34        elif positive and int(integer) >= 2147483647:
35            return 2147483647
36        else:
37            if not positive:
38                return int("-" + integer)
39            return int(integer)
40            
41