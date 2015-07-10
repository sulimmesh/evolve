import member
import trait
import population

PREF = [0.6, 0.4]
SIZE = 100

pop_obj = population.Population(SIZE,PREF)
pop = pop_obj.getPop()
dom = 0
rec = 0
for ind in pop:
	if ind.getPhenotype() == True:
		dom += 1
	else:
		rec += 1

print "Total expression of dominant trait is: "+str(float(dom)/(dom+rec)*100)+"%"