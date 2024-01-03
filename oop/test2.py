class User():
    def sign_in(self):
        print("Logged in!")


class Wizard(User) :
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f"Arrow shot! # Arrows Left: {self.num_arrows}")

    def check_arrows(self):
        print(f"{self.num_arrows} remaining...")

    def run(self):
        print('runs really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self,name,num_arrows)
        Wizard.__init__(self,name,power)


# introspection - ability to determine object's type at runtime
# wizard1 = Wizard("Merlin", 60, 'merlin@gmail.com')

hb1 = HybridBorg('Borgie', 50, 100)
hb1.sign_in()