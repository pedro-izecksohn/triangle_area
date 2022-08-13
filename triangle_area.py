#!/usr/bin/python3
from math import sqrt

class Point:
  def __init__ (self, x, y):
    self.x = x
    self.y = y
  def distance (self, other):
    xd = self.x-other.x
    xds = xd*xd
    yd = self.y-other.y
    yds = yd*yd
    return sqrt (xds+yds)

def triangleArea (a ,b ,c):
  sidea = a.distance (b)
  sideb = b.distance (c)
  sidec = c.distance (a)
  s = (sidea+sideb+sidec)/2
  return sqrt(s*(s-sidea)*(s-sideb)*(s-sidec))

print ("Area of triangle\nBy: Pedro Izecksohn on August 13 of 2022")
ax = float (input ("Enter A.x: "))
ay = float (input ("Enter A.y: "))
a = Point (ax, ay)
bx = float (input ("Enter B.x: "))
by = float (input ("Enter B.y: "))
b = Point (bx, by)
cx = float (input ("Enter C.x: "))
cy = float (input ("Enter C.y: "))
c = Point (cx, cy)
print (triangleArea (a, b, c))
