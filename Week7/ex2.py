from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def create_product(self, kind=None):
        pass

class DogFactory(Factory):
    def create_product(self, kind=None):
        return Dog()

class CatFactory(Factory):
    def create_product(self, kind=None):
        return Cat()

class Animals(ABC):
    @abstractmethod
    def run(self):
        pass

class Dog(Animals):
    def run(self):
        print("I'm a Dog, I can run!!")

class Cat(Animals):
    def run(self):
        print("I'm a Cat, Run!!")

# Client
factory = DogFactory()
dog = factory.create_product()
dog.run()
