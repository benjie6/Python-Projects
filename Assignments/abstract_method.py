from abc import ABC, abstractmethod
# abc is a builtin module, we have to import ABC and abstractmethod

class Animal(ABC): # Inherit from ABC(Abstract base class)
    @abstractmethod  
    def do(self, action): 
        pass
    
    def regular_method(self):
        print("This is a regular method in the Animal class.")

class dog(Animal): 
    def do(self, action, time): 
        print(f"{action} a dog! At {time}") 

class cat(Animal): 
    def do(self, action, time): 
        print(f"{action} a cat! At {time}") 

zoo = [dog(), cat()]

for animal in zoo:
    animal.do(action="feeding", time="9:30")
    animal.regular_method()
