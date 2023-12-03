from collections import deque

def bfs(graph, start): 
    visited = set() # set 데이터 타입 지정
    queue = deque([start]) 
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end= ' ')
            
            queue.extend(graph[node] - visited)


graph = {
    'A' : set(['B', 'C']),
    'B' : set(['A', 'D', 'E']),
    'C' : set(['A','F']),
    'D' : set(['B']),
    'E' : set(['B', 'F']),
    'F' : set(['C', 'E'])
}

bfs(graph, start='A')