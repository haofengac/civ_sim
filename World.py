import numpy as np
from constants import *
import random
import Entity

class World():
	def __init__(self, size=(10,10)):
		self.creatures = {}
		self.grid = Grid(self, size=size)
		self.resources = {}
		self.width, self.height = size
		self.god = None

	def setGod(god):
		self.god = god

class Grid():
	def __init__(self, world, resource_factor=SPARSE_RESOURCE_FACTOR, size=(10,10)):
		self.map = np.zeros(size)
		self.world = world
		generate_resources(resouce_factor)

	def generate_resources(resource_factor):
		for i in range(int(self.world.width * self.world.height * resource_factor)):
			r = int(random.random() * self.height)
			c = int(random.random() * self.width)
			if self.map[r,c] != VACANT:
				continue
			res = Resource((r,c), self.world)
			self.world.resources[res.id] = res

class Resource(Entity):
	def __init__(self, pos, world):
		Entity.__init__(self, pos, world)
		self.world.map[*pos] = RESOURCE
		self.value = RESOURCE_VALUE

	def reap():
		return self.value


class Plant(Entity):
	def __init__(self, pos, world):
		Entity.__init__(self, pos, world)


