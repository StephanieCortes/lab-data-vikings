
# Soldier


class Soldier:
    def __init__(self,health,strenght):
    self.health=health
    self.strenght=strenght
    
    def attack(self):
        return self.strenght
    
    def receiveDamage(self,damage):
        self.health=self.health-damage
    
    pass

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strenght):
        self.name=name
        self.health=health
        self.strenght=strenght
    
    def receiveDamage(self,damage):
        self.damage=self.health-damage
            if self.health>0:
                return(self.name," has received",self.damage,"points of damage")
            else:
                return(self.name," has died in combat")
    
    def BattleCry(self)
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
        self.damage=self.health-damage
            if self.health>0:
                return('A Saxon has received',self.damage,' points of damage')
            else:
                return("A Saxon has died in combat")

# War


