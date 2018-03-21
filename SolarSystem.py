# This program creates a minimalist solar system
# Created by: Brandyn Nishida

from Tkinter import *
from random import randint
import time
import math

WIDTH  = 1000
HEIGHT = 800
center = [WIDTH/2,HEIGHT/2]

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg = "#212121")
tk.title("Solar System")
canvas.pack()

class Planet():
  def __init__ (self,planetRadius,radiusToSun,color,angle,speedFactor):
    self.planetRadius = planetRadius
    self.radiusToSun = radiusToSun
    self.color = color
    self.angle = angle
    self.speedFactor = speedFactor
    [x0,y0] = Planet.getPosition(self)
    self.thisPlanet = canvas.create_oval(x0-self.planetRadius,y0-self.planetRadius,
      x0+self.planetRadius,y0+self.planetRadius,fill = self.color, outline = "")
  def getPosition(self):
    x = center[0]+self.radiusToSun*math.cos(self.speedFactor*self.angle)
    y = center[1]+self.radiusToSun*math.sin(self.speedFactor*self.angle)
    return [x,y]
  def updateCoordinates(self):
    self.angle += 0.01
    [xn,yn] = Planet.getPosition(self)
    [xn1,yn1,xn2,yn2] = xn-self.planetRadius,yn-self.planetRadius,xn+self.planetRadius,yn+self.planetRadius
    canvas.coords(self.thisPlanet, xn1,yn1,xn2,yn2)

def stars(numberOfStars):
  starLocations = []
  starRadius = 0.5
  for i in range(numberOfStars):
    starLocations.append([randint(0,WIDTH),randint(0,HEIGHT)])
  for i in range(numberOfStars):
    drawStar = canvas.create_rectangle(starLocations[i][0]-starRadius,starLocations[i][1]-starRadius,
      starLocations[i][0]+starRadius,starLocations[i][1]+starRadius,fill = "white", outline = "")

stars(200)
sun     = Planet(35,0,"orange",0,0)
mercury = Planet(10,75,"#B99289",0,4.14)
venus   = Planet(10,125,"#FF5733",0,1.626)
earth   = Planet(10.5,175,"#0859AD",0,1)
mars    = Planet(10,225,"#FF2D00",0,0.53)
jupiter = Planet(10,275,"#DE654B",0,0.084)
saturn  = Planet(10,325,"#C0B89E",0,0.034)
uranus  = Planet(10,375,"#C0B89E",0,0.012)
neptune = Planet(10,425,"#7ACAEB",0,0.006)

while True:
  mercury.updateCoordinates()
  venus.updateCoordinates()
  earth.updateCoordinates()
  mars.updateCoordinates()
  jupiter.updateCoordinates()
  saturn.updateCoordinates()
  uranus.updateCoordinates()
  neptune.updateCoordinates()
  time.sleep(0.01)
  tk.update()

canvas.mainloop()
