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

class Weapon(Item):
    def __init__(self, name, damage, weapon_type, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.0 if rarity != "legendary" else 1.15

    def equip(self):
        return f"{self.name} is equipped."

    def use(self):
        if self._ownership:
            total_damage = self.damage * self.attack_modifier
            return f"{self.name} is used, dealing {total_damage} damage."
        return super().use()

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


long_bow = Weapon(name='Belthronding', damage=5000, weapon_type='bow', rarity='legendary')
print(long_bow.pick_up('Beleg'))
print(long_bow.equip())
print(long_bow.use())

broken_shield = Shield(name='Wooden Lid', defense=5, broken=True)
print(broken_shield.pick_up('Beleg'))
print(broken_shield.equip())
print(broken_shield.use())
print(broken_shield.throw_away())
print(broken_shield.use())

atk_potion = Potion.from_ability(name='Atk Potion Temp', owner='Beleg', potion_type='attack')
print(atk_potion.use())
