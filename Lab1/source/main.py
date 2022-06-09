from algorithm import *
import map


#map.draw_map()

#_____________________map without bonus points______________________
test1 = BFS('..\\test\map3.txt')
test1.print_info()
if test1.search() == False:
   print("Can't find the route")
else:
   print('Step: ', test1.step)
   test1.draw_map()


test2 = DFS('..\\test\map3.txt')
test2.print_info()
if test2.search() == False:
   print('Cant find the route.')
else:
   print('Step: ', test2.step)
#    test2.draw_footprint()     Bản đồ bước đi
   test2.draw_map()


test3 = Greedy_Best_First_search('..\\test\map3.txt')
test3.print_info()
if test3.search() == False:
   print('Cant find the route.')
else:
   print('Steps: ', test3.step)
#    test3.draw_footprint()     Bản đồ bước đi
   test3.draw_map()


test4 = A_star_search('..\\test\map3.txt')
test4.print_info()
if test4.search() == False:
   print('Cant find the route.')
else:
    print('Steps: ', test4.step)
    test4.draw_map()


#_____________________map with bonus points______________________
test11 = Greedy_Best_First_search('..\\test\map6.txt')
test11.heuristic = 1#flag
test11.print_info()
if test11.search() == False:
   print('Cant find the route.')
else:
   #test11.draw_footprint()
   test11.print_points_collected()
   test11.draw_map()

test11 = Greedy_Best_First_search('..\\test\map6.txt')
test11.heuristic = 2#flag
test11.print_info()
if test11.search() == False:
   print('Cant find the route.')
else:
   #test11.draw_footprint()
   test11.print_points_collected()
   test11.draw_map()

test13 = Greedy_Best_First_search('..\\test\map6.txt')
test13.heuristic = 3#flag
test13.print_info()
if test13.search() == False:
    print('Cant find the route.')
else:
    #test11.draw_footprint()
    test13.print_points_collected()
    test13.draw_map()
