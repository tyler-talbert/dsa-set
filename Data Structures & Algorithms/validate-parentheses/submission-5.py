class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for ch in s:
            if ch in valid_pairs:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last_paran = stack.pop()
                if ch != valid_pairs[last_paran]:
                    return False
        
        return not stack

        