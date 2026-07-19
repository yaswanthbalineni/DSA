class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length=0
        char=set()
        for i  in range(len(s)):
            while s[i] in char:
                char.remove(s[left])
                left+=1
            char.add(s[i])
            max_length=max(max_length,i-left+1)
        return max_length