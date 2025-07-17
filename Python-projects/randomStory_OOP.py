'''
This code creates randoms stories based on the user inputs
'''


class Story:
	def __init__(self, firstName, secondName, firstPlace, secondPlace):
		self.firstName = firstName
		self.secondName = secondName
		self.firstPlace =firstPlace
		self.secondPlace = secondPlace
		
	def __str__(self): #NOTE: STR method only receives the self parameter, not extra values
	    return "There was a time where {} met {}, they were going to {} but it was closed, so they decided to go to {}".format(self.firstName, self.secondName, self.firstPlace, self.secondPlace)

firstName = input("Enter the first name: ")		
secondName = input("Enter the second name: ")	
firstPlace = input("Enter the first place: ")	
secondPlace = input("Enter the second place: ")	


newStory = Story(firstName, secondName, firstPlace, secondPlace)

print(newStory)