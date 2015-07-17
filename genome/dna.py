import random

class DNA():
	def __init__(self, length):
		self._length = length
		self._base_pairs = ['a','c','t','g']
		self._sequence = self._genSequence()

	def _genSequence(self):
		sequence = ""
		for base in range(0,self._length-1):
			index = random.randint(0,3)
			sequence += self._base_pairs[index]
		return sequence

	def runSequence(self,codons):
		dna = self._sequence
		codon = ""
		protein = ""
		for i in range(0,len(dna)-4,3):
			codon = dna[i]+dna[i+1]+dna[i+2]
			if codon in codons.keys():
				protein += codons[codon]+" "
		return protein
	#get methods
	def getSequence(self):
		return self._sequence