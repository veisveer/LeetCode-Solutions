class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        result = ''

        ignore = True
        for bit in binary:
            if ignore and bit == '1': # flipped
                continue
            elif ignore and bit == '0': # flipped
                ignore = False
            result += str(int(bit) ^ 1)

        if not result:
            return 0
        return int(result, 2)