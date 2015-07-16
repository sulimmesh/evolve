import member
import trait 
import random
import time

class Population:
	"""
	population class

	represents a single population of members, each having
	traits.

	this class holds methods to:
	   _genPopulation -> generates a new population of 
	   <size>

	   TODO: add remaining class methods

	"""
	def __init__(self, size, preference, sexual_maturity, gestation, 
		child_rearing, lifespan):
		self._size = size
		self._preference = preference
		self._maleList = None
		self._femaleList = None
		self._sexual_maturity = sexual_maturity
		self._gestation = gestation
		self._child_rearing = child_rearing
		self._lifespan = lifespan
		self._population = self._genPopulation()

	"""
	method to create the dom/rec traits
	"""
	def _genTraits(self, preference):
		traits = {}
		for pref in preference:
			dom = trait.Trait(True, pref)
			rec = trait.Trait(False, pref)
			current_trait = [dom, rec]
			traits[id(current_trait)] = current_trait
		return traits
	"""
	method to generate the population from members
	@private
	"""
	def _genPopulation(self):
		femaleList = []
		maleList = []
		size = self._size
		traits = self._genTraits(self._preference)
		population = []
		for i in range(1,size):
			#approximately a 75/25 split of dom/rec
			index_1 = random.randint(0,1)
			index_2 = random.randint(0,1)
			age = int(random.normalvariate(int(self._lifespan/2),int(self._lifespan/4)))
			if age < 0 or age >= self._lifespan:
				age = random.normalvariate(int(self._lifespan/2),0)

			ind = member.Member(traits, age, random.choice([True, False]),
				self._gestation, self._child_rearing, self._lifespan,
				self._sexual_maturity)
			population.append(ind)
			if ind.getAvailability():
				if ind.getSex():
					femaleList.append(ind)
				else:
					maleList.append(ind)
		self._maleList = maleList
		self._femaleList = femaleList
		return population

	"""
	method to choose random elements from male and female lists
	@prviate
	"""
	def _randomChoice(self, maleList, femaleList, numTrue):
		if len(maleList) > 0:
			male = random.choice(maleList)
		else:
			male = None
		if len(femaleList) > 0:
			index = random.randint(0,len(femaleList)-1)
			tempFemale = femaleList[index]
			female = tempFemale[0]
			visited = tempFemale[1]
			if not visited:
				tempFemale[1] = True
				numTrue += 1
		else:
			female = None
		return male, female, index, numTrue

	""" 
	returns nothing.
	sorts the population into eligble male and female lists.
	runs the mating algorithm on the two lists and finishes when
	all eligble females have had 3 chances to get pregnant. If they
	fail, then they must wait for the next cycle.
	"""
	def runMating(self):
		segment1 = 0
		segment2 = 0
		segment3 = 0
		maleList = self._maleList[:]
		femaleList = []
		for ind in self._femaleList:
			femaleList.append([ind, False])
		femRuns = 0
		numTrue = 0
		runs = 0

		while len(femaleList) > 0 and femRuns < 1:
			runs += 1
			t0 = time.time()
			members = self._randomChoice(maleList, femaleList, numTrue)
			male = members[0]
			female = members[1]
			index = members[2]
			numTrue = members[3]
			t1 = time.time()
			segment1 += t1-t0
			"""
			I've replaced the normalvariate technique for now
			with simple random integers. This way, if the random
			int is greater than the threshold, the mating is a success.
			This has the same concept behind it as the normalvariate 
			solution did, but it runs a lot faster at large N so is
			currently preferred.
			"""
			t0 = time.time()
			mParam = 1-male.getFitness()
			fParam = 1-female.getFitness()
			mThreshold = mParam*100 
			fThreshold = fParam*100
			"""
			there's a question here whether they share the same
			random number or each get their own. For now they each
			get their own random number
			"""
			mRandom = random.randint(0,100)
			fRandom = random.randint(0,100)
			t1 = time.time()
			segment2 += t1-t0
			""" 
			the problem here is that if the even if both have a 50%\ chance of
			mating successfully alone, when combined in this way, that chacnce alread
			drops to 25%. This means that only a small proportion of the total eligible
			population successfully mates each cycle. 
			 """
			t0 = time.time()
			if mRandom > mThreshold and fRandom > fThreshold:
				if male.mate(female) and female.mate(male):
					femaleList.pop(index)
					numTrue -= 1
			t1 = time.time()
			segment3 += t1-t0

			if numTrue == len(femaleList):
				femRuns += 1

		print "runs: "+str(runs)
		print "Segment 1 took "+str(round(segment1,5))+" seconds"
		print "Segment 2 took "+str(round(segment2,5))+" seconds"
		print "Segment 3 took "+str(round(segment3,5))+" seconds"

	""" returns nothing. removes dead members from the population """
	def agePop(self):
		t0 = time.time()
		total_pop = []
		female_pop = []
		male_pop = []
		for ind in self._population:
			newMember = ind.age()
			if newMember != None:
				total_pop.append(newMember)
			if ind.getAge() <= ind.getLifespan():
				total_pop.append(ind)
				if ind.getAge() >= ind.getSexualMaturity():
					if ind.getSex():
						female_pop.append(ind)
					else:
						male_pop.append(ind)
		self._population = total_pop
		self._femaleList = female_pop
		self._maleList = male_pop
		t1 = time.time()
		print "Population aging took "+str(round(t1-t0,5))+" seconds"

	""" get methods """
	def getSize(self):
		return len(self._population)

	def getPop(self):
		return self._population

	def getMaleList(self):
		return self._maleList
	def getFemaleList(self):
		return self._femaleList



