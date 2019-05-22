from graphics import *
import random
pa = input('f(p,a)= ')
qa = input('f(q,a)= ')
ra = input('f(r,a)= ')
pb = input('f(p,b)= ')
qb = input('f(q,b)= ')
rb = input('f(r,b)= ')
ei = input('Estado inicial: ')
ef = input('Estado final: ')

win = GraphWin(width = 1200, height = 600) 
win.setCoords(0, 0, 8, 8) 




c1 = Circle(Point(1, 5), .5) 
c2 = Circle(Point(3, 5), .5) 
c3 = Circle(Point(5.5, 5), .2) 
c4 = Circle(Point(5.5, 5), .5) 


label = Text(Point(1, 5), ei)
lb2 = Text(Point(5.5, 5), ef)

linea = Line ( Point ( 1.5, 5),  Point ( 2.5 ,  5 ))

linea.setWidth ( 1 )

l2 = Line ( Point ( .2, 5),  Point (.5, 5 ))
l2.setWidth ( 1 )
l3 = Line ( Point ( 3.5, 5),  Point (5, 5 ))
l3.setWidth ( 1 )

if(ei != pa and ei != qa and ei != ra  ):print('El estado inicial no coicide con ningun estado ingresado')
else:c1.draw(win),label.draw(win),linea.draw(win),c2.draw(win),c3.draw(win),lb2.draw(win),l2.draw(win),c4.draw(win),l3.draw(win),print('_______|a    |b \n-> ',ei,' |',pa,'  |',pb,' \n*  ',ef,' |',qa,'  |',qb,' \n    r  |',ra,'  |',rb)



win.getMouse() 
