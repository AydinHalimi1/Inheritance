class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    def print_person(self):
        print(self.__name,self.__address,self.__phone)
    
class Customer(Person):
    def __init__(self,name,address,phone,custnum,mail):
        Person.__init__(self,name,address,phone)

        self.__custnum = custnum
        self.__mail = mail

    def print_person(self):
        Person.print_person(self)
        print(self.__custnum,self.__mail)




