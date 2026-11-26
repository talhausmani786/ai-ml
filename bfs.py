from collections import deque
def Bfs(start , end , tree):
    num_row = len(tree)
    num_col = len(tree[0])
    queue = deque([start])
    visited = set([start])
    parent = {start:None}
    directions = [
        (-1,0),
        (0,-1),
        (1,0),
        (0,1)
    ]
    while queue :
        current = queue.popleft()
        if current == end:
            break
        row,col = current
         
        for r ,c in directions:
            
            new_row = row + r
            new_col = col + c
            
            if (new_row,new_col) not in visited:
                if 0<=new_row<num_row and 0<=new_col<num_col and tree[new_row][new_col] == 0:
                    visited.add((new_row,new_col))
                    queue.append((new_row,new_col))
                    parent[(new_row,new_col)] = current
    
    if end not in parent:
        return None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
        
    path.reverse()
    return path

maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]   
]    

start = tuple(map(int ,input("enter space separated position ").split(" ")))
print("start pos" ,start)
end = (6,4)
path = Bfs(start , end , maze)
if path is None:
    print("no path exits")
else:    
    print(path)
                    