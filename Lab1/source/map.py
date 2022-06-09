def draw_map():
    with open('map1.txt', 'w') as map1:
        map1.write('0\n')
        map1.write('xxxxxxx xxxxxxxxxxxx\n')
        map1.write('x    x  x  xxx xx  x\n')
        map1.write('x  x   x  x  x xxx x\n')
        map1.write('xx  xxxx  xx xx   xx\n')
        map1.write('x x    x   x     xxx\n')
        map1.write('x     xx x  xxx   xx\n')
        map1.write('x xxxx  x x  xxx  xx\n')
        map1.write('x x  xx   x     x xx\n')
        map1.write('x       x   x x  x x\n')
        map1.write('xxx  x  Sx xxxx  xxx\n')
        map1.write('xxxxxxxxxxxxxxxxxxxx')


    with open('map2.txt', 'w') as map2:
        map2.write('0\n')
        map2.write('xxxxxxxxxxxxxxxxxxxxxxx\n')
        map2.write('x                  xxxx\n')
        map2.write('x     xxxx  xxxx   xxxx\n')
        map2.write('x   xxx   xx   x   x  x\n')
        map2.write('x         x  xxxx    xx\n')
        map2.write('x    xx  x  x      xxxx\n')
        map2.write('x       x  x   xx  xxxx\n')
        map2.write('x    xxx  x    xx    xx\n')
        map2.write('xxx   x  x     xxxxx  x\n')
        map2.write('x    x  x         xx  x\n')
        map2.write('x  xx  x  xx   xxxxxx x\n')
        map2.write('x  x  x    x   x      x\n')
        map2.write('x   Sxx  x xxxx  xxxxxx\n')
        map2.write('xxxxxxxxxx xxxxxxxxxxxx')

    with open('map3.txt', 'w') as map3:
        map3.write('0\n')
        map3.write('xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx\n')
        map3.write('x              xx xx              x\n')
        map3.write('x              xx xx              x\n')
        map3.write('x              xx xx              x\n')
        map3.write('x           xx       xx           x\n')
        map3.write('x           xxxxxxxxxxx           x\n')
        map3.write('x                                 x\n')
        map3.write('x                                 x\n')
        map3.write('x                                 x\n')
        map3.write('x      xxxxxxxxxxxxxxxxxxxxx      x\n')
        map3.write('x      x                   x      x\n')
        map3.write('x      x                   x      x\n')
        map3.write('x      x                   x      x\n')
        map3.write('x                                 x\n')
        map3.write('x                S                x\n')
        map3.write('x                                 x\n')
        map3.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    with open('map4.txt', 'w') as map4:
        map4.write('0\n')
        map4.write('xxxxxxxxxxxxxxxxxxxxxxxxx\n')
        map4.write('x                       x\n')
        map4.write('x                       x\n')
        map4.write('x                 S     x\n')
        map4.write('x                       x\n')
        map4.write('x                       x\n')
        map4.write('                        x\n')
        map4.write('xxxxxxxxxxxxxxxxxxxxxxxxx')

    with open('map5.txt', 'w') as map5:#
        map5.write('0\n')
        map5.write('xxxxxxxxxxxxxxxxxxxxxx xx\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                       x\n')
        map5.write('x                      Sx\n')
        map5.write('xxxxxxxxxxxxxxxxxxxxxxxxx\n')
    
    #map name with 2 digit numbers has bonus point
    with open('map7.txt', 'w') as map11:
        map11.write('5\n')
        map11.write('3 14 15\n')
        map11.write('1 1 5\n')
        map11.write('11 18 10\n')
        map11.write('11 12 3\n')
        map11.write('12 7 3\n')
        map11.write('xxxxxxxxxxxxxxxxxxxxxxx\n')
        map11.write('x+                 xxxx\n')
        map11.write('x     xxxx  xxxx   xxxx\n')
        map11.write('x   xxx   xx  +x   x  x\n')
        map11.write('x         x  xxxx    xx\n')
        map11.write('x    xx  x  x      xxxx\n')
        map11.write('x       x  x   xx  xxxx\n')
        map11.write('x    xxx  x    xx    xx\n')
        map11.write('xxx   x  x     xxxxx  x\n')
        map11.write('x    x  x         xx  x\n')
        map11.write('x  xx  x  xx   xxxxxx x\n')
        map11.write('x  x  x    x+  x  +   x\n')
        map11.write('x   Sxx+ x xxxx  xxxxxx\n')
        map11.write('xxxxxxxxxx xxxxxxxxxxxx')


    with open('map6.txt', 'w') as map13:
        map13.write('10\n')
        map13.write('2 27 3\n')#1
        map13.write('3 27 2\n')#2
        map13.write('4 7 7\n')#3
        map13.write('4 17 3\n')#4
        map13.write('4 27 4\n')#5
        map13.write('7 17 5\n')#6
        map13.write('10 17 1\n')#7
        map13.write('12 3 1\n')#8
        map13.write('12 31 1\n')#9
        map13.write('15 17 3\n')#10
        map13.write('xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx\n')
        map13.write('x              xx xx              x\n')
        map13.write('x              xx xx       +      x\n')#1
        map13.write('x              xx xx       +      x\n')#2
        map13.write('x      +    xx   +   xx    +      x\n')#3,4,5
        map13.write('x           xxxxxxxxxxx           x\n')
        map13.write('x                                 x\n')
        map13.write('x                +                x\n')#6
        map13.write('x                                 x\n')
        map13.write('x      xxxxxxxxxxxxxxxxxxxxx      x\n')
        map13.write('x      x         +         x      x\n')#7
        map13.write('x      x                   x      x\n')
        map13.write('x  +   x                   x   +  x\n')#8,9
        map13.write('x                                 x\n')
        map13.write('x                S                x\n')
        map13.write('x                +                x\n')#10
        map13.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    with open('map8.txt', 'w') as map10:#TESTING ONLY
       map10.write('2\n')
       map10.write('1 6 15\n')
       map10.write('1 9 9\n')
       map10.write('xxxxxxxxxxxxxx\n')
       map10.write('x     +  +   x\n')
       map10.write('x     S       \n')
       map10.write('xxxxxxxxxxxxxx')
