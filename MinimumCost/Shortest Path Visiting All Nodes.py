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
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        if len(graph) == 1:
            return 0

        history = set()
        num_nodes = len(graph)
        queue = [(1 << i, i, 0) for i in range(num_nodes)]
        destination = (1 << len(graph)) - 1

        while len(queue) > 0:
            current_path, current_node, steps = queue.pop(0)
            for v in graph[current_node]:
                next_path = current_path | (1 << v)
                if next_path == destination:
                    return steps + 1
                if (next_path, v) not in history:
                    history.add((next_path, v))
                    queue.append((next_path, v, steps + 1))


sol = [[2, 5, 7], [2, 4], [0, 1], [5], [5, 6, 1], [4, 10, 8, 0, 3], [4, 9], [0], [5], [6], [5]]

problem = Solution()
problem.shortestPathLength(sol)
