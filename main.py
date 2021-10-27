from canvas import Canvas
from shapes import Rectangle, Square

canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side=3, color=(0, 100, 225))
s1.draw(canvas)
canvas.make('canvas.png')
