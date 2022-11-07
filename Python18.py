import random
import turtle as t
import random

t.colormode(255)
s = t.Turtle()
color_list = [(202, 164, 110),(236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

s.hideturtle()
s.speed("fastest")
s.penup()
s.setheading(220)
s.forward(420)
s.setheading(0)

num_of_dot = 101

for n in range(1,num_of_dot):
  s.dot(15,random.choice(color_list))
  s.forward(60)

  if n%10 == 0:
    s.setheading(90)
    s.forward(60)
    s.setheading(180)
    s.forward(600)
    s.setheading(0)


screen = t.Screen()
screen.screensize(110,110)
screen.exitonclick()
















###1
# number_of_sides = 3
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# while number_of_sides <= 10:
#     for _ in range(number_of_sides):
#         angle = 360 / number_of_sides
#         turt.forward(100)
#         turt.right(angle)
#     number_of_sides += 1
#     turt.color(random.choice(colors))
###


###2
# turtle.colormode(255)
# turt.pensize(10)
# turt.speed("fastest")
# angle = [0,90,180,270,360]
# def randcolor():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r,g,b)
#     return color
#
# for _ in range(200):
#     turt.forward(10)
#     turt.setheading(random.choice(angle))
#     turt.color(randcolor())
###
# from turtle import Turtle,Screen
# import colorgram




# rgb_color = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

# screen = Screen()
# screen.screensize(150,150)
# screen.bgcolor("white")
# screen.exitonclick()
