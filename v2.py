class Juft:
    def __init__(self, son:int) :
        self.son=son
    def qaytar(self):
        if self.son%2==0:
            return """juft"""
        return """toq"""

a=int(input())
m=Juft(a)
print(m.qaytar())