# A simple function 
def greet_user(): 
    """Display a simple greeting.""" 
    print("Hello!") 
greet_user() 

#Passing an argument 
def greet_user(username): 
    """Display a personalized greeting.""" 
    print("Hello, " + username + "!") 
greet_user('jesse') 

#Default values for parameters 
def make_pizza(topping='bacon'): 
    """Make a single-topping pizza.""" 
    print("Have a " + topping + " pizza!") 
make_pizza() 
make_pizza('pepperoni') 

#Returning a value 
def add_numbers(x, y): 
    """Add two numbers and return the sum.""" 
    return x + y 
sum = add_numbers(3, 5)
print(sum)

#Creating a dog class 
class Dog(): 
    """Represent a dog.""" 
    def init(self, name): 
        """Initialize dog object.""" 
        self.name = name 
    def sit(self): 
        """Simulate sitting.""" 
        print(self.name + " is sitting.") 

my_dog = Dog('Peso') 
print(my_dog.name + " is a great dog!") 
my_dog.sit() 

#Inheritance 
class SARDog(Dog): 
    """Represent a search dog.""" 
    def init(self, name): 
        """Initialize the sardog.""" 
        super().init(name) 
    def search(self): 
        """Simulate searching.""" 
        print(self.name + " is searching.") 
my_dog = SARDog('Willie') 
print(my_dog.name + " is a search dog.") 
my_dog.sit() 
my_dog.search()