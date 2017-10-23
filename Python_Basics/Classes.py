# creating and using classes
class Car():
	def __init__(self,color):
		print "starting %s car started " % color
	def accel(self,speed):
		print "speeding up to %s mph" % speed
	def turn(self, direction):
		print "turning %s" % direction
	def stop(self):
		print "stop"
""" 
Initializing the Car class with car_object
Calling the class and and its functions with
variables
"""
"""
car_object = Car('red')
car_object.color1 = 'red'
car_object.accel(100)
car_object.turn('right')
car_object.stop()
"""

# Inheriting the above class into another class called RaceCar
class RaceCar(Car):
	def __init__(self, color):
		self.color = color
		self.top_speed = 200
		print "%s race car started with a top speed of %s"  % (self.color,self.top_speed)
	def accel(self, speed):
		print "speeding up to %s mph is very very fast" % speeed
	
car_object = Car('red')
racecar_object = RaceCar("Blue")
## Below function is not defined in RaceCar though Car is inherited,it is can call turn function in Car class
racecar_object.turn("letf")
