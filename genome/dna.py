import random

class DNA():
	def __init__(self, length):
		self._length = length
		self._base_pairs = ['a','c','t','g']
		self._sequence = self._genSequence()

	def _genSequence(self):
		sequence = ""
		for base in range(0,self._length-1):
			index = random.randint(0,3)
			sequence += self._base_pairs[index]
		return sequence

	#get methods
	def getSequence(self):
		return self._sequence