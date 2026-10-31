class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Build a map of course -> list[pre]
        required = defaultdict(list)
        for course, pre in prerequisites:
            required[course].append(pre)

        valid_order = []
        taken = set()

        def dfs(course: int, in_progress: set[int]):
            if course in taken:
                return True
            if course in in_progress:
                return False
            
            in_progress.add(course)
            
            for prerequisite in required[course]:
                if not dfs(prerequisite, in_progress):
                    return False

            taken.add(course)
            valid_order.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        
        return valid_order




            


        
        # 1. Cannot be reached
        # 2. We loop infinitely 


        