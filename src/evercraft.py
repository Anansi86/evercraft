

class Character():
    def __init__(self, name, align):
        self.name = name
        self.align = align
        self.armorClass = 10
        self.hitPoints = 5
        self.is_dead = False
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        
    # Charecter Can attack
    # attack greater than or equal to  enemy armorClass
    # if attack = 20 always hit
    def attack(self, diceroll, enemyArmor,hitPoints):
        if diceroll == 20:
            return 'Critical Hit'
        elif diceroll >= enemyArmor:
            return True
        else:
            return False

    # damaged
    # if attack == true
        # enemy gets 1 hp
    # else if diceroll is 20

    def damaged(self, diceroll, armorClass):
        if diceroll >= self.armorClass:
            return self.hitPoints - 1
        else:
            return self.hitPoints


"""
Charecter has:
Strength, Dexterity, Constitution, 
wisdom, intelligence, 
Charisma

Create class that contains abilities that the charecter can inheret
"""
