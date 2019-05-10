import turtle
t=turtle.pen()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

turtle.getscreen()._root.mainloop()
 
t.reset()
for x in range (1,9):
 	t.forwrd(100)
 	t.left(225)
turtle.getscreen()._root.mainloop()

def micuadro(size):
	for x in range(1,5):
		t.forward(size)
		t.left(90)