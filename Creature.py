import random
import time
import Entity
from constants import *

class Creature(Entity):
	def __init__(self, pos, world, hp=100, age=0, sex=None):
		Entity.__init__(self, pos, world)
		self.hp = hp
		self.age = age
		self.sex = sex
		if self.sex == None:
			self.sex = int(random.random()*2)

	def mate(lover):
		child = Creature(self.pos)
		self.world.creatures[child.id] = child
		return child



