
# is_key_pressed = True


# if is_key_pressed:
#     print("დაჭირა")
# else:
#     print("დაჭირა")


from turtle import *

speed(1)
width(3)

side_length = 400

for i in range(4):
    forward(side_length)
    right(90)

exitonclick()