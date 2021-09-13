
class Rocket:
    def __init__(self, x, y, velocity=5):
        self.x = x
        self.y = y
        self.base_y = 20
        self.velocity = velocity

    def move_up(self):
        self.y -= self.velocity


my_rockets = [Rocket(x, 20) for x in range(0, 5)]
for instance in my_rockets:
    instance.move_up()
    print(instance.x, instance.y)



