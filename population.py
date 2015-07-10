import member
import trait 
import random

class Population:
	"""
	population class

	represents a single population of members, each having
	traits.

	this class holds methods to:
	   _genPopulation -> generates a new population of 
	   <size>

	   TODO: add remaining class methods
	   TODO: should the mating algorithm go here?

	"""
	def __init__(self, size, preference):
		self._size = size
		self._preference = preference
		self._population = self._genPopulation()


	def getSize(self):
		return self._size

	def getPop(self):
		return self._population
	"""
	method to create the dom/rec traits
	"""
	def _genTraits(self, preference):
		dom = trait.Trait(True, preference)
		rec = trait.Trait(False, preference)
		traits = [dom, rec]
		return traits

	"""
	method to generate the population from members
	@private
	"""
	def _genPopulation(self):
		size = self._size
		traits = self._genTraits(self._preference)
		population = []
		for i in range(1,size):
			#approximately a 75/25 split of dom/rec
			index_1 = random.randint(0,1)
			index_2 = random.randint(0,1)
			ind = member.Member(
				traits[index_1],
				traits[index_2])
			population.append(ind)
		return population



