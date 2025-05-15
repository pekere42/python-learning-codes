import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#e2bbd6") 
drawing_board.title("Drawing Board")

turtle.instance = turtle.Turtle()
turtle.instance.color("#2f2853")

#you should write your side number in both num_sides and range() 
num_sides = 4
angle = 360 / num_sides
side_length = 200

for i in range(4):
    turtle.instance.right(angle)
    turtle.instance.forward(side_length)


#drawing cirle
colors_list = ["red","blue","black","white","purple","pink","yellow","green"]
for i in range(10):
    turtle.instance.color(colors_list[i % len(colors_list)])
    turtle.instance.circle(20 + i*2)
    turtle.instance.left(10)
turtle.done()