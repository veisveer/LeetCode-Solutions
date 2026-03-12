1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        left = 0
7        right = len(s) - 1
8        while left < right:
9            temp = s[left]
10            s[left] = s[right]
11            s[right] = temp
12
13            left += 1
14            right -= 1
15        