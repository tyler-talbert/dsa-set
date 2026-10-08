class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        completed = set()

        # course --> prerequisites
        for a, b in prerequisites:
            adj_list[a].append(b)

        def dfs(course, in_progress):
            if course in completed:
                return True
            # Cycle
            if course in in_progress:
                return False

            in_progress.add(course)

            for pre in adj_list[course]:
                if not dfs(pre, in_progress):
                    return False

            in_progress.remove(course)
            completed.add(course)

            return True
    

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True
        