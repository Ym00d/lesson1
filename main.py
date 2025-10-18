#print("Hello World")
#print("Hello I'm Github")

#ООП Класи Артибути та методи класів

class Student:
    print("Hello!")
    def __init__(self, height=160):
        self.height=160
        self.age=17

nick=Student()
kate=Student(height=155)
print(nick.height)
print(nick.age)