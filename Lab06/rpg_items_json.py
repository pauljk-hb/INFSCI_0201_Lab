import json

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

    def to_json(self):
        """Convert the item to a JSON-encodable dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'ownership': self._ownership
        }
    
    def __str__(self):
        if self.rarity == 'legendary':
            return f"*** {self.name} ***\nLegendary Item - {self.description}\n★★★★★★\nThis item glows with power!"
        else:
            return f"{self.name}: {self.description} ({self.rarity})"

    @classmethod
    def from_json(cls, data:json):
        """Create an item instance from a JSON dictionary"""
        item = cls(data['name'], data['description'], data['rarity'])
        item._ownership = data['ownership']
        return item


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
    
    def equip(self):
        return f"{self.name} is equipped."

    def to_json(self):
        data = super().to_json()
        data.update({
            'damage': self.damage,
            'weapon_type': self.weapon_type,
            'attack_modifier': self.attack_modifier
        })
        return data

    @classmethod
    def from_json(cls, data:json):
        weapon = cls(data['name'], data['damage'], data['weapon_type'], data['rarity'])
        weapon._ownership = data['ownership']
        return weapon

    def equip(self):
        return f"{self.name} is equipped."


class Shield(Item):
    def __init__(self, name, defense, broken=False, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.0 if rarity != "legendary" else 1.10

    def equip(self):
        return f"{self.name} is equipped."
    
    def use(self):
        if self._ownership:
            total_defense = self.defense * self.defense_modifier * self.broken_modifier
            return f"{self.name} is used, blocking {total_defense} damage."
        return super().use()

    def to_json(self):
        data = super().to_json()
        data.update({
            'defense': self.defense,
            'broken': self.broken,
            'defense_modifier': self.defense_modifier
        })
        return data

    @classmethod
    def from_json(cls, data:json):
        shield = cls(data['name'], data['defense'], data['broken'], data['rarity'])
        shield._ownership = data['ownership']
        return shield


class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time

    def to_json(self):
        data = super().to_json()
        data.update({
            'potion_type': self.potion_type,
            'value': self.value,
            'effective_time': self.effective_time
        })
        return data
    
    @classmethod
    def from_ability(cls, name, owner, potion_type):
        return cls(name, potion_type, value=50, effective_time=30, rarity="common")

    @classmethod
    def from_json(cls, data:json):
        potion = cls(data['name'], data['potion_type'], data['value'], data['effective_time'], data['rarity'])
        potion._ownership = data['ownership']
        return potion


class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.backpack = []

    def add_item(self, item):
        if item not in self.backpack:
            item.pick_up(self.owner)
            self.backpack.append(item)
            return f"{item.name} has been added to {self.owner}'s backpack."
        return f"{item.name} is already in the backpack."

    def drop_item(self, item):
        if item in self.backpack:
            item.throw_away()
            self.backpack.remove(item)
            return f"{item.name} has been removed from {self.owner}'s backpack."
        return f"{item.name} is not in the backpack."

    def to_json(self):
        return {
            'owner': self.owner,
            'backpack': [item.to_json() for item in self.backpack]
        }

    @classmethod
    def from_json(cls, data:json):
        inventory = cls(data['owner'])
        for item_data in data['backpack']:
            if 'weapon_type' in item_data:
                inventory.add_item(Weapon.from_json(item_data))
            elif 'defense' in item_data:
                inventory.add_item(Shield.from_json(item_data))
            elif 'potion_type' in item_data:
                inventory.add_item(Potion.from_json(item_data))
        return inventory

    def __iter__(self):
        return iter(self.backpack)

    def __contains__(self, item):
        return item in self.backpack


inventory = Inventory(owner='Beleg')
inventory.add_item(Weapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary'))
inventory.add_item(Shield(name='Round Shield', defense=150, rarity='epic'))

json_data = json.dumps(inventory.to_json(), indent=4)
print(json_data)

deserialized_inventory = Inventory.from_json(json.loads(json_data))
print(deserialized_inventory.owner)
for item in deserialized_inventory:
    print(item)