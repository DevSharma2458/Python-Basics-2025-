# class Point: # Vector
#     def __init__(self, x, y): # x and y coordinates
#         self.x = x
#         self.y = y

#     def sum(self, p):
#         return Point((self.x + p.x), (self.y + p.y))
    
#     def print_point(self):
#         return f"X is {self.x} and y is {self.y}"

# p1 = Point(3, 2)
# p2 = Point(6, 3)

# p = p1.sum(p2)
# p.print_point()
# Overloading here ---------------------------------------------
class Point: # Vector
    def __init__(self, x, y): # x and y coordinates
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print (f"X is {self.x} and Y is {self.y}")
    
    def __add__(self, p):
        return Point((self.x + p.x) ,( self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2)
p = p1 + p2
p.print_point()

'''Operator Overloading- Giving a normal operator (like +, -, ) a new meaning for your custom objects.

Method Overriding- A child class replaces a parent class method with its own version.
'''