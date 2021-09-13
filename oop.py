
class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1


my_rocket = Rocket()
print(my_rocket)
