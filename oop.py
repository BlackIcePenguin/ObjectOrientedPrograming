
class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_rocket(self, width, height):
        self.x += width
        self.y += height

    def get_distance(self, rocket):
        a = self.x - rocket.x
        b = self.y - rocket.y
        distance = (a ** 2 + b ** 2) ** (1/2)
        print(distance)


my_rockets = [Rocket(x, 0) for x in range(0, 5)]
for instance in my_rockets:
    instance.move_rocket(20, -3)
    print(instance.x, instance.y)

Alpha = Rocket(5, 10)
Beta = Rocket(0, 2)
Gamma = Rocket(1, -9)
Delta = Rocket(-3, 6)


Alpha.get_distance(Beta)
Alpha.get_distance(Delta)
Alpha.get_distance(Gamma)
Delta.get_distance(Beta)
Delta.get_distance(Gamma)


# Rocket Attributes #
class RocketTwo:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.velocity = 5

    def move_rocket(self, width, height):
        self.x += width
        self.y += height

    def get_distance(self, rocket):
        a = self.x - rocket.x
        b = self.y - rocket.y
        distance = (a ** 2 + b ** 2) ** (1/2)
        print(distance)


Epsilon = RocketTwo(0, 0, 8)
print(Epsilon.size, Epsilon.velocity)
Zeta = RocketTwo(0, 0, 10)
Eta = RocketTwo(0, 0, 2)
Theta = RocketTwo(0, 0, 15)
print(Epsilon.size, Epsilon.velocity)
print(Zeta.size, Zeta.velocity)
print(Eta.size, Eta.velocity)
print(Theta.size, Theta.velocity)


# Rocket Methods #
class RocketThree:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.velocity = 5

    def move_rocket(self, width, height):
        self.x += width
        self.y += height

    def get_distance(self, rocket):
        a = self.x - rocket.x
        b = self.y - rocket.y
        distance = (a ** 2 + b ** 2) ** (1/2)
        return distance

    def land_rocket(self):
        self.x = 0
        self.y = 0

    def launch_phrase(self):
        print(f'Houston, {self.name} has achieved Liftoff!')

    def safety_check(self, rocket):
        distance = self.get_distance(rocket)
        if distance >= 4:
            print('No danger, rockets have enough distance')
        elif distance == 0.0:
            print('CRITICAL ERROR, ROCKETS HAVE COLLIDED')
        elif distance < 4:
            print('WARNING: TOO CLOSE TO ROCKET, MOVE AWAY NOW')

        else:
            print('Invalid Results')


Iota = RocketThree(0, 5, 'Iota')
Kappa = RocketThree(5, 10, 'Kappa')
Lambda = RocketThree(0, 3, 'Lambda')
Mu = RocketThree(0, 5, 'Mu')
Kappa.launch_phrase()
Iota.safety_check(Kappa)
Iota.safety_check(Lambda)
Iota.safety_check(Mu)
print(Kappa.x, Kappa.y)
Lambda.land_rocket()
print(Kappa.x, Kappa.y)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
        print(f'Hello there, my name is {self.name}')

    def age_person(self):
        self.age += 1


Albert = Person('Albert', 19, 'Male')
print(Albert.name, Albert.age, Albert.gender)
Albert.introduction()
Albert.age_person()
print(Albert.name, Albert.age, Albert.gender)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f'The car is a {self.make} {self.model} made in\n'
              f'the year {self.year}, and has not had any accidents')


Stick = Car('Subaru', 'Outback', '2004')
Stick.describe_car()
