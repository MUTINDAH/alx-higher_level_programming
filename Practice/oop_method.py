def intro():
    print(f"Name of the father is {father.set_name}, He is {age.set_age} years old")


class Family:
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


father = Family()
father.set_name = "Mbivye"

age = Family()
age.set_age = 30

intro()

# mother = Family ("Mercy Naliaka",28,"Female")
# son = Family ("Liam",4,"Male")
# daughter = Family ("Amani",1,"Female")
# daughter.name="amanda"
# son.age = 25
