import math

class Sphere:
	def __init__(self, radius):
		self.radius=radius
    #returns radius
	def getRadius(self):
		return self.radius
	#returns surface area after calculating
	def surfaceArea(self):
		self.surfaceArea=(4*math.pi*self.radius**2)
		return self.surfaceArea
	#returns volume after calculating
	def volume(self):
		self.volume=(4/3*math.pi*(self.radius**3))
		return self.volume