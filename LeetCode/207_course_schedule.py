from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        firstCandi = {i for i in range(numCourses)}
        nextMap = defaultdict(set)
        preMap = defaultdict(set)
        
        for pair in prerequisites:
            firstCandi.discard(pair[1])
            nextMap[pair[0]].add(pair[1])
            preMap[pair[1]].add(pair[0])
        
        curs = firstCandi
        visited = set()
        while len(curs) > 0:
            nexts = set()
            for i in curs:
                visited.add(i)
                for j in nextMap[i]:
                    preMap[j].discard(i)
                    if len(preMap[j]) == 0:
                        nexts.add(j)
            curs = nexts
        
        return len(visited) == numCourses