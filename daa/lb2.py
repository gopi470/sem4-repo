from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        path,res=[],[]
        des=len(graph)-1

        def backtrack(node):
            path.append(node)

            if node==des:
                res.append(list(path))
            
            else:
                for neighbour in graph[node]:
                     backtrack(neighbour)
            
            path.pop()

        backtrack(0)
        return res


sol = Solution()

graph = [[1,2],[3],[3],[]]

result = sol.allPathsSourceTarget(graph)

print(result)










# #"Hamiltonian path" Problem

# def backtrack(node):
#     path.append(node)
#     visited.add(node)

#     # Check if we reached the end AND visited everyone
#     if len(path) == len(graph):
#         res.append(list(path))
    
#     else:
#         for neighbour in graph[node]:
#             if neighbour not in visited:      # Crucial for general graphs
#                 backtrack(neighbour)
    
#     # Backtrack
#     path.pop()
#     visited.remove(node)



# #"Hamiltonian Circuit/Cycle" Problem

def findHamiltonianCircuit(graph):
    res = []
    path = []
    visited = set()
    n = len(graph)
    
    def backtrack(node, start_node):
        path.append(node)
        visited.add(node)

        # 1. Check if all vertices are visited
        if len(path) == n:
            # 2. Check if the last node has an edge back to the start
            if start_node in graph[node]:
                # We found a circuit! 
                res.append(list(path) + [start_node])
        
        else:
            for neighbour in graph[node]:
                if neighbour not in visited:
                    backtrack(neighbour, start_node)
        
        # Backtrack (Clean up for the next branch)
        path.pop()
        visited.remove(node)

    # Start the search from node 0 (or any node)
    if n > 0:
        backtrack(0, 0)
    
    return res