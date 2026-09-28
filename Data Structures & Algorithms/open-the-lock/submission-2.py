class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = {*deadends, "0000"}
        q = collections.deque([("0000", 0)])

        while q:
            curr, depth = q.popleft()
            if curr == target:
                return depth
            
            for i in range(len(curr)):
                number = int(curr[i])
                nxt, prev = (number + 1) % 10, (number - 1) % 10

                above = curr[:i] + str(nxt) + curr[i + 1:]
                below = curr[:i] + str(prev) + curr[i + 1:]

                if above not in visited:
                    q.append((above, depth + 1))
                    visited.add(above)
                if below not in visited:
                    q.append((below, depth + 1))
                    visited.add(below)

        return -1




        


        