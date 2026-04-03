class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        unique = ""
        for i in range(len(nums)):
            num = nums[i]
            bit = int(num[i])
            unique += str(bit ^ 1)
        return unique