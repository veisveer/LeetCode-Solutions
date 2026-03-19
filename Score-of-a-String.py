1class Solution:
2    def scoreOfString(self, s: str) -> int:
3        score = 0
4        for i in range(len(s)-1):
5            score += abs(ord(s[i]) - ord(s[i+1]))
6        return score
7
8        