class Warrior():
    def __init__(self, name, power, endurance, hair_colour):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_colour = hair_colour

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 1

    def hit(self):
        print(f'{self.name} бьет кого-то')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} гуляет')

    def info(self):
        print(f'имя воина - {self.name}')
        print(f'цвет волос - {self.hair_colour}')
        print(f'сила воина - {self.power}')
        print(f'выносливость воина - {self.endurance}')

war1 = Warrior('Степа', 76, 45, 'коричневый')
war2 = Warrior('Егор', 76, 45, 'блонд')

# war1.sleep()
# war1.eat()
# war1.hit()
# war1.walk()
# war1.info()

print(war1.name)
print(war2.power)
print(war1.endurance)
print(war1.hair_colour)



