# import the titanic data csv files and convert from string of data to array

#csv importer
import csv as csv
#import numpy package to convert data
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))

header = csv_file_object.next() #ignores the header line

data = [] #creates the variable 'data'
for row in csv_file_object:
	data.append(row) #run through each row and append it to the data
#right now the data is stored as a list in a variable, we want to convert it to an array
data = np.array (data)

print data

#print the first row in detail
print data[0]

#try being selective, tell me the 4th passenger's name?
print data[3,3] #remember 1st col is 0, 1st row is 0

#try doing some calculations 
#everything is stored as a string so need to convert to float

#size(data[0:: means include all the data in the array
number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers