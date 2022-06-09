from utility import *


class BFS(maze):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.step = 0
    def expand_node(self, node, marked: list):
        north = Node(node.coor_x - 1, node.coor_y, parent = node)
        south = Node(node.coor_x + 1, node.coor_y, parent = node)
        east = Node(node.coor_x, node.coor_y + 1, parent = node)
        west = Node(node.coor_x, node.coor_y - 1, parent = node)

        valid_nodes = []

        if not self.is_wall(node = north) and not is_exist(north, marked):
            valid_nodes.append(north)
        if not self.is_wall(node = south) and not is_exist(south, marked):
            valid_nodes.append(south)
        if not self.is_wall(node = east) and not is_exist(east, marked):
            valid_nodes.append(east)
        if not self.is_wall(node = west) and not is_exist(west, marked):
            valid_nodes.append(west)
        
        return valid_nodes


    def search(self):
        queue = []
        #If a node is marked, we don't open it again

        node_start = Node(x = self.start[0], y = self.start[1])
        queue.append(node_start)
        marked = [node_start]
        while 1:
            if not queue: 
                return False #can't find the answer for this maze
            current = queue.pop(0) #get first elem

            if current.get_coor() == self.end:
                self.answer = current.backtracking()   #user can use this node to backtrack to the start.
                self.step = len(marked)
                return current                         #or, we can do it anyway!

            for neighbour in self.expand_node(current, marked):
                queue.append(neighbour)
                marked.append(neighbour)


class DFS(maze):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.step = 0
        self.footprint = []

    def get_step(self):
        return self.step

    def draw_footprint(self):
        '''
        No need to worry about the arrows after running visualize_maze(),
        imagine these are footprint that the algorithm left for us to see where it went.
        '''
        visualize_maze(self.matrix, self.bonus_points, self.start, self.end, self.footprint)

    def increase_step(self, val: int = 1):
        self.step += 1

    def search(self):
        node_start = Node(x = self.start[0], y = self.start[1])
        stack = []
        stack.append(node_start)
        marked = []
        return self.recursion_DFS(stack, marked)

    def recursion_DFS(self, stack, marked):
        current = stack.pop() #get last node
        marked.append(current)
        self.increase_step() #increase step by 1 (moving 1 space)
        self.footprint.append(current.get_coor()) #save footprint

        if current.get_coor() == self.end:
            self.answer = current.backtracking()
            return current

        for neighbour in self.expand_node(current, marked):
            stack.append(neighbour)
            result = self.recursion_DFS(stack, marked)
            if result != False:
                return result

        return False

    def expand_node(self, node, marked):
        north = Node(node.coor_x - 1, node.coor_y, parent = node)
        south = Node(node.coor_x + 1, node.coor_y, parent = node)
        east = Node(node.coor_x, node.coor_y + 1, parent = node)
        west = Node(node.coor_x, node.coor_y - 1, parent = node)

        valid_nodes = []
        if not self.is_wall(node = north) and not is_exist(north, marked):
            valid_nodes.append(north)
        if not self.is_wall(node = south) and not is_exist(south, marked):
            valid_nodes.append(south)
        if not self.is_wall(node = east) and not is_exist(east, marked):
            valid_nodes.append(east)
        if not self.is_wall(node = west) and not is_exist(west, marked):
            valid_nodes.append(west)

        #priority: [north, south, east, west], not all 4 elements exist at once!
        #order is random, depends on what you write.
        return valid_nodes 


