class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.curriculum = {}
        for course in prerequisites:
            pre = course[1]
            cur = course[0]
            if cur in self.curriculum.keys():
                self.curriculum[cur].append(pre)
            else:
                self.curriculum[cur] = [pre]

            if pre in self.curriculum.keys():
                if not self.check(pre, cur):
                    return False
        return True

    def check(self, pre, cur):
        for course in self.curriculum[pre]:
            if course == cur:
                return False
            if course in self.curriculum.keys():
                if not self.check(course, cur):
                    return False
        return True