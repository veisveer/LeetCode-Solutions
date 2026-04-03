class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found = True
        for start in range(len(haystack)):
            for i in range(len(needle)):
                if start + i < len(haystack) and not haystack[start + i] == needle[i]:
                    found = False
                    break
                elif start + i >= len(haystack):
                    found = False
                    break
            if found:
                return start
            else:
                found = True
        return -1