import scipy.spatial, numpy as np, turtle, random
moje_punkty=[]
for i in range(1,101):
    moje_punkty.append([random.randint(-200,200),random.randint(-200,200)])
print(moje_punkty)
#moje_punkty=[[0,0],[200,0], [300,100], [0,-200], [0,400], [0,-200],[100,0], [100,100], [100,150], [-100, -200]]
punkty=np.array(moje_punkty)
p=scipy.spatial.Delaunay(punkty)
wn=turtle.Screen()
trojkaty=p.simplices
turtle.tracer(0)
def rysuj_punkty(punkty):
    for punkt in punkty:
        turtle.penup()
        turtle.goto(punkt)
        turtle.pendown()
        turtle.dot(size=None)
def rysuj_trojkaty(trojkaty):
    for trojkat in trojkaty:
        turtle.penup()
        for punkt in trojkat:
            turtle.goto(moje_punkty[punkt])
            turtle.pendown()
        turtle.penup()

def new_point_after_click(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(size=None)
    moje_punkty.append([int(x),int(y)])
    punkty = np.array(moje_punkty)
    p = scipy.spatial.Delaunay(punkty)
    trojkaty = p.simplices
    #print(trojkaty)
    turtle.clear()
    rysuj_punkty(punkty)
    rysuj_trojkaty(trojkaty)
    turtle.update()
    #print(moje_punkty)
rysuj_punkty(punkty)
rysuj_trojkaty(trojkaty)
turtle.onscreenclick(new_point_after_click, btn=1)
#print(trojkaty)
#print(punkty)
#rysuj_punkty(punkty)
#rysuj_trojkaty(p)
turtle.mainloop()
