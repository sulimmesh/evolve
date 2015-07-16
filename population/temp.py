import population
import member
import trait

trait1_m = trait.Trait(True, [0.6,0.4])
trait1_p = trait.Trait(True, [0.6,0.4])

trait2_m = trait.Trait(False, [0.7,0.3])
trait2_p = trait.Trait(True, [0.7,0.3])

genome = {
	"trait1": [trait1_m,trait1_p],
	"trait2": [trait2_m,trait2_p]
}
kwargs = {
	"age": 5,
	"sex": True,
	"gestation": 2,
	"child_rearing": 2,
	"lifespan": 15,
	"sexual_maturity": 4,
}
member1 = member.Member(genome, **kwargs)

kwargs = {
	"age": 5,
	"sex": False,
	"gestation": 2,
	"child_rearing": 2,
	"lifespan": 15,
	"sexual_maturity": 4,
}
member2 = member.Member(genome,**kwargs)

#testing all get methods
assert member1.isGestating() == False
assert member1.isChildRearing() == False
assert member1.getFitness() > 0 and member1.getFitness() < 1
print member1.getFitness()
for key in member1.getGenome().keys():
	print member1.getPhenotype(key)
assert member1.getAge() == 5
assert member1.getSex() == True
assert member1.getGestation() == 2
assert member1.getChildRearing() == 2
assert member1.getLifespan() == 15
assert member1.getSexualMaturity() == 4
assert member1.getAvailability() == True
assert member1.getGenome() == genome
for key in member1.getGenome().keys():
	print member1.getPaternalType(key).getDom(),member1.getPaternalType(key).getDom()
	print member1.getMaternalType(key).getDom(),member1.getMaternalType(key).getDom()

#age testing
age1 = member1.getAge()
age2 = member2.getAge()
assert member1.age() == None
assert member1.getAge() == age1+1
assert member2.age() == None
assert member2.getAge() == age2+1

#testing mating
assert member1.mate(member2) == True
assert member2.mate(member1) == True
assert member1.isGestating() == True
member1.age()
assert type(member1.age()) == type(member1)


