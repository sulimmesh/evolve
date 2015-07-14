import member
import trait
import population
import time

t0 = time.time()
PREF = [0.6, 0.4]
SIZE = 10000
details = {
	"lifespan": 15,
	"gestation": 2,
	"child_rearing": 2,
	"sexual_maturity": 4,
}

pop = population.Population(SIZE,PREF,**details)
#pop.runMating()
for i in range(0,10):
	pop.agePop()
print pop.getSize()
#pregnant = 0
#notPregnant = 0
t1 = time.time()
"""
for ind in pop.getPop():
	if ind.getSex():
		if ind.isGestating():
			pregnant += 1
		else:
			notPregnant += 1
print "Rate of pregnancy: "+str(float(pregnant)/(pregnant+notPregnant)*100)
print "With population size N="+str(SIZE)+" Total runtime was: "+str(round(t1-t0,5))+" seconds"
"""