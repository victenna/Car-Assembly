import turtle,random
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
#--------------------------------------------------------------------------------------------------
image=['assembly.gif','body2.gif','cabin1.gif','frame1.gif',\
       'wheel1.gif','wheel2.gif','wheel3.gif','firehose.gif']
t=[]
X=[0,0,0,0,0,0,0,0]
Y=[0,0,0,0,0,0,0,0]
for n in range (8):
    wn.addshape(image[n])
    t.append(turtle.Turtle())
    t[n].up()
    t[n].shape(image[n])
    if n>0:
        t[n].goto(random.randint(-400,400),\
                  random.randint(-300,300))
t[0].goto(520,400)
t[1].goto(450,-300)
for m in range(2,8):
    t[m].ondrag(t[m].goto)
    
j=0
def move():
    global j
    if j==0:
        for m in range(1,8):
            X[m],Y[m]=t[m].position()
    if j==600:
        for m in range(1,8):
            t[m].goto(X[m],Y[m])
            j=0
    delta=5
    j=j+1            
    if (t[2].ycor()<-300 and t[3].ycor()<-300 and t[4].ycor()<-300 and t[5].ycor()<-300\
        and t[6].ycor()<-300 and t[7].ycor()<-300):

        for m in range (1,8):
            t[m].fd(-delta)
    wn.ontimer(move)

wn.onkey(move,'space')
wn.listen()
#-----------------------------------------------------------

