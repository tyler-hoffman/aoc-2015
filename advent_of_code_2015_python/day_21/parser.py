from advent_of_code_2015_python.day_21.shared import Enemy, Item, ItemCategory, Shop


class Parser(object):
    @staticmethod
    def parse_enemy(input: str) -> Enemy:
        lines = input.strip().splitlines()
        values = [int(line.split(": ")[1]) for line in lines]
        hp, dmg, armor = values
        return Enemy(hp=hp, damage=dmg, armor=armor)

    @staticmethod
    def parse_shop(input: str) -> Shop:
        lines = input.strip().splitlines()
        looking_for_header = True
        category: ItemCategory = ItemCategory.WEAPON  # arbitrary starting point
        weapons: set[Item] = set()
        armors: set[Item] = set()
        rings: set[Item] = set()

        for line in lines:
            if looking_for_header:
                if line.startswith("Weapons"):
                    category = ItemCategory.WEAPON
                elif line.startswith("Armor"):
                    category = ItemCategory.ARMOR
                elif line.startswith("Rings"):
                    category = ItemCategory.RING
                else:
                    assert False, "We can't get here"
                looking_for_header = False
            elif not line.strip():
                looking_for_header = True
            else:
                pieces = line.split()
                name = "".join(pieces[:-3])
                cost, dmg, armor = [int(pieces[x]) for x in range(-3, 0)]
                collection: set[Item]
                match category:
                    case ItemCategory.WEAPON:
                        collection = weapons
                    case ItemCategory.ARMOR:
                        collection = armors
                    case ItemCategory.RING:
                        collection = rings
                collection.add(Item(name=name, cost=cost, damage=dmg, armor=armor))
        return Shop(weapons=weapons, armor=armors, rings=rings)
