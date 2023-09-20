import turtle as t

t.speed(25)
Forwardlength = 200
colors = ["lawngreen", "blue", "yellow", "orange", "lightpink", "lightgreen"]
t.goto(-125, -200)

for i in range(9, 3, -1):
    t.fillcolor(colors[i - 4])
    t.begin_fill()
    if i == 4:  # 사각형을 그릴 때
        t.forward(7)  # x축 방향으로 1만큼 움직임
        t.stamp()  # stamp 찍기
        t.backward(7)  # 원래 위치로 돌아옴
    for _ in range(i):
        t.forward(Forwardlength/2)
        t.stamp()
        t.forward(Forwardlength/2)
        t.left(360 / i)
    t.end_fill()
    Forwardlength -= 20
    t.setheading(0)
    t.forward(10)

t.goto
t.hideturtle()
t.penup()
t.goto(-20, 270)
t.pendown()
t.write("김솔비", align="center", font=("Arial", 35, "bold"))

# 창을 최대화로 키워줌 
canvas = t.Screen().getcanvas()
root = canvas.winfo_toplevel()
root.state('zoomed')

t.done()
