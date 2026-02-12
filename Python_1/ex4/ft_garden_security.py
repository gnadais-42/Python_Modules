class SecurePlant():
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_h):
        if new_h < 0:
            print(f"Invalid operation attemped: height {new_h}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = new_h
        print(f"Height updated: {new_h}cm [OK]")

    def set_age(self, new_a):
        if new_a < 0:
            print(f"Invalid operation attemped: age {new_a} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = new_a
        print(f"Age updated: {new_a} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def display_info(self):
        print(f"{self._name}, ({self._height}cm, {self._age} days)")


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, -8)
    print()
    plant.set_height(-5)
    plant.set_age(30)
    print()
    print("Current plant: ", end="")
    plant.display_info()
