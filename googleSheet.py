#gspread documentation:
#http://www.indjango.com/access-google-sheets-in-python-using-gspread/
#
#You will probably need to 'pip install gspread' to get this working  

#!/usr/bin/python

#Setting up our Google Spreadsheet interface
import gspread
gc = gspread.login('fleserverconfig@gmail.com', 'yerbamate')

#Open Google sheet by name
sh = gc.open("SanDisk Configuration Database")

#Select worksheet by index
worksheet = sh.get_worksheet(0)


##################################################################################
#Finding first empty row
valuesList = worksheet.col_values(1)
rowIndex = len(valuesList) + 1

worksheet.update_cell(rowIndex,1,'Free room!') #Testing that we have an empty row


##################################################################################
#Searching for a particular server based on MAC 
#Replace CDDE w/ what we find
cellSearchResult = worksheet.findall("CDDE")

#Update one cell to the right 
worksheet.update_cell(cellSearchResult[0].row,cellSearchResult[0].col+1,'To the right!')


##################################################################################
#On restart, search spreadsheet to see if the MAC has been configured & at what step
#cellSearchResult = worksheet.findall("CDDE")

#If it hasn't been found, then we are free to write it to a new row
if not cellSearchResult: 
	print ('Cant find him!')

#If it has been found, we want to see at what index/step we left off
if cellSearchResult:
	valuesList = worksheet.row_values(cellSearchResult[0].row)
	lastStepIndex = (len(valuesList))
	print(lastStepIndex)



