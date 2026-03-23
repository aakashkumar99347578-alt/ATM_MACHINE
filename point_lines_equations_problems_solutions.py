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
