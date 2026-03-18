from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician

class Boss(Swordsman, Archer, Magician): # multiple inheritance
	def _init_(self, username):
		super() ._ init_(username)
		self.setStr(10)
		self.setVit(25)
		self.setInt(5)
		self.setHp(self.getHp()+self.getVit())

