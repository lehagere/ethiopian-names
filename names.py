import xlrd
import json

wb = xlrd.open_workbook("40-60 house.xlsx" , encoding_override="utf-8")

data = {}

# Name of the sheet the data is on 
sheet = "Data"

for i in range(wb.sheet_by_name( sheet ).nrows):
	name = wb.sheet_by_name( sheet ).row(i)[1] 
	name = name.value.encode('utf-8')
	names = str( name ).split(' ')

	gender = wb.sheet_by_name( sheet ).row(i)[3].value.encode('utf-8') 
	
	index = 0 
	for n in names:
		# Replacing unnecessary characters that were created when converting the PDF file to Excel file
		n = n.replace("'", "").replace("1", "I").replace("l", "I")

		try:
			data[ n ]['count'] = data[ n ]['count'] + 1
		except:
			# If it's not the first name then the gender is male by default 
			if index != 0: 
				gender = "Male" 

			# Setting the initial value for a name 
			data[ n ] = {
				"gender" : gender.upper(),
				"count" : 1
			}
		
		# keeps count of names that have been split 
		index = index + 1 

# Removing an empty
data.pop('')

with open('data.json', 'w') as fp:
	json.dump(data, fp)
