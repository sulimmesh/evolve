import random
from collections import OrderedDict

class DNA():
	def __init__(self, length):
		self._length = self._checkLength(length)
		self._base_pairs = ['a','c','t','g']
		self._codons = OrderedDict([
			("att","i"),
			("atc","i"),
			("ata","i"),
			("ctt","l"),
			("ctc","l"),
			("cta","l"),
			("tta","l"),
			("ttg","l"),
			("gtt","v"),
			("gtc","v"),
			("gta","v"),
			("gtg","v"),
			("ttt","f"),
			("ttc","f"),
			("atg","m"),
			("tgt","c"),
			("tgc","c"),
			("gtc","a"),
			("gcc","a"),
			("gca","a"),
			("gcg","a"),
			("cct","p"),
			("ccc","p"),
			("cca","p"),
			("ccg","p"),
			("atc","t"),
			("acc","t"),
			("aca","t"),
			("acg","t"),
			("tct","s"),
			("tcc","s"),
			("tca","s"),
			("tcg","s"),
			("agt","s"),
			("agc","s"),
			("tat","y"),
			("tac","y"),
			("tgg","w"),
			("caa","q"),
			("cag","q"),
			("aat","n"),
			("aac","n"),
			("cat","h"),
			("cac","h"),
			("gaa","e"),
			("gag","e"),
			("gat","d"),
			("gac","d"),
			("aaa","k"),
			("aag","k"),
			("cgt","r"),
			("cgc","r"),
			("cga","r"),
			("cgg","r"),
			("aga","r"),
			("agg","r"),
			("taa","stop"),
			("tag","stop"),
			("tga","stop")
			])
		self._sequence = self._genSequence()

	def _checkLength(self, length):
		difference = length%3
		if difference > 0:
			length = length-difference
			print "Length off by "+str(difference)+", subtracting difference..."
		return length


	def _genSequence(self):
		sequence = ""
		codon_keys = self._codons.keys()
		for i in range(0,self._length/3):
			index = random.randint(0,len(codon_keys)-4)
			sequence += codon_keys[index]
		return sequence

	def runSequence(self):
		dna = self._sequence
		codon = ""
		protein = ""
		for i in range(0,len(dna)-4,3):
			codon = dna[i]+dna[i+1]+dna[i+2]
			if codon in self._codons.keys():
				protein += self._codons[codon]+" "
		return protein
	#get methods
	def getSequence(self):
		return self._sequence
	def getCodons(self):
		return self._codons

