1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        weight = 0
4        binary = bin(n)[2:]
5        for bit in binary:
6            if bit == '1':
7                weight += 1
8        return weight