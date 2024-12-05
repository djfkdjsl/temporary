# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:05:36 2024

@author: user
"""

tom = 27
Alice = 29

def age_up():
    global tom
    global Alice
    tom +=1
    Alice +=1
    
def tom_year():
    return tom
    
def alice_year():
    return Alice


def main(): #그냥함수이름임
    print("2024년 tom : %d\n2024년 Alice : %d" %(tom_year(), alice_year()))
    age_up()
    print("2025년 tom : %d\n2025년 Alice : %d" %(tom_year(), alice_year()))
    
main()

#%%

class AgePgm:
  
    def age_up(self):
        self.age+=1
    def get_age(self):
        return self.age
def main():
    tom = AgePgm()
    tom.age = 27
    print("2024년 tom : ",tom.get_age())
    tom.age_up()
    print("2025년 tom : ",tom.get_age())
main()

#%%
class AgePgm:
  
    def age_up(self):
        self.age+=1
    def get_age(self):
        return self.age


def main():
    tom = AgePgm()
    alice = AgePgm()
    milk = AgePgm()
    tom.age = 27
    alice.age = 29
    milk.age = 22
    sum = tom.get_age()+alice.get_age()+milk.get_age()
    
    print("2024 sum : ",tom.get_age()+alice.get_age()+milk.get_age()) 
    tom.age_up()
    alice.age_up()
    milk.age_up()
    sum = tom.get_age()+alice.get_age()+milk.get_age()

    print("2025년 sum : ",sum)
main()
#%%
class AgePgm:
  
    def age_up(self):
        self.age+=1
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age

def main():
    tom = AgePgm()
    alice = AgePgm()
    milk = AgePgm()
    tom.set_age(27)
    alice.set_age(29)
    milk.set_age(22)
    sum = tom.get_age()+alice.get_age()+milk.get_age()
    
    print("2024 sum : ",tom.get_age()+alice.get_age()+milk.get_age()) 
    tom.age_up()
    alice.age_up()
    milk.age_up()
    sum = tom.get_age()+alice.get_age()+milk.get_age()

    print("2025년 sum : ",sum)
main()

#%%

class korea:
    def __init__(self,num1):
        self.num1=num1
    def show_pgm(self,cnt):
        print(self.num1*cnt)
        
def main():
    k1 = korea("Python_PGM ")
    k2 = korea("OOP\t")
    
    k1.show_pgm(2)
    k2.show_pgm(3)
    
main()
    

#%%

class Phone_Book:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_name(self,name):
        self.name=name
    def set_phone(self,phone):
        self.phone=phone
    def show_info(self):
        print("name : ",self.name)
        print("phone : ",self.phone)
na = input("name : ")
ph = input("phone(xxx-xxxx-xxxx) : ")
i_v = Phone_Book(na,ph)
print(i_v.get_name(), i_v.get_phone())
i_v.show_info()        
