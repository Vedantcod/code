# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
import turtle #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size-5

