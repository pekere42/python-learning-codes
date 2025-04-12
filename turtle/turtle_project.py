import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("blue")
drawing_board.title("Python Turtle")
#üst taraf rengi ve ismini belirledi renk kısmında hex kodlarıyla özelleştirme yapılabilir



#turtle.instance = turtle.Turtle()#bu her kodda var turtleı tanımlamak için kesin gerekli
""" alttaki kod kare için for versiyonu da var
turtle.instance = turtle.Turtle()
x = 0
while x < 4:
    turtle.instance.forward(200)
    turtle.instance.right(90)
    x += 1
turtle.done()
"""
"""
#yildiz oluşturma
turtle.instance = turtle.Turtle()
x = 0
while x < 5:
    turtle.instance.right(144)
    turtle.instance.forward(200)
    x += 1
turtle.done()
"""

#çokgen oluşturma kodu num_sides ve range değiştirerek değiştirilir
turtle.instance = turtle.Turtle()
num_sides = 5
angle = 360 / num_sides
side_length = 200
for i in range(5):
    turtle.instance.right(angle)
    turtle.instance.forward(side_length)
turtle.done()








#turtle.done()#bu kod turtleın açık kalmasını sağlıyor(kod bir daha çalışmıyor ama uygulama açık kalıyor)

import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("red")
turtle_screen.title("cycle project")


turtle_instance = turtle.Turtle()
turtle_instance.color("dark blue")

colors_list = ["red","blue","black","white","purple","pink","yellow","green"]
for i in range(20):
    turtle_instance.color(colors_list[i % 7])#20 tane renk yok hepsinin çalışabilmei için yöntem
    turtle_instance.circle(i * 5)#bir sürü yöntem var bu da bir tane dekorasyon yöntemi
    turtle_instance.circle(i * -5)



turtle.mainloop()# bu da olur turtle.done() da olur


import turtle

turtle_hareket_edecek = turtle.Screen()
turtle_hareket_edecek.bgcolor("red")
turtle_hareket_edecek.title("interaktif_hareket")
turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
#klavyeden basınca hareket edilmesini sağlayan yöntem
def interaktif_turtle():
    turtle_instance.forward(100)
def turn_angle_right():
    #turtle_instance.right(90)
    turtle_instance.setheading(turtle_instance.heading()+10)
def turn_angle_left():
    #turtle_instance.left(90)
    turtle_instance.setheading(turtle_instance.heading()-10)
def clear_screen():
    turtle_instance.clear()
def return_home():
    turtle_instance.home()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()





turtle_hareket_edecek.listen()
turtle_hareket_edecek.onkey(fun=interaktif_turtle, key="space")
turtle_hareket_edecek.onkey(fun=turn_angle_right, key="Down")
turtle_hareket_edecek.onkey(fun=turn_angle_left, key="Up")
turtle_hareket_edecek.onkey(fun=clear_screen, key="c")
turtle_hareket_edecek.onkey(fun=return_home, key="j")
turtle_hareket_edecek.onkey(fun=turtle_pen_up, key="a")
turtle_hareket_edecek.onkey(fun=turtle_pen_down, key="d")
turtle.mainloop()