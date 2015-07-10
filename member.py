import trait
#declaring class constants here so no magic numbers
_DOM = 0
_REC = 1

class Member:
	""" class for individual member of 
	the sample population
	"""


	def __init__(self, m_type, p_type):
		"""
		m_type and p_type are classes with
		information about dominant/recessive and
		whether this trait has higher fitness for
		full dom or full rec

		when two different alleles meet, the overall
		fitness is calculated by taking the dom

		TODO: implement multiple alleles

		attributes of type:
		dominant: boolean -> if allele is dom/rec
		pref: array of floats for dom and rec fitness
		"""
		self._m_type = m_type
		self._p_type = p_type
		self._total_fitness = self._calcFitness()

	"""
	finds the overall fitness for the individual 
	@private
	"""
	def _calcFitness(self):
		m_dominance = self._m_type.getDom()
		p_dominance = self._p_type.getDom()
		fitness = None
		if m_dominance == p_dominance:
			if m_dominance == True:
				fitness = self._m_type.getPref(_DOM)
			else:
				fitness = self._m_type.getPref(_REC)
		else:
			if m_dominance == True:
				fitness = self._m_type.getPref(_DOM)
			else:
				fitness = self._m_type.getPref(_REC)
		return fitness		

	""" get method for member fitness"""
	def getFitness(self):
		return self._total_fitness

