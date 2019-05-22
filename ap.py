from graphics import *

au = input('ingrese automata: ')

win = GraphWin(width = 600, height = 400) 
win.setCoords(0, 0, 10, 10) 

c1 = Circle(Point(3, 5), 1) 
c1.setFill("yellow")

label = Text(Point(3, 5), au)

linea = Line ( Point ( 1, 1),  Point ( 1 ,  2 ))
linea.setWidth ( 3 )

if (au == 'a'): c1.draw(win),label.draw(win),linea.draw(win) 
else: print('Error')

win.getMouse() 
