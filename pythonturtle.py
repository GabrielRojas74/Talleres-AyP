import turtle

t = turtle.Turtle()
t.speed(40)
t.pensize(5)
t.color("blue")
t.shape("square")
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(190)
t.rt(90)
t.fd(100)


t.up()
t.goto(120, -100)
t.down()

t.pensize(5)
t.color("red")
t.shape("square")
t.rt(270)
t.fd(190)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(190)
t.rt(180)
t.fd(100)
t.rt(270)
t.fd(100)

t.up()
t.goto(245, -100)
t.down()

t.pensize(5)
t.color("black")
t.shape("square")
t.rt(90)
t.fd(190)
t.rt(90)
t.fd(98)
t.rt(45)
t.fd(30)
t.rt(45)
t.fd(50)
t.rt(45)
t.fd(35)
t.rt(45)
t.fd(95)
t.rt(180)
t.fd(95)
t.rt(45)
t.fd(30)
t.rt(45)
t.fd(52)
t.rt(45)
t.fd(30)
t.rt(45)
t.fd(95)

t.up()
t.goto(385, -100)
t.down()

t.pensize(5)
t.color("green")
t.shape("square")
t.rt(90)
t.fd(190)
t.rt(90)
t.fd(100)
t.rt(45)
t.fd(30)
t.rt(45)
t.fd(50)
t.rt(45)
t.fd(30)
t.rt(45)
t.fd(97)
t.rt(180)
t.fd(97)
t.rt(50)
t.fd(25)
t.rt(40)
t.fd(80)

t.up()
t.goto(530, -100)
t.down()

t.pensize(5)
t.color("yellow")
t.shape("square")
t.rt(270)
t.fd(130)
t.rt(180)
t.fd(65)
t.rt(90)
t.fd(190)
t.rt(90)
t.fd(65)
t.rt(180)
t.fd(130)

t.up()
t.goto(805, -100)
t.down()

t.pensize(5)
t.color("brown")
t.shape("square")
t.rt(0)
t.fd(120)
t.rt(90)
t.fd(95)
t.rt(90)
t.fd(120)
t.rt(180)
t.fd(120)
t.rt(90)
t.fd(95)
t.rt(90)
t.fd(120)

t.up()
t.goto(850, -100)
t.down()

t.pensize(5)
t.color("grey")
t.shape("square")
t.rt(0)
t.fd(130)
t.rt(180)
t.fd(130)
t.rt(90)
t.fd(190)
t.up()
t.goto(-10, -125)
t.down()

t.speed(15)
t.pensize(5)
t.color("#094360")
t.shape("square")
t.rt(90)
t.fd(1000)
t.rt(270)
t.fd(240)
t.rt(270)
t.fd(1000)
t.rt(270)
t.fd(237)

t.up()
t.goto(-20, -140)
t.down()

t.speed(15)
t.pensize(5)
t.color("#094360")
t.shape("square")
t.rt(270)
t.fd(1025)
t.rt(270)
t.fd(240)
t.rt(270)
t.fd(1025)
t.rt(270)
t.fd(235)

t.up()
t.goto(-20, -140)
t.down()


for x in range(8):
    t.rt(90)
    for y in range(3):
        t.fd(10)
        t.rt(45)
    t.rt(90)

t.up()
t.goto(1060, -140)
t.down()


for x in range(8):
    t.rt(90)
    for y in range(3):
        t.fd(10)
        t.rt(45)
    t.rt(90)

t.up()
t.goto(1050, 140)
t.down()


for x in range(8):
    t.rt(90)
    for y in range(3):
        t.fd(10)
        t.rt(45)
    t.rt(90)

t.up()
t.goto(-10, 140)
t.down()


for x in range(8):
    t.rt(90)
    for y in range(3):
        t.fd(10)
        t.rt(45)
    t.rt(90)
