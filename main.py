import member
import trait
import population

PREF = [0.6, 0.4]
SIZE = 2000

pop = population.Population(SIZE,PREF)
pop.runMating()
pop.agePop()
pregnant = 0
notPregnant = 0
for ind in pop.getPop():
	if ind.getSex():
		if ind.isGestating():
			pregnant += 1
		else:
			notPregnant += 1
print "Rate of pregnancy: "+str(float(pregnant)/(pregnant+notPregnant)*100)
