class Insect:
    def __init__(self, name="Insect", speed=1, mass=1):
        self.__name = name
        self.__speed = speed
        self.__mass = mass
        self.public_number = 0
        self.public_string = "Str"

    def __init__(self, name = "Insect", speed = 0, mass = 0, public_number = 0, public_string = "1"):
        self.__name = name
        self.__speed = speed
        self.__mass = mass
        self.public_number = public_number
        self.public_string = public_string

    def __del__(self):
        print(f"Insect '{self.__name}' has been destroyed.")

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_mass(self):
        return self.__mass

    def set_name(self, name):
        self.__name = name

    def set_speed(self, speed):
        self.__speed = speed

    def set_mass(self, mass):
        self.__mass = mass

    def __str__(self):
        return f"Insect: {self.__name}, Speed: {self.__speed} m/s, Mass: {self.__mass} g"

    def __repr__(self):
        return f"Insect(name={self.__name}, speed={self.__speed}, mass={self.__mass})"

def main():
    insect1 = Insect("Bee", 15, 0.2, 5, "Fast insect")
    insect2 = Insect("Butterfly", 5, 0.5, 3, "Graceful insect")
    insect3 = Insect("Ant", 0.1, 0.005, 1, "Tiny insect")
    insect4 = Insect()

    print(insect1)
    print(insect2)
    print(insect3)
    print(insect4)

    print(f"{insect1.get_name()} has speed {insect1.get_speed()} m/s and mass {insect1.get_mass()} g.")

main()
