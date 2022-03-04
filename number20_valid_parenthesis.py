class Solution:
    def __init__(self):
        self.open_brackets = ["(", "{", "["]
            
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for bracket in s:
            if(len(bracket_stack) == 0):
                bracket_stack.append(bracket)
            elif(bracket in self.open_brackets):
                bracket_stack.append(bracket)
            elif((bracket == ")" and bracket_stack[-1] != "(") or (bracket == "}" and bracket_stack[-1] != "{") or (bracket == "]" and bracket_stack[-1] != "[")):
                    return False
            else:
                bracket_stack.pop()
        
        if(len(bracket_stack) != 0): return False
        return True
