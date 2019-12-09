import turtle as tl

def fib(n):
	if n == 1:
		return 1
	if n == 0:
		return 0
	return fib(n-1) + fib(n-2)




tl.shape("turtle")
tl.speed(8)
tl.left(45)
for i in range(10,500):
	tl.forward(i)
	tl.left(120)

tl.exitonclick()