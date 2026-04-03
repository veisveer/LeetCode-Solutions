class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        binary = bin(n)[2:]
        for bit in binary:
            if bit == '1':
                weight += 1
        return weight