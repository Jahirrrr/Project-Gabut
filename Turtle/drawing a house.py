## Project Gabut
## Drawing a Houae with Turtle Graphics
## Code by me

import turtle


t = turtle.Turtle()

t.pen(pensize=3, speed=2, pencolor="purple")

def gambar_cerobong(t, width, height):
	t.hideturtle()
	t.forward(width)
	t.left(90)
	t.forward(height)
	t.left(90)
	t.forward(width)
	t.left(90)
	t.forward(height)
	t.left(90)

def main ():
	t.hideturtle()
	t.right(90)
	t.forward(100)
	t.left(90)
	t.backward(200)
	t.left(90)
	t.forward(100)
	t.right(90)
	t.forward(200)
	t.left(133)
	t.forward(145)
	t.left(94)
	t.forward(150)
	t.backward(160)
	t.right(230)
	t.forward(230)
	t.right(90)
	t.forward(104)
	t.right(89)
	t.forward(135)
	t.backward(130)
	t.left(90)
	t.forward(102)
	t.right(90)
	t.forward(145)
	for i in range (1):
		t.penup()
		t.forward(130)
		t.pendown()
		t.left(50)
		t.forward(180)
		t.backward(170)
		t.left(135)
		t.forward(100)
		t.right(135)
		t.forward(200)
		for i in range (1):
			t.penup()
			t.backward(200)
			t.right(50)
			t.forward(70)
			t.pendown()
			t.right(90)
			t.forward(70)
			t.right(90)
			t.forward(60)
			t.right(90)
			t.forward(70)
			for i in  range (1):
				t.penup()
				t.backward(60)
				t.left(90)
				t.forward(90)
				t.pendown()
				t.right(90)
				t.forward(40)
				t.left(90)
				t.forward(30)
				t.left(90)
				t.forward(40)
				t.left(90)
				t.forward(30)
				for i in range (1):
					t.penup()
					t.left(180)
					t.forward(60)
					t.right(90)
					t.pendown()
					t.forward(30)
					t.left(90)
					t.forward(30)
					t.left(90)
					t.forward(30)
					t.left(90)
					t.forward(30)
					for i in range (1):
						t.penup()
						t.right(90)
						t.forward(145)
						t.pendown()
						gambar_cerobong(t, 40, 50)



if __name__ == "__main__":
    main()
