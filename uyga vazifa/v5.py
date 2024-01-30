class Restangle:
    def __init__(self, heght:int, width:int):
        self.height=heght
        self.width=width
    def boyi(self):
        return self.height
    def eni (self):
        return self.width
    def change_boyi(self, change_height:int):
        self.height=change_height
        return self.height
    def change_eni(self, change_width:int):
        self.width=change_width
        return self.width
    def kv(self):
        return (self.width+self.height)*2
    def yuza(self):
        return self.height*self.height
    def restange_info(self):
        return f"""
    boyi : {self.boyi()}
    eni :  {self.eni()}
    ozgartirilgan boyi : {self.change_boyi(50)}
    ozgartirilgan eni : {self.change_eni(60)}
    kv : {self.kv()}
    yuza : {self.yuza()}
    """
a1=Restangle(10, 20)
print(a1.boyi())
print(a1.change_boyi(50))
print(a1.eni())
print(a1.change_eni(30))
print(a1.kv())
print(a1.yuza())
print(a1.restange_info())

