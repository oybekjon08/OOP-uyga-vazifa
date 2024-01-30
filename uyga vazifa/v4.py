class Circle:
    def __init__(self, radius:int, color:str):
        self.radius=radius
        self.color=color
    def get_radius(self):
        a=self.radius
        return a
    def set_radius(self, new_radius:int):
        self.radius=new_radius
        print(self.radius)
    def get_color(self):
        return self.color
    def set_color(self, new_color:str):
        self.color=new_color
        return self.color
    def get_area(self):
        return self.radius**2*3.14
    def circuremence (self):
        return 2*3.14*self.radius
    def get_info(self):
        return f"""
    radius:             {self.get_radius()}
    color :             {self.get_color()}
    change radius :     {self.set_radius(100)}
    change color :      {self.set_color("blue")}
    S:                  {self.get_area()}
    C:                  {self.circuremence()}
    """
    


o1=Circle(10, "red")
print(o1.get_radius())
print(o1.set_radius(100))
print(o1.get_color())
print(o1.get_area())
print(o1.set_color("blue"))
print(o1.get_area())
print(o1.circuremence())
print(o1.get_info())