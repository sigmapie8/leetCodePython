class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        finalMap = {}
        for alpha in s:
            try:
                finalMap[alpha] += 1
            except:
                finalMap[alpha] = 1
        
        for alpha in t:
            try:
                finalMap[alpha] -= 1
                if(finalMap[alpha] < 0): return False
            except:
                return False
        
        return max(finalMap.values()) == 0
