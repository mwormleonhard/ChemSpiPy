import chemspipy
import re
import sys

if len(sys.argv) == 1:
	indfilnavn = raw_input("Filnavn med stoffer? >")
else:
	indfilnavn = sys.argv[1]
	
fjern = re.compile('[^a-zA-Z0-9]')
print("Stof\tSumformel\tMonoisotopicmass")
 
with open(indfilnavn) as f:
	for line in f:
		c = chemspipy.find_one(line)
		print line.strip(), "\t", re.sub(fjern, '', c.mf) , "\t", c.monoisotopicmass 
