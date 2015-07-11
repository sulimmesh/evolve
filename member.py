import trait
#declaring class constants here so no magic numbers
_DOM = 0
_REC = 1

class Member:
	""" class for individual member of 
	the sample population
	"""


	def __init__(self, m_type, p_type, age, sex, gestation,
		child_rearing, lifespan, sexual_maturity, 
		isGestating=False, isRearing=False):
		"""
		m_type and p_type are classes with
		information about dominant/recessive and
		whether this trait has higher fitness for
		full dom or full rec

		when two different alleles meet, the overall
		fitness is calculated by taking the dom

		TODO: implement multiple alleles
		TODO: add age, sex, gestation, child_rearing,
		lifespan, sexual_maturity attributes

		attributes of type:
		dominant: boolean -> if allele is dom/rec
		pref: array of floats for dom and rec fitness
		total_fitness: float representing the fitness of the member
		phenotype: boolean -> whether the member expresses the 
		   dom or rec trait
		age: int, age of the member
		sex: boolean, true->female, false->male
		gestation: int # of time steps before birth
		child_rearing: int # of time steps to raise child
		lifespan: int # of time steps until death
		sexual_maturity: int # of time steps until sexual maturity
		isGestating: boolean, if member is pregnant
		isRearing: boolean, if member is raising a child
		"""
		self._m_type = m_type
		self._p_type = p_type
		self._total_fitness = self._calcFitness()
		self._phenotype = self._calcPhenotype()
		self._age = age
		self._sex = sex
		self._gestation = gestation
 		self._child_rearing = child_rearing
		self._lifespan = lifespan
		self._sexual_maturity = sexual_maturity
		self._isGestating = isGestating
		self._isRearing = isRearing

	"""
	finds the overall fitness for the member 
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

	"""
	finds the phenotype of the member
	@private
	"""
	def _calcPhenotype(self):
		if self._m_type.getDom() == True:
			return True
		if self._p_type.getDom() == True:
			return True
		return False

	def _isAvailable(self):
		return None

	def age(self):
		self._age += 1


	""" get methods"""
	def getFitness(self):
		return self._total_fitness
	def getPhenotype(self):
		return self._phenotype
	def getAge(self):
		return self._age
	def getSex(self):
		return self._sex
	def getGestation(self):
		return self._gestation
	def getChildRearing(self):
		return self._child_rearing
	def getLifespan(self):
		return self._lifespan
	def getSexualMaturity(self):
		return self._sexual_maturity
	def getAvailability(self):
		return None


