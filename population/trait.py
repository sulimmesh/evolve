class Trait:
	""" 
	trait class. represents individual alleles for a 
	given trait

	holds information about dominant/recessive and
	whether this trait has higher fitness for
	full dom or full rec

	when two different alleles meet, the overall
	fitness is calculated by taking the dom

	TODO: implement multiple alleles

	attributes of type:
	dominance: boolean -> if allele is dom/rec
	pref: array of floats for dom and rec fitness

	"""
	def __init__(self, dominance, pref):
		self._dominance = dominance
		self._preference = pref

	def getDom(self):
		return self._dominance

	def getPref(self, index=None):
		if index != None:
			return self._preference[index]
		else:
			return self._preference