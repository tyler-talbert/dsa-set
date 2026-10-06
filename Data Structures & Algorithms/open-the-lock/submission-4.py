class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends or target in deadends:
            return -1

        deadends = set(deadends)
        q = collections.deque([("0000", 0)])
        seen = set()

        while q:
            combination, depth = q.popleft()
            if combination in deadends:
                continue
            if combination == target:
                return depth

            # Get every combination
            for i in range(len(combination)):
                turn_point = int(combination[i])

                forward, backward = (turn_point + 1) % 10, (turn_point - 1) % 10
                f = combination[:i] + str(forward) + combination[i+1:]
                b = combination[:i] + str(backward) + combination[i+1:]

                if f not in seen:
                    q.append((f, depth + 1))
                    seen.add(f)
                if b not in seen:
                    q.append((b, depth + 1))
                    seen.add(b)

        return -1



            






        