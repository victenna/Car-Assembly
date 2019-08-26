import turtle
import time
wn=turtle.Screen()
wn.setup(1300,1000)
wn.bgcolor('gold')
wn.bgpic('rd3.gif')
turtle.tracer(2)

text=turtle.Turtle()
text.hideturtle()
text_font=('Arial',15,'bold')
text.up()
text.goto(-400,450)
text.down()
text.write('Build a fire truck shown in the figure on the',font=text_font)
text.up()
text.goto(-400,420)
text.down()
text.write('right dragging the parts of the vehicle',font=text_font)
text.up()
text.goto(-400,390)
text.down()
text.write('with the right button of the computer mouse ',font=text_font)
text.up()
text.goto(-500,320)
text.down()
text.color('blue')
text.write('To move assembled fire truck press "space" button of the keyboard',font=text_font)

class Car(turtle.Turtle):
    
    def __init__(self,X,Y,image):
        super().__init__()
        wn.addshape(image)
        self.shape(image)
        self.up()
        self.goto(X,Y)
        self.down()
t=[0,0,0,0,0,0,0,0]
X=[0,0,0,0,0,0,0,0]
Y=[0,0,0,0,0,0,0,0]

t[0]=Car(520,400,'assembly.gif')
t[0].up()
t[1]=Car(-200,200,'cabin1.gif')
t[1].up()
t[2]=Car(450,-280,'body2.gif')
t[2].up()
t[3]=Car(200,110,'frame1.gif')
t[3].up()
t[4]=Car(-200,50,'wheel1.gif')
t[4].up()
t[5]=Car(-370,180,'wheel2.gif')
t[5].up()
t[6]=Car(300,240,'wheel3.gif')
t[6].up()
t[7]=Car(470,190,'firehose.gif')
t[7].up()

X[2]=450
Y[2]=-280

#cabin
def dragging1(x, y):
    t[1].ondrag(None)
    t[1].goto(x, y)
    t[1].ondrag(dragging1)
    X[1]=t[1].xcor()
    Y[1]=t[1].ycor()
t[1].ondrag(dragging1)

#frame
def dragging3(x, y):
    t[3].ondrag(None)
    t[3].goto(x, y)
    t[3].ondrag(dragging3)
    X[3]=t[3].xcor()
    Y[3]=t[3].ycor()
t[3].ondrag(dragging3)

#wheel_1
def dragging4(x, y):
    t[4].ondrag(None)
    t[4].goto(x, y)
    t[4].ondrag(dragging4)
    X[4]=t[4].xcor()
    Y[4]=t[4].ycor()
t[4].ondrag(dragging4)

#wheel_2
def dragging5(x, y):
    t[5].ondrag(None)
    t[5].goto(x, y)
    t[5].ondrag(dragging5)
    X[5]=t[5].xcor()
    Y[5]=t[5].ycor()
t[5].ondrag(dragging5)

#wheel_3
def dragging6(x, y):
    t[6].ondrag(None)
    t[6].goto(x, y)
    t[6].ondrag(dragging6)
    X[6]=t[6].xcor()
    Y[6]=t[6].ycor()
t[6].ondrag(dragging6)

#firehose
def dragging7(x, y):
    t[7].ondrag(None)
    t[7].goto(x, y)
    t[7].ondrag(dragging7)
    X[7]=t[7].xcor()
    Y[7]=t[7].ycor()
t[7].ondrag(dragging7)
j=-1

def move():
    global j
    delta=2
    while True:
        if (Y[1]<-280 and Y[3]<-330 and Y[4]<350 and Y[5]<-350 and Y[6]<-350 and Y[7]<-270):  
            j=j+1
        if j==600:
            j=0
        for m in range (1,8):
            if m!=0:
                t[m].setposition(X[m]-j*delta,Y[m])
wn.onkey(move,'space')
wn.listen()

