class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_t = {}
        letters_s = {}

        for char in t:
            letters_t[char] = letters_t.get(char, 0) + 1
        
        for char in s:
            letters_s[char] = letters_s.get(char, 0) + 1
        
        return letters_t == letters_s