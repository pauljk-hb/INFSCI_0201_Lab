class Item:
    def __init__(self, name, description="", rarity="common"):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ""

    def pick_up(self, character: str):
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self):
        self._ownership = ""
        return f"{self.name} is thrown away"

    def use(self):
        if self._ownership:
            return f"{self.name} is used"
        return f"{self.name} has no owner, cannot be used"
    
    def __str__(self):
        if self.rarity == 'legendary':
            return f"*** {self.name} ***\n" \
                   f"Legendary Item - {self.description}\n" \
                   f"★★★★★★\nThis item glows with power!"
        else:
            return f"{self.name}: {self.description} ({self.rarity})"

class Weapon(Item):
    def __init__(self, name, damage, weapon_type, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.0 if rarity != "legendary" else 1.15

    def use(self):
        if self._ownership:
            total_damage = self.damage * self.attack_modifier
            return f"{self.name} is used, dealing {total_damage} damage."
        return super().use()

    def attack_move(self):
        raise NotImplementedError("This method should be overridden in subclasses")
    
    def equip(self):
        return f"{self.name} is equipped."


class SingleHandedWeapon(Weapon):
    def attack_move(self):
        return self._slash()

    def _slash(self):
        return f"{self.name} performs a slashing attack."


class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return self._spin()

    def _spin(self):
        return f"{self.name} performs a spinning attack."


class Pike(Weapon):
    def attack_move(self):
        return self._thrust()

    def _thrust(self):
        return f"{self.name} performs a thrusting attack."


class RangedWeapon(Weapon):
    def attack_move(self):
        return self._shoot()

    def _shoot(self):
        return f"{self.name} shoots an arrow."


class Shield(Item):
    def __init__(self, name, defense, broken=False, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.0 if rarity != "legendary" else 1.10
        self.broken_modifier = 0.5 if broken else 1.0

    def equip(self):
        return f"{self.name} is equipped."

    def use(self):
        if self._ownership:
            total_defense = self.defense * self.defense_modifier * self.broken_modifier
            return f"{self.name} is used, blocking {total_defense} damage."
        return super().use()

class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    def use(self):
        if not self.empty and self._ownership:
            if self.effective_time == 0:
                self.empty = True
            return f"{self.name} is consumed, {self.potion_type} increased by {self.value} for {self.effective_time} seconds."
        return "The potion is empty or has no owner."

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        return cls(name, potion_type, value=50, effective_time=30, rarity="common")

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.backpack = []

    def add_item(self, item):
        """Add item to the inventory and set the owner"""
        if item not in self.backpack:
            item.pick_up(self.owner)
            self.backpack.append(item)
            return f"{item.name} has been added to {self.owner}'s backpack."
        return f"{item.name} is already in the backpack."

    def drop_item(self, item):
        """Remove item from the inventory and reset its ownership"""
        if item in self.backpack:
            item.throw_away() 
            self.backpack.remove(item)
            return f"{item.name} has been removed from {self.owner}'s backpack."
        return f"{item.name} is not in the backpack."

    def view(self, item_type=None):
        """View individual items or a collection of items based on type"""
        if item_type:
            filtered_items = [item for item in self.backpack if isinstance(item, item_type)]
            return [str(item) for item in filtered_items]
        else:
            return [str(item) for item in self.backpack]

    def __iter__(self):
        """Make Inventory iterable"""
        return iter(self.backpack)

    def __contains__(self, item):
        """Support 'in' operator to check item existence in inventory"""
        return item in self.backpack


master_sword = SingleHandedWeapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary')
muramasa = DoubleHandedWeapon(name='Muramasa', damage=580, weapon_type='katana', rarity='legendary')
gungnir = Pike(name='Gungnir', damage=290, weapon_type='spear', rarity='legendary')
belthronding = RangedWeapon(name='Belthronding', damage=500, weapon_type='bow', rarity='legendary')
broken_pot_lid = Shield(name='Broken Pot Lid', defense=5, broken=True)
round_shield = Shield(name='Round Shield', defense=200, broken=False)

beleg_backpack = Inventory(owner='Beleg')

print(beleg_backpack.add_item(belthronding))
print(beleg_backpack.add_item(master_sword))
print(beleg_backpack.add_item(muramasa))
print(beleg_backpack.add_item(gungnir))
print(beleg_backpack.add_item(broken_pot_lid))
print(beleg_backpack.add_item(round_shield))

print("All items in the backpack:")
print(beleg_backpack.view())

print("Shields in the backpack:")
print(beleg_backpack.view(item_type=Shield))

print(beleg_backpack.drop_item(broken_pot_lid))

if master_sword in beleg_backpack:
    master_sword.equip()
    print(master_sword)
    master_sword.use()

for item in beleg_backpack:
    if isinstance(item, Weapon):
        print(f"Weapon in inventory: {item}")