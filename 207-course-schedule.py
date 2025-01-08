class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = {}
        for prereq in prerequisites:
            if prereq[0] not in courseDict:
                courseDict[prereq[0]] = set()
            courseDict[prereq[0]].add(prereq[1])
        
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if course not in courseDict or len(courseDict[course]) == 0:
                return True
            
            visitSet.add(course)
            for prereq in courseDict[course]:
                if not dfs(prereq):
                    return False
            visitSet.remove(course)
            courseDict[course].clear()
            return True

        for course in courseDict:
            if not dfs(course):
                return False
        return True


            
