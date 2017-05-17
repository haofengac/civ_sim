from constants import *
import time

class Entity():
	def __init__(self, pos, world, id):
		self.pos = pos
		self.world = world
		self.id = time.time()