
abilitiesChart = {
    '1': -5,
    '2': -4,
    '3': -4,
    '4': -3,
    '5': -3,
    '6': -2,
    '7': -2,
    '8': -1,
    '9': -1,
    '10': 0,
    '11': 0,
    '12': 1,
    '13': 1,
    '14': 2,
    '15': 2,
    '16': 3,
    '17': 3,
    '18': 4,
    '19': 4,
    '20': 5
}


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
        self.charisma = 10

    # Charecter Can attack
    # attack greater than or equal to  enemy armorClass
    # if attack = 20 always hit
    # def attack(self, diceroll, enemyArmor, enemyHp):


    def attack(self,diceRoll, enemy):
        if enemy.is_dead == False:
            modifier = abilitiesChart[diceRoll]
            self.strength = self.strength + modifier
            return self.strength

    def defense(self, diceRoll):
        modifier = abilitiesChart[diceRoll]
        return self.dexterity + modifier
        

    # damaged
    # if attack == true
        # enemy gets 1 hp
    # else if diceroll is 20

    def damaged(self, diceroll, armorClass):
        if diceroll >= self.armorClass:
            return self.hitPoints - 1
        else:
            return self.hitPoints

    def mod_diceRoll():
        # return score
        pass


# Strength, measuring physical power
# Dexterity, measuring agility
# Constitution, measuring endurance
# Intelligence, measuring reasoning and memory
# Wisdom, measuring Perception and Insight
# Charisma, measuring force of Personality

# Roll dice, based on the dice roll, abilities will
# go up or down.

# lets say we roll a 20, we will increase ability by 5

# function modStrength(diceroll):


