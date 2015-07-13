import member
import trait 
import random
import scipy.stats as st

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

			ind = member.Member(traits[index_1], traits[index_2],
				5, random.choice([True, False]),2,2,15,2)
			population.append(ind)
		return population

	""" returns nothing. removes dead members from the population """
	def agePop(self):
		for ind in self._population:
			newMember = ind.age()
			if newMember != None:
				self._population.append(newMember)
			if ind.getAge() > ind.getLifespan():
				self._population.remove(ind)

	""" 
	returns nothing.
	sorts the population into eligble male and female lists.
	runs the mating algorithm on the two lists and finishes when
	all eligble females have had 3 chances to get pregnant. If they
	fail, then they must wait for the next cycle.
	"""
	def runMating(self):
		maleList = []
		femaleList = []
		femRuns = 0
		numTrue = 0
		runs = 0
		for ind in self._population:
			if ind.getAvailability():
				if ind.getSex():
					#need to check if we've run on this female
					femaleList.append([ind,False])
				else: 
					maleList.append(ind)
		while len(femaleList) > 0 and femRuns < 1:
			runs += 1
			#print "starting cycle"
			if len(maleList) > 0:
				male = random.choice(maleList)
			else:
				return None
			if len(femaleList) > 0:
				tempFemale = random.choice(femaleList)
			else:
				return None
			index = femaleList.index(tempFemale)
			female = tempFemale[0]
			visited = tempFemale[1]
			if not visited:
				femaleList[index][1] = True
				numTrue += 1
			#param is 1-fitness, for use in ppf
			mParam = 1-male.getFitness()
			fParam = 1-female.getFitness()
			mThreshold = st.norm.ppf(mParam)
			fThreshold = st.norm.ppf(fParam)
			#print "thresholds assigned"
			"""
			there's a question here whether they share the same
			random number or each get their own. For now they each
			get their own random number
			"""
			mRandom = random.normalvariate(0,1)
			fRandom = random.normalvariate(0,1)
			""" 
			the problem here is that if the even if both have a 50%\ chance of
			mating successfully alone, when combined in this way, that chacnce alread
			drops to 25%. This means that only a small proportion of the total eligible
			population successfully mates each cycle. 
			 """
			if mRandom > mThreshold and fRandom > fThreshold:
				#print "both above threshold"
				if male.mate(female) and female.mate(male):
					#print "current female length: "+str(len(femaleList))
					femaleList.remove(tempFemale)
					numTrue -= 1
					#print "new length: "+str(len(femaleList))
			"""
			for ind in femaleList:
				#print "has been visited: "+str(ind[1])
				if not ind[1]:
					break
				else: 
					numTrue += 1
			"""
			if numTrue == len(femaleList):
				femRuns += 1

			#print
		print "runs: "+str(runs)

	""" get methods """
	def getSize(self):
		return self._size

	def getPop(self):
		return self._population



