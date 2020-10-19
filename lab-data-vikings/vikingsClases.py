
# Soldier


class Soldier:
    def __init__(self,health,strenght):
    self.health=health
    self.strenght=strenght
    
    def attack(self):
        return strenght
    
    def receiveDamage(self,damage):
        self.damage= self.health-damage
    

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strenght):
        self.name=name
        self.health=health
        self.strenght=strenght
    
    def receiveDamage(self,damage):
        self.damage=self.health-damage
            if self.damage <self.health:
                print(self.name," has received",self.damage,"points of damage")
            else:
                print(self.name," has died in combat")
    
    def BattleCry(self)
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
        self.damage=self.health-damage
            if self.damage <self.health:
                print('A Saxon has received',self.damage,' points of damage')
            else:
                print("A Saxon has died in combat")

# War


class War:
    pass
