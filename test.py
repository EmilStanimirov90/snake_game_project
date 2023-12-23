import random

class Knight:
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.items = []

    def attack_monster(self):
        return random.randint(5, self.attack)

    def defend(self, damage):
        actual_damage = damage - self.defense
        if actual_damage > 0:
            self.health -= actual_damage

    def get_item(self, item):
        self.items.append(item)
        self.update_stats()

    def update_stats(self):
        # Example: Update knight's stats based on collected items
        for item in self.items:
            if item == 'Sword':
                self.attack += 5
            elif item == 'Armor':
                self.defense += 3


class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_knight(self):
        return random.randint(3, self.attack)


def main():
    knight = Knight()
    monsters = [
        Monster('Goblin', 30, 8),
        Monster('Orc', 50, 12),
        Monster('Dragon', 80, 18)
    ]

    print("Knight's stats: Health={}, Attack={}, Defense={}".format(knight.health, knight.attack, knight.defense))
    print("Let the battle begin!")

    while knight.health > 0:
        monster = random.choice(monsters)
        print(f"A {monster.name} appears!")

        while monster.health > 0:
            knight_damage = knight.attack_monster()
            monster.defend(knight_damage)
            print(f"Knight attacks {monster.name} for {knight_damage} damage!")

            if monster.health <= 0:
                print(f"{monster.name} defeated!")
                dropped_item = random.choice(['Sword', 'Armor'])
                print(f"{monster.name} dropped a {dropped_item}!")
                knight.get_item(dropped_item)
                break

            monster_damage = monster.attack_knight()
            knight.defend(monster_damage)
            print(f"{monster.name} attacks Knight for {monster_damage} damage!")
            print(f"Knight's health: {knight.health}")

        print("Knight rests before the next battle...")
        print()

    print("Game over! The knight has been defeated.")


if __name__ == "__main__":
    main()