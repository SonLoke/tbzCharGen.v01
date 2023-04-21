import random
import math

class pc: # pc = Player Character
    def __init__(self, name, age, sex, concept):
        # Basic Details
        self.name = name
        self.age = age
        self.sex = sex
        self.concept = concept
        
        # Attribute Distribution
        self.attribute_total = None
        while self.attribute_total != 40:
            self.attributes = [random.randint(1,9) for _ in range(7)]
            self.attribute_total = sum(self.attributes)

        # Stats
        self.vitality = self.attributes[0] + self.attributes[4]
        self.light_wounds = math.ceil(self.attributes[0])
        self.heavy_wounds = math.ceil(self.attributes[0]/2)
        self.critical_wounds = math.ceil(self.attributes[0]/4)
        self.dead_wound = 1

        self.soul = 2 * (self.attributes[3] + self.attributes[4])

        self.karma = 30 + random.randint(0,30)

        # Weapons & Gear
        self.weapon_cost = random.randint(0,6)
        self.weapon_name_list = ["Rock","Stick","Pole","Dagger","Short Sword","Knife","Tachi","Katana","Great Sword","Rilfe"]
        self.weapon_name = random.choice(self.weapon_name_list)
        while self.weapon_cost > self.attributes[6]:
            self.weapon_cost = random.randint(0,6)

# Character Sheet Sample
p1 = pc("Kirie", "Older Teen", "Female", "Gruff and quick-tempered ex-armour rider turned armour hunter")

print(
    f"""
    Name: {p1.name}
    Age: {p1.age} | Sex: {p1.sex}
    Concept: {p1.concept}

    Stats:
        Vitality: {p1.vitality} | Soul: {p1.soul}
            Light Wounds: {p1.light_wounds}
            Heavy Wounds: {p1.heavy_wounds}
            Critical Wounds: {p1.critical_wounds}
            Dead: {p1.dead_wound}
        
        Karma: {p1.karma}/108

    Attributes:
        Body: {p1.attributes[0]} | Agility: {p1.attributes[1]} | Senses: {p1.attributes[2]}
        Knowledge: {p1.attributes[3]} | Spirit: {p1.attributes[4]} | Empathy: {p1.attributes[5]} | Station: {p1.attributes[6]}

    Skills:
        Unskilled (1):
        Skilled (2):
        Advanced (3):
        Master (4):
        Supreme (5):

    Weapon: {p1.weapon_name}(+{p1.weapon_cost} dmg)
    """
)
