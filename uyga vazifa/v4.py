class Circle:
    def __init__ (self, radius:int, color:str):
        self.radius=radius
        self.color=color
    def get_radius(self):
        return self.radius
    def set_radius(self, newRadius:int):
        self.radius=newRadius
    def get_color(self):
        return self.color
    def set_color(self, newColor:str):
        self.color=newColor
    def yuza(self):
        return self.radius**2*3.14
    def aylana_uzunligi(self):
        return 2*self.radius*3.14
    def info(self):
        return f"""
    aylana radiusi  : {self.radius}
    aylana rangi    : {self.color}
    aylana yuzasi   : {self.yuza()}
    aylana uzunligi : {self.aylana_uzunligi()}    
    """
a=Circle(10, "blue")
print(a.get_radius())
print(a.get_color())
a.set_radius(20)
a.set_color("white")
print(a.yuza())
print(a.aylana_uzunligi())
print(a.info())