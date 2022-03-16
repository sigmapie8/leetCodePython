class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha_map = {}
        
        for index, char in enumerate(s):
            try:
                alpha_map[char] += 1
            except:
                alpha_map[char] = 1
                
        for index, char in enumerate(s):
            if(alpha_map[char] == 1):
                return index
        
        return -1
