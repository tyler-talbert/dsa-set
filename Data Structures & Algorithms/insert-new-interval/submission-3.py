class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        nstart, nend = newInterval

        # Intervals prior to the conflict
        # While the end of the interval is less than the start
        while i < len(intervals) and intervals[i][1] < nstart:
            res.append(intervals[i])
            i += 1
        
        # Handle the conflict 
        # While the end of the new interval is greater than / equal to the start of the next
        while i < len(intervals) and nend >= intervals[i][0]:
            nstart = min(nstart, intervals[i][0])
            nend = max(nend, intervals[i][1])
            i += 1
        
        res.append([nstart, nend])
        
        # Insert the remaining intervlas
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res

