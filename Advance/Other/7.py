# Python program to extract emails From 
import re 

# Example string 
setence = 'Hello from suraj.karki500@gmail.com to saman@gmail.com about the meeting @2PM'

# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 
exp = '\S+@\S+'
lst = re.findall(exp,setence)	 

# Printing of List 
print(lst) 


# A Python program to demonstrate working 


# a sample function that uses regular expressions 
# to find month and day of a date. 
def findMonthAndDate(string): 
	
	regex = r"([a-zA-Z]+) (\d+)"
	match = re.match(regex, string) 
	
	if match == None: 
		print("Not a valid date")
		return

	print("Given Data: %s" % (match.group())) 
	print("Month: %s" % (match.group(1))) 
	print("Day: %s" % (match.group(2))) 

	
# Driver Code 
findMonthAndDate("Jun 24") 
print("") 
findMonthAndDate("I was born on June 24") 
