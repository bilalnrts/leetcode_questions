class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()
        neighbours = {}
        visited = set()
        count = 0
        
        for a,b in connections:
            edges.add((a,b))
        
        for city in range(n):
            neighbours[city] = []
        
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbours, visited, count
            for neighbour in neighbours[city]:
                if (neighbour in visited):
                    continue
                if (neighbour, city) not in edges:
                    count += 1
                visited.add(neighbour)
                dfs(neighbour)
        
        visited.add(0)
        dfs(0)
        return (count)