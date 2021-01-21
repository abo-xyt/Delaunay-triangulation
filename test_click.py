import turtle
moje_punkty=[[0,0],[200,0], [300,100], [0,200], [0,400], [0,600],[100,0], [100,100]]
wn=turtle.Screen()
t=turtle.Turtle()

def new_point_after_click(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(size=None)
turtle.listen()
wn.onscreenclick(new_point_after_click)
#nowy_punkt=[]
#nowy_punkt.append(wn.onscreenclick(new_point_after_click))
#print(nowy_punkt)
turtle.mainloop()