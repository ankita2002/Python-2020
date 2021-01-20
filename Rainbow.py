import turtle
s = turtle.Screen()
p = turtle.Turtle()

def semicircle(col, rad, val):
    p.color(col)
    p.circle(rad, -180)
    p.up()
    p.setpos(val,0)
    p.down()
    p.right(180)

col = ['violet','indigo','blue','green','yellow','orange','red']
s.setup(600,600)
s.bgcolor('black')
p.right(90)
p.width(10)
p.speed(1)

for i in range(7):
    semicircle(col[i],10*(i+8),-10*(i+1))
p.hideturtle()
