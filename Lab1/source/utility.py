import matplotlib.pyplot as plt
from math import sqrt
import time

def read_file(file_name: str = 'maze.txt'):
    #authors: teachers Nguyễn Khánh Toàn, Lê Minh Nhật
    f=open(file_name,'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text=f.read()
    matrix=[list(i) for i in text.splitlines()]
    f.close()

    return bonus_points, matrix

def visualize_maze(matrix, bonus, start, end, route=None):
    #authors: teachers Nguyễn Khánh Toàn, Lê Minh Nhật
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=100).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=100,color='black')

    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=100,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='silver')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def get_start_end_from_matrix(matrix):
    #authors: teachers Nguyễn Khánh Toàn, Lê Minh Nhật
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start = (i,j)
            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end = (i,j)
            else:
                pass
            
    return start, end

def calc_distance(a: tuple, b: tuple):
    #calculate distance between a & b
    #Example: a = (5, 6); b = (8, 2) -> distance = 5
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def find_node(node, nodes: list):
    '''Return index of the node in list_of_nodes base on coordinate'''
    temp = node.get_coor()
    for i in range(len(nodes)):
        if nodes[i].get_coor() == temp:
            return i
    return False

def is_exist(node, nodes: list)->bool:
    for i in nodes:
        if i.get_coor() == node.get_coor():
            return True
    return False

def Time(ob):
    start = time.time()
    ob.search()
    end = time.time()
    return round(end - start, 5)
#____________________________________________________________________________________
class Node:
    def __init__(self, x, y, action:str = None, parent = None):
        self.coor_x = x #coor: coordinate
        self.coor_y = y
        self.parent = parent #backtracking

    def get_coor(self):
        return (self.coor_x, self.coor_y)

    def is_passed(self):
        #check if a node'parent is the same with the current node
        if not self.parent:
            return False

        backtracking_node = self.parent
        while 1:
            if self.get_coor() == backtracking_node.get_coor():
                return True
            if not backtracking_node.parent:
                return False
            backtracking_node = backtracking_node.parent

    def backtracking(self)->list:
        list_of_nodes = list()
        if (not self.parent):
            return list_of_nodes

        backtracking_node = self
        while 1:
            list_of_nodes.insert(0, backtracking_node.get_coor())
            if (not backtracking_node.parent):
                return list_of_nodes
            backtracking_node = backtracking_node.parent


class Node_(Node):
    '''Node_ is an upgrade of Node, has more attributes than Node, used in A* search'''
    def __init__(self, x, y, action:str = None, parent = None, cost = 0, distance = 0):
        super().__init__(x, y, action, parent)
        self.cost = cost                        # g(x): cost of moving from start
        self.distance = distance                # h(x): distance: from node itself to exit point
        self.value = self.cost + self.distance  # f(x) = g(x) + h(x)

    def calc_value(self):
        self.value = self.cost + self.distance
    
    def print_node(self):
        super().print_node()
        print(f'f(x) = g(x) + h(x) = {self.cost} + {self.distance} = {self.value}')


class maze:
    #BASE CLASS
    def __init__(self, file_name: str):
        self.bonus_points, self.matrix = read_file(file_name)
        self.start, self.end = get_start_end_from_matrix(self.matrix)
        self.width = len(self.matrix[0])
        self.height = len(self.matrix)
        self.answer = []
        self.points_collected = []
        self.sum_point = 0
        self.bonus_points_ = list(self.bonus_points)#We can use 'copy.deepcopy()' instead.

    def print_info(self):
        print(f'''Starting point: (x, y) = {self.start}
Ending point: (x, y) = {self.end}
Maze width: {self.width}
Maze height: {self.height}
        ''')
        for point in self.bonus_points:
            print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


    def is_wall(self, node: Node = None, coor: tuple = None) -> bool:
        if node != None:
            return self.matrix[node.coor_x][node.coor_y] == 'x'
        elif coor != None:
            return self.matrix[coor[0]][coor[1]] == 'x'

    def draw_map(self):
        visualize_maze(self.matrix, self.bonus_points, self.start, self.end, self.answer)

    def calc_points_collected(self):
        if not self.bonus_points:
            return
        for a in self.answer:
            for p in self.bonus_points:
                if a == (p[0], p[1]):
                    self.sum_point += p[2]
                    self.points_collected.append(p)
        return self.sum_point

    def print_points_collected(self):
        if not self.bonus_points:
            return
        self.calc_points_collected()
        print('Points collected: ')
        for i in self.points_collected:
            print(f'({i[0]}, {i[1]}), value: {i[2]}')
        print('Total: ', self.sum_point)
