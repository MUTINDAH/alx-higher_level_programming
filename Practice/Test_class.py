class Employee:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def getemail(self):
        return f"{self.first}.{self.last}@company.com"


emp1 = Employee("Peter", "Mutinda", "peter.mutinda@gmail.com")
emp2 = Employee("Liam", "Mbivye", "liam.mbivye@gmail.com")

print(emp2.getemail())