class Greedy_Best_First_search(maze):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.step = 0
        self.footprint = []
        self.heuristic = 0

    def draw_footprint(self):
        '''
        No need to worry about the arrows after running visualize_maze(),
        imagine these are footprint that the algorithm left for us to see where it went.
        '''
        visualize_maze(self.matrix, self.bonus_points, self.start, self.end, self.footprint)

    def increase_step(self, val: int = 1):
        self.step += 1

    def search(self):
        node_start = Node(x = self.start[0], y = self.start[1])
        stack = []
        stack.append(node_start)
        marked = []
        return self.recursion_DFS(stack, marked)

    def recursion_DFS(self, stack, marked):
        current = stack.pop() #get last node
        marked.append(current)
        self.increase_step() #increase cost by 1 OR moving 1 space
        self.footprint.append(current.get_coor()) #save footprint

        if current.get_coor() == self.end:
            self.answer = current.backtracking()
            return current

        if self.bonus_points_:
            for index in range(len(self.bonus_points_)):
                if current.get_coor() == (self.bonus_points_[index][0], self.bonus_points_[index][1]):
                    #self.point += self.bonus_points_[index][2]
                    self.bonus_points_.pop(index)#After getting bonus point, delete it.
                    break

        for i in self.expand_node(current, marked):
            stack.append(i)
            result = self.recursion_DFS(stack, marked)
            if result != False:
                return result

        return False

    def sort_increase_distance(self, nodes: list, point: tuple):
        '''Node is increase based on the distance from that node to a point'''
        for i in range(len(nodes)):
            min = i
            for j in range(i, len(nodes)):
                if calc_distance(nodes[j].get_coor(), point) < calc_distance(nodes[min].get_coor(), point):
                    min = j
            nodes[i], nodes[min] = nodes[min], nodes[i]

    def heuristic_1(self, node, nodes: list):
            '''Collect nearest bonus point, not care about its value'''
            d = []
            for p in self.bonus_points_:
                d.append(calc_distance(node.get_coor(), (p[0], p[1])))
            d.append(calc_distance(node.get_coor(), self.end))

            min = 0
            for index in range(len(d)):
                if d[min] > d[index]:
                    min = index
            
            if min == len(d) - 1:
                self.sort_increase_distance(nodes, self.end)
            else:
                x=self.bonus_points_[min][0]
                y=self.bonus_points_[min][1]
                self.sort_increase_distance(nodes, (x,y))

    def heuristic_2(self, node, nodes):
        L = []
        for n in nodes:
            total_distance = 0
            for p in self.bonus_points_:
                total_distance += calc_distance(n.get_coor(), (p[0], p[1]))
            total_distance += calc_distance(n.get_coor(), self.end)

            L.append([n, total_distance])

        for i in range(len(L)):
            min = i
            for j in range(i, len(L)):
                if L[j][1] < L[min][1]:
                    min = j
                elif L[j][1] == L[min][1] and calc_distance(L[j][0].get_coor(), self.end) < calc_distance(L[min][0].get_coor(), self.end):
                    min = j
            nodes[i], nodes[min] = nodes[min], nodes[i]

    def heuristic_3(self, node, nodes):
        subset_of_bp = [] # is a subset of bonus_points
        for p in self.bonus_points_:
            if p[2] > calc_distance(node.get_coor(), (p[0], p[1])):
                subset_of_bp.append(p)

        if not subset_of_bp:
            self.sort_increase_distance(nodes, self.end)
            return

        list_of_distance = []
        for p in subset_of_bp:
            list_of_distance.append(calc_distance(node.get_coor(), (p[0], p[1])))
        list_of_distance.append(calc_distance(node.get_coor(), self.end))

        min = 0
        for index in range(len(list_of_distance)):
            if list_of_distance[min] > list_of_distance[index]:
                min = index
            
        if min == len(list_of_distance) - 1:
            self.sort_increase_distance(nodes, self.end)
        else:
            x = subset_of_bp[min][0]
            y = subset_of_bp[min][1]
            self.sort_increase_distance(nodes, (x,y))


    def expand_node(self, node, marked):
        north = Node(node.coor_x - 1, node.coor_y, parent = node)
        south = Node(node.coor_x + 1, node.coor_y, parent = node)
        east = Node(node.coor_x, node.coor_y + 1, parent = node)
        west = Node(node.coor_x, node.coor_y - 1, parent = node)

        valid_nodes = []

        if not self.is_wall(node = north) and not is_exist(north, marked):
            valid_nodes.append(north)
        if not self.is_wall(node = south) and not is_exist(south, marked):
            valid_nodes.append(south)
        if not self.is_wall(node = east) and not is_exist(east, marked):
            valid_nodes.append(east)
        if not self.is_wall(node = west) and not is_exist(west, marked):
            valid_nodes.append(west)
        
        if not self.bonus_points_:#map without bonus points or all bonus points have been collected
            self.sort_increase_distance(valid_nodes, self.end)#priority: shortest distance to 'end' point
        elif self.heuristic == 1:#map with bonus points
            self.heuristic_1(node, valid_nodes)
        elif self.heuristic == 2:
            self.heuristic_2(node, valid_nodes)
        elif self.heuristic == 3:
            self.heuristic_3(node, valid_nodes)
            
        return valid_nodes



