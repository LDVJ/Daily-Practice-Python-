class Person:
    # below initialization are kind of default vlues of attributes
    name = "Unkonwn"
    age = 0

    def display(self):
        print("Name: ",self.name)
        print("age: ",self.age)


s1 = Person()
s1.name = "Mike"
s1.age = 14
s1.display() # for this case self is s1

s2 = Person()
s2.name = "Jenny"
s2.age = 13
s2.display() # for this case self is s2 so now self.name is for s2.name and same for age

x = (1,2)
y = (1,2)

print(id(x))
print(id(y))