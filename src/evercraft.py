

class Character:
    def __init__(self,name,align,armorClass,hitPoints):
        self.name = name
        self.align = align
        self.armorClass = armorClass
        self.hitPoints  = hitPoints
        
    # Charecter Can attack
    # attack greater than or equal to  enemy armorClass
    #if attack = 20 always hit
    def attack(self, hitPoints):
        return self.hitPoints 