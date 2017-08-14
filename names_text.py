# import xlrd
import json

data = {}

f = open('4060.txt', 'r')
lines = f.readlines()

i = 0
for line in lines:
	i = i + 1

	# Skipping some unnecessary lines at the beggining 
	if i > 5:
		if len(line) < 3:
			continue

		if line == "3 BED ROOM" or line == "2 BED ROOM" or line == "1 BED ROOM":
			continue

		line = line.replace("\n", "").replace(".", "")

		# removing initials added in the lsting 
		replacements = [
			"ABA ",
			"(POA)", 
			"(KESSIS)", 
			"(D/R)", 
			"(D.R)", 
			"(DOCTOR)", 
			"(ABA)", 
			"(DR.)", 
			"(KESS)", 
			"(S/R)", 
			"(M/A)", 
			"(LIKETEGUHAN)", 
			"(MEMEHIR)", 
			"(C/L)", 
			"(ABBA)", 
			"(ENGINEER)", 
			"(NIBREEID)", 
			"(DR)", 
			"(W/O)"
		]

		for r in replacements:
			line = line.replace(r, " ")

		line = line.replace("", "")

		# Replacing names written in shorthand form 
		line = line.replace("T/", "TEKLE")
		line = line.replace("W/", "WELDE")
		line = line.replace("G/", "GEBRE")
		line = line.replace("H/", "HAILE")

		line = line.replace("T.", "TEKLE")
		line = line.replace("W.", "WELDE")
		line = line.replace("G.", "GEBRE")
		line = line.replace("H.", "HAILE")

		# print line

		names = line.split(' ')
 
		for n in names:
			# Skipping names that are short. They are considered errors. 
			if len( n ) < 3:
				continue

			try:
				data[ n ] = data[ n ] + 1
			except:

				# Setting the initial value for a name 
				data[ n ] = 1
			

with open('data_text.json', 'w') as fp:
	json.dump(data, fp)
