import turtle
bob=turtle.Turtle()



def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

#teacherpolygon
def polygon(sides, dist):
  angle = 360/sides
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()        
def spiral( times , distance , color , angle ):
    bob.color(color)
    for times in range(10):
      comet(10, 100, "blue", 20)
      bob.width(2)
def comet ( times , distance , color, angle ):
    for times in range(10):
        bob.color(color)
        bob.width(times*2)
        bob.forward(distance)
        bob.left(angle)
def stair( times , distance , angle ):
    for times in range( 2 ):
        bob.forward( distance )
        bob.left( 90 )
        bob.forward( distance )
        bob.right( 90 )

