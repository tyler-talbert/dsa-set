class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = collections.defaultdict(list)
        completed = set()
        res = []

        # Course --> Prerequisites
        for a, b in prerequisites:
            adj_list[a].append(b)

        def course_order(current_course: int, in_progress: set[int]) -> bool:
            if current_course in completed:
                return True
            if current_course in in_progress:
                return False

            in_progress.add(current_course)
            for pre in adj_list[current_course]:
                if not course_order(pre, in_progress):
                    return False

            in_progress.remove(current_course)
            res.append(current_course)
            completed.add(current_course)
            return True

        for i in range(numCourses):
            if not course_order(i, set()):
                return []

        return res


            

        
