class animal:
	def __init__(self, leg, horn, nail):
		self.leg = leg
		self.horn = horn
		self.nail = nail

	def move(self):
		print("Moving")

class horse(animal):
	def __init__(self, leg, horn, nail, type):
		self.type = type

		animal.__init__(self, leg, horn, nail)

	def move(self):
		print("Running")

	def get_details(self):
		print("Number of leg:	{}".format(self.leg))
		
		if self.horn:
			print("Has horn")
		else:
			print('No horn')

		if self.nail:
			print("Has nail")
		else:
			print('No nail')

		print("{} type".format(self.type))

myhorse = horse(leg=4, horn=False, nail=False, type="Sport")
myhorse.move()
myhorse.get_details()