from collections import defaultdict
from typing import List, Dict


# N = numCourses
# R = len(prerequisites)
# TC: O(N + R) (while文の中では各courseに対して1回だけ処理が行われている)
# SC: O(N + R)
class Solution1:
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

# N = numCourses
# R = len(prerequisites)
# TC: O(N + R)
# SC: O(N + R)
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextMap = defaultdict(list)
        for pair in prerequisites:
            nextCourse, prevCourse = pair[0], pair[1]
            nextMap[prevCourse].append(nextCourse)
        
        visited = [False] * numCourses
        isChecked = [False] * numCourses
        for i in range(numCourses):
            if self.isCycle(i, visited, isChecked, nextMap):
                return False
        
        return True
        
    def isCycle(self, course: int, visited: List[bool], isChecked: List[bool], nextMap: Dict[int, List[int]]) -> bool:
        if isChecked[course]:
            return False
        if visited[course]:
            return True
        
        ret = False
        visited[course] = True
        for nextCourse in nextMap[course]:
            ret = self.isCycle(nextCourse, visited, isChecked, nextMap)
            if ret: break
        
        visited[course] = False
        isChecked[course] = True
        return ret