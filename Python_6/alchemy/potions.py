from .elements import create_fire as fire, create_water as water, \
    create_earth as earth, create_air as air


def healing_potion():
    return f"Healing potion brewed with {fire()} and {water()}"


def strength_potion():
    return f"Healing potion brewed with {earth()} and {fire()}"


def invisibility_potion():
    return f"Invisibility potion brewed with {air()} and {water()}"


def wisdom_potion():
    return "Wisdom potion brewed with all elements: " \
           f"{fire()}, {water()}, {earth()} and {air()}"
