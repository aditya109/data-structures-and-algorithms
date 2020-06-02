# Python3 Program to check whether a 
# given key already exists in a dictionary. 

# Function to print sum 
def checkKey(dict, key): 
	
	if dict.has_key(key): 
		print ("Present, value =", dict[key] )
	else: 
		print ("Not present")

# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
key = 'b'
checkKey(dict, key) 

key = 'w'
checkKey(dict, key) 



