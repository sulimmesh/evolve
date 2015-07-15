import trait
import random
#declaring class constants here so no magic numbers
_DOM = 0
_REC = 1

class Member:
	""" class for individual member of 
	the sample population
	
	TODO: implement multiple alleles
	"""


	def __init__(self, m_type, p_type, age, sex, gestation,
		child_rearing, lifespan, sexual_maturity, 
		isGestating=False, isRearing=False, child=None):
		"""
		m_type and p_type are classes with
		information about dominant/recessive and
		whether this trait has higher fitness for
		full dom or full rec

		when two different alleles meet, the overall
		fitness is calculated by taking the dom

		attributes of type:
		dominant: boolean -> if allele is dom/rec
		pref: array of floats for dom and rec fitness

		Args:
		m_type and p_type: maternal and paternal Traits
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
		self._child = child

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

	"""
	returns whether the member is available for mating
	@private
	"""
	def _isAvailable(self):
		if self._age >= self._sexual_maturity:
			if self._isGestating or self._isRearing:
				return False
			else:
				return True
		else:
			return False

	""" 
	creates a child member within a gestating female member
	@private
	"""		
	def _createChild(self, paternal_type):
		if random.randint(0,1) == 1:
			maternal_type = self._m_type
		else:
			maternal_type = self._p_type
		self._child = [maternal_type, paternal_type,0]

	"""
	takes the child attribute and returns a new member
	"""
	def _birth(self):
		if self._isGestating and self._child[2] >= self._gestation:
			m_type = self._child[0]
			p_type = self._child[1]
			#these numbers need to change and are just placeholders
			#for now
			newMember = Member(m_type,p_type,0,
				random.choice([True, False]),2,2,15,2)
			return newMember
		else:
			return None

	""" takes an available member and impregnates them if female """
	def mate(self, partner):
		if self._isAvailable() and self._sex:
			partner_type = None
			if random.randint(0,1) == 1:
				partner_type = partner.getMaternalType()
			else:
				partner_type = partner.getPaternalType()
			self._isGestating = True
			self._createChild(partner_type)
			#print "Member is female and available, returning true"
			return True
		elif self._isAvailable() and not self._sex:
			#print "Member is male and available, returning true"
			return True
		else:
			return False
	""" 
	ages the member 1 year -> this could be changed to a given
	time step
	"""
	def age(self):
		self._age += 1
		if self._isGestating:
			self._child[2] += 1
			if self._child[2] >= self._gestation:
				return self._birth()
			else:
				return None
		else:
			return None

	""" status checkers for statistical purposes"""
	def isGestating(self):
		return self._isGestating
	def isChildRearing(self):
		return self._isRearing

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
		return self._isAvailable()
	def getPaternalType(self):
		return self._p_type
	def getMaternalType(self):
		return self._m_type



