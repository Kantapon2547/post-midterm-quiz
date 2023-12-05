class Human:
    def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def getage(self):
        return self.__age

    def setage(self, age):
        if age <= 0 or age > 100:
            raise ValueError
        self.__age = age

    def eat(self):
        print("I can eat.")

    def sleep(self):
        print("I can sleep.")


class Student(Human):
    def __init__(self, name, age, email, grade):
        super().__init__(name, age)
        self.__email = email
        self.__grade = grade


person = Human()

person.setname("Mammoth")
person.setage(19)

person.eat()
person.sleep()

print(person.getname())
print(person.getage())




