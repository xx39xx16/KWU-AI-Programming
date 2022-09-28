import turtle as t
t.Turtle
t.showturtle()
t.bgcolor('gray')
t.speed(10)
t.penup()
t.setposition(0,-100)
t.pendown()

t.pensize(5)
t.pencolor('bisque')
t.fillcolor('darkgoldenrod')
t.begin_fill()
t.circle(150)
t.end_fill() #얼굴 그리기 

t.penup()
t.setposition(0,-45)
t.pendown()
t.pensize(2)
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.circle(90)
t.end_fill() #입 아랫입술 

t.penup()
t.setposition(-5,-35)
t.pendown()
t.pensize(2)
t.pencolor('darkgoldenrod')
t.fillcolor('darkgoldenrod')
t.begin_fill()
t.circle(110)
t.end_fill() #입 윗입술


t.penup()
t.setposition(0,30)
t.pendown()
t.pensize(1)
t.pencolor('goldenrod')
t.fillcolor('goldenrod')
t.begin_fill()
t.circle(15)
t.end_fill() #코 그리기

t.penup()
t.setposition(-100,70)
t.pendown()
t.pensize(3)
t.pencolor('black')
t.fillcolor('aqua')
t.begin_fill()
t.seth(-45)
t.circle(30,90)
t.circle(10,90)
t.circle(30,90)
t.circle(10,90)
t.end_fill() #왼쪽 눈 그리기

t.penup()
t.setposition(32,70)
t.pendown()
t.pensize(6)
t.pencolor('black')
t.fillcolor('steelblue')
t.begin_fill()
t.seth(-45)
t.circle(40,90)
t.circle(20,90)
t.circle(40,90)
t.circle(20,90)
t.end_fill() #오른쪽 눈 그리기

t.done()
