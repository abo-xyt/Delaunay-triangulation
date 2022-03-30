import scipy.spatial, numpy as np, turtle, random, math

moje_punkty=[]
for i in range(1,101):
    moje_punkty.append([random.randint(-300,300),random.randint(-300,300)])

punkty=np.array(moje_punkty)
p=scipy.spatial.Delaunay(punkty)
trojkaty=p.simplices

wn=turtle.Screen()
turtle.tracer(0)
turtle.color('red')

def rysuj_punkty(punkty):
    for punkt in punkty:
        turtle.penup()
        turtle.goto(punkt)
        turtle.pendown()
        turtle.dot(size=None)

def rysuj_trojkaty(trojkaty):
    for trojkat in trojkaty:
        turtle.penup()
        pierwszy=None
        for punkt in trojkat:
            if pierwszy==None:
                pierwszy=punkt
            turtle.goto(moje_punkty[punkt])
            turtle.pendown()
        turtle.goto(moje_punkty[pierwszy])
        turtle.penup()

def rysuj_okregi(trojkaty):
    for trojkat in trojkaty:
        turtle2=turtle.Turtle()
        turtle2.color('lightgrey')
        turtle2.penup()
        ws_pkt=[]
        for punkt in trojkat:
            ws_pkt.append([moje_punkty[punkt][0], moje_punkty[punkt][1]])
        d=2*(ws_pkt[0][0]*(ws_pkt[1][1]-ws_pkt[2][1])+ws_pkt[1][0]*(ws_pkt[2][1]-ws_pkt[0][1])+ws_pkt[2][0]*(ws_pkt[0][1]-ws_pkt[1][1]))

        ux=((ws_pkt[0][0]*ws_pkt[0][0]+ws_pkt[0][1]*ws_pkt[0][1])*(ws_pkt[1][1]-ws_pkt[2][1])+(ws_pkt[1][0]*ws_pkt[1][0]+ws_pkt[1][1]*
            ws_pkt[1][1])*(ws_pkt[2][1]-ws_pkt[0][1])+(ws_pkt[2][0]*ws_pkt[2][0]+ws_pkt[2][1]*ws_pkt[2][1])*(ws_pkt[0][1]-ws_pkt[1][1]))/d

        uy=((ws_pkt[0][0]*ws_pkt[0][0]+ws_pkt[0][1]*ws_pkt[0][1])*(ws_pkt[2][0]-ws_pkt[1][0])+(ws_pkt[1][0]*ws_pkt[1][0]+ws_pkt[1][1]*
            ws_pkt[1][1])*(ws_pkt[0][0]-ws_pkt[2][0])+(ws_pkt[2][0]*ws_pkt[2][0]+ws_pkt[2][1]*ws_pkt[2][1])*(ws_pkt[1][0]-ws_pkt[0][0]))/d

        R=math.sqrt((moje_punkty[punkt][0]-ux)**2+(moje_punkty[punkt][1]-uy)**2)
        turtle2.goto(ux,uy)
        turtle2.setheading(math.degrees(-math.atan((moje_punkty[punkt][1]-uy)/(moje_punkty[punkt][0]-ux))))
        turtle2.forward(R)
        turtle2.right(-90)
        turtle2.pendown()
        turtle2.circle(R)
        turtle2.penup()
        turtle2.hideturtle()

def new_point_after_click(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(size=None)
    moje_punkty.append([int(x),int(y)])
    punkty = np.array(moje_punkty)
    p = scipy.spatial.Delaunay(punkty)
    trojkaty = p.simplices
    turtle.clear()
    rysuj_okregi(trojkaty)
    rysuj_punkty(punkty)
    rysuj_trojkaty(trojkaty)
    turtle.update()

rysuj_punkty(punkty)
rysuj_trojkaty(trojkaty)
turtle.onscreenclick(new_point_after_click, btn=1)
turtle.mainloop()













