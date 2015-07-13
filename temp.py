"""import random
import scipy.stats as st

pval = input("enter the desired p-value: ")
param = 1-pval
mean = 0
std = 1

threshold = st.norm.ppf(param)

success = 0
failure = 0
runs = 100

for i in range(0,runs):
	x = random.normalvariate(0,1)
	if x > threshold:
		success += 1
	else:
		failure += 1

print "total success: "+str(success)
print "total failure: "+str(failure)
print "percent succes: "+str((success/float(runs)))
"""