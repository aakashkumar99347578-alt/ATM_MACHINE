#this code is find distance between two points in x and y planes 
# in this code firstly i create a class then create a constructor then magic str method for printing and formate of ponit 
# then create a distance method for calculations 


class Point:

  def __init__(self,x,y):
    self.x_cod = x
    self.y_cod = y

  def __str__(self):
    return '<{},{}>'.format(self.x_cod,self.y_cod)

  def euclidean_distance(self,other):
    return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5


p1= Point(3,4)
p2= Point(5,6)
print(p1.euclidean_distance(p2))

#this code find any point lies on the line yes or no


class Line: #create a line class 

  def __init__(self,A,B,C): #create a constructor and pass the cofficient value of line 
    self.A = A
    self.B = B
    self.C = C

  def __str__(self): #this is magic method for line equtions
    return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)

  def point_on_line(line,point): #this is method for calculted point lies on the point yes or no 
    if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
      return "lies on the line"
    else:
      return "does not lie on the line"
    
  def shortest_distance(line,point):   # this code is calculated shortest distance between line and point 
    return (line.A*point.x_cod + line.B*point.y_cod + line.C) / (line.A**2 +line.B**2)**0.5
  
  def iine_intersect(line,other): #this code is calculated any two lines intersect at point yes or no 
    if line.A/other.A != line.B/other.B :
      return "yes both lines intersecting at any point"
    else :
      return "no both lines intersecting at any point"

  def distance_between_two_points(self,other):
    return ((self.x_cod-other.x_cod)**2 + (self.y_cod - other.y_cod)**2)*0.5
    



l1=Line(5,6,3)
l2=Line(6,5,9)
p3=Point(2,6)
p4=Point(6,7)
print(l1.point_on_line(p3))
print(l1.shortest_distance(p3))
print(l1.iine_intersect(l2))

    



    