import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = s.lower()
        converted = re.sub(r'[^a-z0-9]', "", converted)

        if not converted or len(converted) == 1:
            return True

        left = 0
        right = len(converted) - 1
        while left < right:
            if converted[left] != converted[right]:
                return False
            left += 1
            right -= 1
        return True