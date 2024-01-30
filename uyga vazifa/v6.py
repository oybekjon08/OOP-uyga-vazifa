class Date:
    def __init__(self, day: int, month:int, year:int):
        self.day=day
        self.month=month
        self.year=year
    
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year
    def set_day(self, kun:int) -> None:
        self.day=kun
    def set_month(self, oy:int) -> None:
        self.month=oy
    def set_year(self, yil:int) -> None:
        self.year=yil
    def set_data(self, bugun:int, oyi:int, yili:int) -> None:
        self.sana=f"""{bugun}/{oyi}/{yili}"""
    def to_string(self):
        return f"""
    eski sana : {self.get_day()}/{self.get_month()}/{self.get_year()}
    yangi kun : {self.day}
    yangi oy  : {self.month}
    yangi yil : {self.year}
    
    bu yangilantirilgalari 
    {self.day}/{self.month}/{self.year}
      
    """
        
a=Date(10, 5, 2021)
print(f"\t{a.get_day()}/{a.get_month()}/{a.get_year()}" )
print(a.to_string())
a.set_day(5)
a.set_month(10)
a.set_year(2028)
print(a.to_string())
