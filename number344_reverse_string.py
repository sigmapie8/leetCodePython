class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s[:] = s[::-1]
        #s[:] = [s[x] for x in range(len(s)-1, -1, -1)] 
        s[:] = reversed(s)
