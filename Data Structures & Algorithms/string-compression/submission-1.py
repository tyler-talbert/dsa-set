class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0

        while r < len(chars):
            cur_letter = chars[r]
            count = 0

            # Move r past every copy of the current letter
            while r < len(chars) and chars[r] == cur_letter:
                r += 1
                count += 1

            # Write the letter, then its count if it repeated
            chars[l] = cur_letter
            l += 1
            if count > 1:
                for n in str(count):
                    chars[l] = n
                    l += 1

        return l