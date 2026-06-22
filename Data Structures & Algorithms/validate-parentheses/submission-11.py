class Solution:
    def isValid(self, s: str) -> bool:
        opening_chars = []

        if len(s) < 2:
            return False

        for ch in s:
            if ch in ('(', '[', '{'):
                opening_chars.append(ch)
            elif ch in (')', ']', '}'):
                if len(opening_chars)== 0:
                    return False
                opening_char = opening_chars.pop()
                if ch == ')' and opening_char != '(':
                    return False
                if ch == ']' and opening_char != '[':
                    return False
                if ch == '}' and opening_char != '{':
                    return False
            else:
                return False
        return len(opening_chars) == 0