# class Solution:
#     def shortestPathLength(self, graph) -> int:

#         self.total_nodes = len(graph)
#         self.answer = []
#         self.min_len = float("inf")
#         self.graph = graph
#         self.path = set()
#         self.visited = []

#         if len(graph) == 1:
#             return 0
#         for idx in range(self.total_nodes):
#             self.BFS(idx)

#         print(self.answer)

#         return self.min_len

#     def BFS(self, current_node):)
#         if len(self.path) >= self.total_nodes - 1 and self.check_visited_all(self.path):
#             if len(self.path) < self.min_len:
#                 self.answer = list(self.path)
#                 self.min_len = len(self.answer)
#             return
#         for i in self.graph[current_node]:
#             if (current_node, i) in self.path:
#                 continue
#             self.path.add((current_node, i))
#             self.visited.append(current_node)
#             self.visited.append(i)
#             self.BFS(i)
#             self.path.remove((current_node, i))
#             self.visited.pop()
#             self.visited.pop()

#     def check_visited_all(self, path):

#         for i in range(self.total_nodes):
#             if i not in self.visited:
#                 return False
#         return True


# sol = [
#     [1, 2, 3],
#     [0],
#     [0],
#     [0],
# ]


class Solution:
    def shortestPathLength(self, graph):
        memo, final, q, steps = (
            set(),
            (1 << len(graph)) - 1,
            [(i, 1 << i) for i in range(len(graph))],
            0,
        )
        while True:
            new = []
            for node, state in q:
                if state == final:
                    return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1


sol = [[2, 5, 7], [2, 4], [0, 1], [5], [5, 6, 1], [4, 10, 8, 0, 3], [4, 9], [0], [5], [6], [5]]

problem = Solution()
problem.shortestPathLength(sol)
