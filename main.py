import member
import trait
import population

PREF = [0.6, 0.4]
SIZE = 20

pop = population.Population(SIZE,PREF)
pop.runMating()
pop.agePop()
for ind in pop.getPop():
	if ind.getSex():
		print ind.isGestating()
