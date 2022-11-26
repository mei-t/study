from collections import defaultdict
from typing import List

class courseNode:
    def __init__(self):
        self.nexts = []
        self.prevs = 0

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        firstCandi = {i for i in range(numCourses)}
        courseMap = defaultdict(courseNode)
        for pair in prerequisites:
            nextCourse, prevCourse = pair[0], pair[1]
            firstCandi.discard(nextCourse)
            courseMap[prevCourse].nexts.append(nextCourse)
            courseMap[nextCourse].prevs += 1
        
        curs = firstCandi
        ret = []
        while len(curs) > 0:
            nexts = set()
            for i in curs:
                ret.append(i)
                for j in courseMap[i].nexts:
                    print(j, courseMap[j].prevs)
                    courseMap[j].prevs -= 1
                    if courseMap[j].prevs == 0:
                        nexts.add(j)
            curs = nexts
        if len(ret) < numCourses:
            return []
        
        return ret