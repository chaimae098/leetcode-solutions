class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        dic={")":"(","}":"{","]":"["}
        for char in s :
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if not stack or dic[char] != stack.pop():
                    return False
        return not stack     
