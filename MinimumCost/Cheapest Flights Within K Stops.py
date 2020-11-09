class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        edges = [[False for i in range(n)] for i in range(n)]
        num_edges = len(flights)
        costs = [float('inf') for i in range(n)]
        q = []
        
        for i in range(num_edges):
            start_vertice,end_vertice,path_cost = flights[i]
            edges[start_vertice][end_vertice]= path_cost
            if flights[i][0]==src:
                heapq.heappush(q,((path_cost,end_vertice,0)))
                costs[end_vertice] = path_cost
                
        while len(q)>0:
            current_cost,current_vertex,k = heapq.heappop(q)
            if current_vertex==dst:
                return current_cost
            if k<K:
                for next_vertex,cost in enumerate(edges[current_vertex]):
                    if cost:
                        costs[next_vertex] = current_cost+cost
                        heapq.heappush(q,(costs[next_vertex],next_vertex,k+1))
        return -1