##import jieba
##sm="我爱中国"
##c=jieba.lcut(sm)
##print(c)
##a, b,c=eval(input())
##ls=[]
##for i in range(c):
##    ls.append(a+b*1)
##print(ls)

##import random
##s=input()
##ls=[]
##for i in range(26):
##    ls.append(chr(ord('a')+i))
##for i in range(10):
##    ls.append(chr(ord('0')+i))
##
##random.seed(eval(s))
##for i in range(10):
##    for i in range(8):
##        print(random.choice(ls),end='')
##    print()

##import turtle
##turtle.seth(-30)
##turtle.fd(200)
##turtle.right(120)
##turtle.fd(200)
##turtle.right(60)
##turtle.fd(200)
##turtle.right(120)
##turtle.fd(200)

##import turtle
##turtle.pensize(2)
##d=-45
##for i in range(4):
##    turtle.seth(d)
##    d+=90
##    turtle.fd(200)

##import turtle
##for i in range(4):
##    turtle.fd(100)
##    turtle.fd(-100)
##    turtle.seth((i+1)*90)

##import turtle
##
##
##turtle.left(30)
##turtle.fd(100)
##
##turtle.seth(30)
##turtle.fd(100)
##
##turtle.right(30)
##turtle.fd(100)

##import turtle as t
##for i in range(3):
##    t.seth(i*120)
##    t.fd(200)
##
##import turtle
##turtle.pensize(2)
##d=0
##for i in range(1,9):
##    turtle.fd(100)
##    d+=45
##    turtle.seth(d)

##import turtle
##turtle.pensize(20)
##d=0
####for i in range(5):
##for i in range(1,6):
##    turtle.fd(100) 
##    d+=72
##    turtle.seth(d)

##import turtle
##d=0
##turtle.pensize(2)
##for i in range(1,13):
##    turtle.fd(40)
##    d+=30
##    turtle.seth(d)
##    
    
##import turtle
##turtle.pensize(2)
##for i in range(4):
##    turtle.fd(200)
##    turtle.left(90)
##turtle.left(-45)
##turtle.circle(100*pow(2,0.5))

##
##import turtle as t
##import random as r
##color=['red','orange','blue','green','purple']
##r.seed(1)
##for i in range(5):
##    rad=r.randint(20,50)
##    x0=r.randint(-100,100)
##    y0=r.randint(-100,100)
##    t.color(r.choice(color))
##    t.penup()
##    t.goto(x0,y0)
##    t.pendown()
##    t.circle(rad)
##t.done()

##import turtle as t
##import random as r
##
##r.seed(1)
##t.pensize(2)
##t.pencolor('red')
##angles=7
##points=[[0,0],[50,40],[70,80],[-40,30]]
##
##for i in range(len(points)):
##    x0,y0=points[i]
##    t.penup()
##    t.goto(x0,y0)
##    t.pendown()
##
##    length=r.randint(6,16)
##    for j in range(angles):
##        t.forward(length)
##        t.backward(length)
##        t.right(360/angles)
##t.done()


##import turtle as t
##import random as r
##r.seed(1)
##t.pensize(2)
##for i in range(3):
##    length=r.randint(20,80)
##    x0=r.randint(-100,100)
##    y0=r.randint(-100,100)
##
##    t.penup()
##    t.goto(x0,y0)
##    t.pendown()
##    for j in range(4):
##        t.forward(length)
##        t.setheading(90*(j+1))
##t.done()

##import turtle as t
##ls=[300,292,33,131,61,254]
##x_len=400
##y_len=300
##x0=-200
##y0=-100
##
##t.penup()
##t.goto(x0,y0)
##t.pendown()
##
##t.fd(x_len)
##t.fd(-x_len)
##t.seth(90)
##t.fd(y_len)
##t.pencolor('red')
##t.pensize(5)
##for i in range(len(ls)):
##    t.penup()
##    t.goto(x0+(i+1)*50,y0)
##    t.seth(90)
##    t.pendown()
##    t.fd(ls[i])
##t.done()
