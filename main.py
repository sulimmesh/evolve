import member
import trait

PREF = [0.6, 0.4]

allele1 = trait.Trait(True, PREF)
allele2 = trait.Trait(False, PREF)

ind = member.Member(allele1, allele2)
fitness = ind.getFitness()
print fitness