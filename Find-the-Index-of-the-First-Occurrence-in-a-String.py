1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        found = True
4        for start in range(len(haystack)):
5            for i in range(len(needle)):
6                if start + i < len(haystack) and not haystack[start + i] == needle[i]:
7                    found = False
8                    break
9                elif start + i >= len(haystack):
10                    found = False
11                    break
12            if found:
13                return start
14            else:
15                found = True
16        return -1
17
18            
19        