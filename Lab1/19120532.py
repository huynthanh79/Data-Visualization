# Ho va ten: Nguyen Thanh Huy
# MSSV: 19120532

# In[30]:


import numpy as np
from scipy.spatial import distance

def DFS_Recursive(matrix, start, end, path, visited):
    path.append(start)
    if start == end:
        return path, visited
    else:
        for i in range(len(matrix)):
            if not(end in visited):
                if matrix[start][i] != 0 and not(i in visited):
                    visited[i] = start
                    DFS_Recursive(matrix, i, end, path, visited)
                    
    if len(path) != 0:
        if path[-1] == start:
            path.pop(-1)
    return path, visited

                
def DFS(matrix, start, end):
    path = []
    visited = {start: None}
    return DFS_Recursive(matrix, start, end, path, visited)



# In[32]:

# ham dung de truy xuat nguoc duong di
def back_path(matrix, end, visited, path):
    path.append(end)
    if end == visited[0]:
        return path
    for i in range(len(visited)):
        if matrix[visited[i]][end] != 0:
            return back_path(matrix, visited[i], visited, path)

def BFS(matrix, start, end):
    visited = [start]
    visited_dict = {start: None}
    q = [start]
    path = []
    while q:
        if end in visited:
            back_path(matrix, visited[len(visited) - 1], visited, path)
            path.reverse()
            return path, visited_dict
        vis = q[0]
        q.pop(0)

        for i in range(len(matrix)):
            if not(end in visited):
                if (matrix[vis][i] != 0 and (not(i in visited))):
                    q.append(i)
                    visited.append(i)
                    visited_dict[i] = vis




# In[76]:

# ham tim min cua list PQ
# PQ = [(1, 2), (2, 4), (3, 9)]
# tra ra 2 thanh phan la index_min va min_pq
# trong vi du tren ham se tra ra: [0, 2]
def Min_PQ(PQ):
    min_pq = PQ[0][1]
    index_min = 0
    for i in range(len(PQ)):
        if PQ[i][1] <  min_pq:
            min_pq = PQ[i][1]
            index_min = i
    return index_min, min_pq

def UCS(matrix, start, end): 
    path=[]
    min_visited = []
    visited_dict = {start: None}
    PQ = [(start, 0)]
    check_point = False
    i = 0
    while PQ:
        Q = Min_PQ(PQ)
        i = Q[0]
        if not(PQ[i][0] in min_visited):
            min_visited.append(PQ[i][0])
        if PQ[i][0] == end:
            back_path(matrix, min_visited[len(min_visited) - 1], min_visited, path)
            path.reverse()
            return path, visited_dict
        for j in range(len(matrix)):
            if matrix[PQ[i][0]][j] != 0:
                for k in range(len(PQ)):
                    if j == PQ[k][0]:
                        if PQ[k][1] > (matrix[PQ[i][0]][j] + PQ[i][1]):
                            PQ[k] = (PQ[k][0], matrix[PQ[i][0]][j] + PQ[i][1])
                            visited_dict.update({j: PQ[i][0]})
                        check_point = True
                        break
                if not(check_point):
                    visited_dict[j] = PQ[i][0] 
                    PQ.append((j, matrix[PQ[i][0]][j] + PQ[i][1]))
                check_point = False
        PQ.pop(i)
    
    return path, visited_dict



# In[90]:


def GBFS(matrix, start, end):
    path=[start]
    visited_dict={start: None}
    next_point = start
    
    while 1:
        PQ = []
        for i in range(len(matrix)):
            if matrix[next_point][i] != 0:
                PQ.append((i, matrix[next_point][i]))
        if len(PQ) == 0:
            break
        for i in range(len(PQ)):
            if PQ[i][0] == end:
                visited_dict[end] = next_point
                path.append(end)
                return path, visited_dict
        Q = Min_PQ(PQ)
        visited_dict[PQ[Q[0]][0]] = next_point
        next_point = PQ[Q[0]][0]
        path.append(next_point)
        
    
    return path, visited_dict


# In[99]:


def Astar(matrix, start, end, pos):
    path=[]
    min_visited = []
    visited_dict = {start: None}
    PQ = [(start, 0)]
    check_point = False
    i = 0
    while PQ:
        Q = Min_PQ(PQ)
        i = Q[0]
        if not(PQ[i][0] in min_visited):
            min_visited.append(PQ[i][0])
        if PQ[i][0] == end:
            back_path(matrix, min_visited[len(min_visited) - 1], min_visited, path)
            path.reverse()
            return path, visited_dict
        for j in range(len(matrix)):
            if matrix[PQ[i][0]][j] != 0:
                for k in range(len(PQ)):
                    if j == PQ[k][0]:
                        if PQ[k][1] > (matrix[PQ[i][0]][j] + PQ[i][1] + distance.euclidean(pos[j], pos[end])):
                            PQ[k] = (PQ[k][0], matrix[PQ[i][0]][j] + PQ[i][1] + distance.euclidean(pos[j], pos[end]))
                            visited_dict.update({j: PQ[i][0]})
                        check_point = True
                        break
                if not(check_point):
                    visited_dict[j] = PQ[i][0] 
                    PQ.append((j, matrix[PQ[i][0]][j] + PQ[i][1] + distance.euclidean(pos[j], pos[end])))
                check_point = False
        PQ.pop(i)
    
    return path, visited_dict


