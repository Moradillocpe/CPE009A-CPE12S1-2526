class Character():
    def __init__(self, username):
     self.__username = euni
     self.__hp = 100
     self.__mana = 100
     self.__damage = 5
     self.__str = 0
     self.__vit = 0
     self.__init = 0
     self.__agi= 0
def getUsername(self):
    return self.__username
def setUsername(self, new_username):
    self._username = new_username
def getHP(self):
    return self.__hp
def setHP(self, new_hp):
    self.__hp = new_hp
def getDamage(self):
    return self.__damage
def setDamage(self, new_damage):
    self.__damage = new_damage
def getstr(self):
    return self.__str
def setstr(self, new_str):
    self.__str = new_str
def getvit(self):
    return self.__vit
def setvit(self, new_vit):
    self.__vit = new_vit
def getint(self):
    return self ._int
def getint(self):
    return self.__int
def setint(self, new_int):
    self .__int = new_int
def getAgi(self):
    return self .__agi
def setAgi(self, new_agi):
    self.__agi = new_agi
def reduceHp(self, damage_amount):
    self.__hp = self .__hp - damage_amount
def addHp(self, heal_amount):
    self .__hp = self .__hp + heal_amount
    
    
character1 = Character("Euni")
print(character1.__username)
print(character1.getUsername())