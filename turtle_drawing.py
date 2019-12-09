import turtle as tl

tl.shape("turtle")
tl.speed(8)
tl.left(45)
for i in range(1,500):
	tl.color("Blue")
	tl.forward(i)
	tl.left(90)
	tl.color("red")
	tl.forward(i)
	tl.left(90)

tl.exitonclick()