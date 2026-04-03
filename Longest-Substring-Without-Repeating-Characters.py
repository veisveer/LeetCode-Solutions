class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        best_length = 0
        head = 0
        tail = 0
        for i in range(len(s)):
            char = s[i]
            if char in last_seen and (head > last_seen[char] >= tail):
                tail = last_seen[char] + 1
            head += 1
            last_seen[char] = i
            best_length = max(best_length, head - tail)
        return best_length