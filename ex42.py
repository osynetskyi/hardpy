# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

# Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		# dog has-a name
		self.name = name
		
	def bark(self):
		print "Woof!"
		
# cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		# cat has-a name
		self.name = name
		
# person is-a object
class Person(object):
	def __init__(self, name):
		# person has-a name
		self.name = name
		
		# person has-a pet of some kind
		self.pet = None
		
	def speak(self):
		print "Hello, my name is", self.name

# employee is-a person
class Employee(Person):
	def __init__(self, name, salary):
		# employee has-a name
		super(Employee, self).__init__(name)
		# employee has-a salary
		self.salary = salary
		
	def speak(self, boast):
		print "Hello, I'm %s %s and my salary is %s" % (boast, self.name, self.salary)
		
# fish is-a object
class Fish(object):
	def swim(self):
		print "Psst"
	
# salmon is-a fish
class Salmon(Fish):
	pass
	
# halibut is-a fish
class Halibut(Fish):
	pass
	

# rover is-a dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")
mary.speak()

# mary has-a pet satan
mary.pet = satan

# frank is-a employee
frank = Employee("Frank", 120000)
#frank.speak()
frank.speak("awesome")

# frank has-a pet rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()
harry.swim()