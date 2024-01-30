class Masala:
    def __init__(self, a:int):
        self.a=a
    def qaytar(self)->int:
        if self.a<0:
            return """manfiy"""
        return """musbat"""

son=int(input())

a=Masala(son)
print(a.qaytar())
       
        