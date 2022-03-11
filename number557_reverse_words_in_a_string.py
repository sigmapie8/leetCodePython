class Solution:
    def reverseWords(self, s: str) -> str:
        result = " ".join(["".join(reversed(word)) for word in s.split()])
        return result