class A_star_search(maze):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.step = 0

    def find_lowest_value(self, nodes: list)->int:
        #return index of the lowest value, if 2 nodes have the same 'value', then compare 'distance'.
        min = 0
        for i in range(0, len(nodes)):
            if nodes[i].value < nodes[min].value:
                min = i
            elif nodes[i].value == nodes[min].value and nodes[i].distance < nodes[min].distance:
                min = i
        return min     
    
    def sort_increase_value(self, nodes: list):
        for i in range(len(nodes)):
            min = i
            for j in range(i, len(nodes)):
                if nodes[j].value < nodes[min].value:
                    min = j
                elif nodes[j].value == nodes[min] and nodes[j].distance < nodes[min].distance:
                    min = j
            nodes[i], nodes[min] = nodes[min], nodes[i]

    def expand_node(self, node):
        valid_nodes = []

        x, y = node.coor_x - 1, node.coor_y
        if not self.is_wall(coor = (x, y)):
            north = Node_(x, y, parent = node, cost = node.cost + 1, distance = calc_distance((x, y), self.end))
            valid_nodes.append(north)

        x, y = node.coor_x + 1, node.coor_y
        if not self.is_wall(coor = (x, y)):
            south = Node_(x, y, parent = node, cost = node.cost + 1, distance = calc_distance((x, y), self.end))
            valid_nodes.append(south)
        
        x, y = node.coor_x, node.coor_y + 1
        if not self.is_wall(coor = (x, y)):
            east = Node_(x, y, parent = node, cost = node.cost + 1, distance = calc_distance((x, y), self.end))
            valid_nodes.append(east)

        x, y = node.coor_x, node.coor_y - 1
        if not self.is_wall(coor = (x, y)):
            west = Node_(x, y, parent = node, cost = node.cost + 1, distance = calc_distance((x, y), self.end))
            valid_nodes.append(west)
        
        self.sort_increase_value(valid_nodes)
        return valid_nodes

    def is_shorter(self, neighbour, open)->bool:
        result = find_node(neighbour, open)
        if result == False:
            return False
        if neighbour.value < open[result].value or (neighbour.value == open[result].value and neighbour.distance < open[result].distance):
            #update as the path to go to this neighbour is shorter than the old way
            open[result] = neighbour
            return True
        return False

    def search(self):
        open = [] 
        closed = [] 
        open.append(Node_(x = self.start[0], y = self.start[1], 
                    cost = 0, distance = calc_distance(self.start, self.end)))

        while 1:
            if not open:
                return False #Cant find the route
            current = open.pop(self.find_lowest_value(open))
            closed.append(current)

            if current.get_coor() == self.end:
                self.answer = current.backtracking()
                self.step = len(open) + len(closed)
                return current #answer

            for neighbour in self.expand_node(current):
                if is_exist(neighbour, closed):
                    continue
                if not is_exist(neighbour, open) or self.is_shorter(neighbour, open):
                    result = find_node(neighbour, open) #If 'neighbour' is not in 'open' then add it.
                    if result == False:
                        open.append(neighbour)
