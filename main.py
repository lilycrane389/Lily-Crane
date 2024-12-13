import turtle

screen= turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('Light pink')

t = turtle.Turtle()
t2 = turtle.Turtle()
t2.penup()
t2.hideturtle()

t.penup()

t.goto(0,100)
t.write("My Favorites",font=('arial',28,'bold'),align="center")



t.goto(0,-100)

t.write("Introduction",font=('arial',28,'bold'),align="center")



enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('lavender')
t2.goto(-150,220)
turtle.addshape('sushi.gif')
t2.shape('sushi.gif')
a = t2.stamp()
t2.goto(150,220)
t.goto(0,100)

t2.goto(-150,0)
turtle.addshape('tacos.gif')
t2.shape('tacos.gif')
a = t2.stamp()
t2.goto(-100,0)

t2.goto(150,220)
turtle.addshape('pizza.gif')
t2.shape('pizza.gif')
a = t2.stamp()
t2.goto(-100,0)

t.write("page 2",font=('arial',28,'bold'),align="center")

t.goto(0,-100)

t.write("My favorite foods are tacos, pizza, and sushi",font=('arial',28,'bold'),align="center")

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('hotpink')

t.goto(0,100)
t.write("page3",font=('arial',28,'bold'),align="center")


t.goto(0,-100)

t.write("My favorite hobbies are lifting, soccer, shopping, and hanging out with friends",font=('arial',28,'bold'),align="center")
t2.goto(-150,220)
turtle.addshape('hob.gif')
t2.shape('hob.gif')
a = t2.stamp()
t2.goto(-100,0)

t2.goto(150,220)
turtle.addshape('hob2.gif')
t2.shape('hob2.gif')
a = t2.stamp()
t2.goto(120,0)

t2.goto(150,220)
turtle.addshape('hob3.gif')
t2.shape('hob3.gif')
a = t2.stamp()
t2.goto(120,-220)



enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('light blue')

t.goto(0,100)
t.write("page 4",font=('arial',28,'bold'),align="center")

t.goto(0,-100)

t.write("My favorite movie is Home alone ",font=('arial',28,'bold'),align="center")

t2.goto(-150,220)
turtle.addshape('movie.gif')
t2.shape('movie.gif')
a = t2.stamp()
t2.goto(-100,0)

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('tomato1')

t.goto(0,100)
t.write("page 5",font=('arial',28,'bold'),align="center")

t.goto(0,-100)

t.write("My favorite sport is soccer",font=('arial',28,'bold'),align="center")

t2.goto(-150,220)
turtle.addshape('soccer.gif')
t2.shape('soccer.gif')
a = t2.stamp()
t2.goto(-100,0)

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('SlateBlue')
