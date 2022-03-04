class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = "";
        try:
            for index, alphabet in enumerate(strs[0]):
                for word in strs:
                    if(len(word) == 0): return ""
                    if(word[index] != alphabet):
                        return result
                result += alphabet
            return result
        except:
            return result
