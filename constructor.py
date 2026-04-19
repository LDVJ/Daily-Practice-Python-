class Student:

    # constructor
    def __init__(self, name):
        self.name = name
        print("Constructor called for:",self.name)

    #destructor 
    def __del__(self):
        print("Descturor called for: ",self.name)


s1= Student("Alice") # parameterised construtor

print("Object is being usesd.")

# del s1

print("Destruction is done.....")