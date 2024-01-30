class Employes:
    def __init__(self, id:int, name:str, last_name:str, salary:int):
        self.id=id
        self.name=name
        self.last_name=last_name
        self.salary=salary
    def get_id(self):
        return self.id
    def first_name(self):
        return self.name
    def familya(self):
        return self.last_name
    def maosh(self):
        return self.salary
    def AnnualSalary(self):
        yillik=self.salary*12
        return yillik
    def foiz(self, protsent:int):
        return self.salary+self.salary*protsent
        
    def chiqar(self):
        return f""" 
    id: {self.get_id()}
    ism:{self.first_name()}
    familiya: {self.familya()}
    maosh: {self.maosh()}
    yillik maosh: {self.AnnualSalary()}
    foiz : {self.foiz(20)}    
    """

odam=Employes(20022, "Oybek", "Rasulov", 10)
print(odam.chiqar())


    
    