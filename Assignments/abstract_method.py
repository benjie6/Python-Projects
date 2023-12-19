from abc import ABC,abstractmethod 

class Animal(ABC):
    @abstractmethod  
    def do(self, action): 
        pass

class dog(Animal): 
    def do(self, action, time): 
        print(f"{action} a dog! At {time}") 

class cat(Animal): 
    def do(self, action, time): 
        print(f"{action} a cat! At {time}") 

zoo = [dog(), cat()]

for animal in zoo:
    animal.do(action="feeding", time="9:30 am")
