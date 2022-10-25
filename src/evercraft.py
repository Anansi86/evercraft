

class Character:
    def __init__(self,name,align,armorClass,hitPoints):
        self.name = name
        self.align = align
        self.armorClass = armorClass
        self.hitPoints  = hitPoints
        
    # Charecter Can attack
    # attack greater than or equal to  enemy armorClass
    #if attack = 20 always hit
    def attack(self,diceroll,enemyArmor):
        if diceroll == 20:
            return 'Critical Hit'
        elif diceroll >= enemyArmor:
            return True
        else: 
            return False
    
    #damaged
    #if attack == true
        #enemy gets 1 hp
    # else if diceroll is 20

    def damaged(self,diceroll,armorClass):
        if diceroll >= self.armorClass:
            return self.hitPoints - 1
        else:
             return self.hitPoints

