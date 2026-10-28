class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        l = 0
        cur_letter = None
        count = 0

        for r in range(len(chars)):
            if not cur_letter:
                cur_letter = chars[r]
                count += 1
                continue

            if chars[r] != cur_letter and count > 1:
                chars[l] = cur_letter
                l += 1

                count = str(count)
                for n in count:
                    chars[l] = n
                    l += 1
            elif chars[r] != cur_letter:
                chars[l] = cur_letter
                l += 1
            else:
                count += 1
                continue
                
            count = 1
            cur_letter = chars[r]
        
        if cur_letter and count > 1:
            chars[l] = cur_letter
            l += 1

            count = str(count)
            for n in count:
                chars[l] = n
                l += 1
        elif cur_letter:
            chars[l] = cur_letter
            l += 1

        return l
            




        