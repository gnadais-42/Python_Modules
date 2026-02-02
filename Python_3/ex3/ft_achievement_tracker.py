class Player:
    def __init__(self, name, achievements=set()):
        self._name = name
        self._achievements = set(achievements)

    def get_name(self):
        return self._name

    def get_achievements(self):
        return self._achievements

    def add_achievement(self, achievement):
        self._achievements.append(achievement)

    def print_achievements(self):
        print(f"Player {self.get_name()} achievements: "
              f"{self.get_achievements()}")


def unique_set(set1, sets):
    other_sets = set()
    for x in sets:
        if x is not set1:
            other_sets = other_sets.union(x)
    return set1.difference(other_sets)


print("=== Achievement Tracker System ===\n")
achievements = set()
alice = Player("alice", {'first_kill', 'level_10',
                         'treasure_hunter', 'speed_demon'})
bob = Player("bob", {'first_kill', 'level_10',
                     'boss_slayer', 'collector'})
charlie = Player("charlie", {'level_10', 'treasure_hunter', 'boss_slayer',
                 'speed_demon', 'perfectionist'})
sets = (alice.get_achievements(), bob.get_achievements(),
        charlie.get_achievements())
for x in sets:
    achievements = achievements.union(x)
alice.print_achievements()
bob.print_achievements()
charlie.print_achievements()
print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {achievements}")
print(f"Total unique achievements: {len(achievements)}\n")
print(f"Common to all players:"
      f"{alice.get_achievements().intersection(
                      bob.get_achievements(),
                      charlie.get_achievements())}")
not_unique = set()
for set1 in sets:
    for set2 in sets:
        if set1 is not set2:
            not_unique = not_unique.union(set1.intersection(set2))
unique = achievements.difference(not_unique)
print(f"Rare achievements (1 player): {unique}")
print(f"Alice vs Bob common: "
      f"{alice.get_achievements().intersection(bob.get_achievements())}")
alice_unique = unique_set(alice.get_achievements(), sets)
print("Alice unique: "
      f"{alice_unique if len(alice_unique) > 0 else "None"}")
bob_unique = unique_set(bob.get_achievements(), sets)
print("Bob unique: "
      f"{bob_unique if len(bob_unique) > 0 else "None"}")
