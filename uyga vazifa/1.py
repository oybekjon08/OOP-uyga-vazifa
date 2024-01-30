
class Employee:
    def __init__(self, id, firstName, lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    
    def getID(self) -> int:
        return self.id
    
    def getFirstName(self) -> str:
        return self.firstName

    def getName(self) -> str:
        return f"{self.firstName} {self.lastName}"

    def setSalary(self, newSalary: int) -> None:
        self.salary = newSalary
    
    def getAnnualSalary(self) -> int:
        return self.salary * 12

    def raiseSalary(self, percent: int) -> int:
        return self.salary + self.salary * (percent / 100)

    def toString(self):
        return f"""
id:      {self.id}
name:    {self.getName()}
salary:  {self.salary}
"""


emp = Employee(1, "Eshmat", "G'ishmatov", 5600)
print(emp.getID())
print(emp.getFirstName())
print(emp.getName())

print(emp.salary)
emp.setSalary(26000)
print(emp.salary)
print(emp.getAnnualSalary())
print(emp.raiseSalary(10))

print(emp.toString())

