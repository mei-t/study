from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        firstCandi = {i for i in range(numCourses)}
        nextMap = defaultdict(set)
        prevs = [0] * numCourses
        
        for pair in prerequisites:
            nextCourse, prevCourse = pair[0], pair[1]
            firstCandi.discard(nextCourse)
            nextMap[prevCourse].add(nextCourse)
            prevs[nextCourse] += 1
        
        curs = firstCandi
        visited = set()
        while len(curs) > 0:
            nexts = set()
            for i in curs:
                visited.add(i)
                for j in nextMap[i]:
                    prevs[j] -= 1
                    if prevs[j] == 0:
                        nexts.add(j)
            curs = nexts
        
        return len(visited) == numCourses