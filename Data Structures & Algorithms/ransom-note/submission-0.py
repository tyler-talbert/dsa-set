class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine) # O(n) time + space

        for letter in ransomNote:
            if letter not in magazine_count:
                return False
            else:
                magazine_count[letter] -= 1
                if not magazine_count[letter]:
                    del magazine_count[letter]

        return True
        