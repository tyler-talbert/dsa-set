class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        res = []
        # Sort intervals by start, end 
        intervals.sort()

        start, end = intervals[0]

        for nstart, nend in intervals[1:]:
            if nstart <= end:
                start = min(start, nstart) # might not need
                end = max(end, nend)
            else:
                res.append([start, end])
                start, end = nstart, nend
        
        res.append([start, end])
        return res


        