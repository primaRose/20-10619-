class user:
	users=[]
	def add_user(self,name,password,gender,email,location,number):
		self.name=name
		self.password=password
		self.gender=gender
		self.email=email
		self.location=location
		self.number=number
		self.users.append((self.name,self.password,self.gender,self.email,self.location,self.number))
	def getName(self):
		return self.name
	def getGender(self):
		return self.gender
	def getMail(self):
		return self.email
	def getLocation(self):
		return self.location
	def p(self):
		print(self.users)

class Account(user):
	def __init__(self):
		self.new_account=False
		self.existing_account=False
	def Login(self,username,password):
		self.username=username
		self.password=password
		if user.users==[]:
			print('Invalid username or password\nType in "CreateAccount" if you dont have an existing account.')
		for i in range(len(user.users)):
			if self.username in user.users[i] and self.password in user.users[i]:
				self.existing_account=True
				print('Sucessfully logged in.\nWelcome',user.users[i][0])
				break
			else:
				print('Invalid username or password\nType in "CreateAccount" if you dont have an existing account.')
				self.new_account=True
				break
	def CreateAccount(self,name,password,gender,email,location,number):
		user.add_user(self,name,password,gender,email,location,number)
		print('Account Sucessfully created!\nType in Login.')

class airlineInfo:
	airlines=[]
	def addAirline(self,name,rating,menu,rev):
		self.name=name
		self.rating=rating
		self.menu=menu
		self.rev=rev
		self.airlines.append((self.name,self.rating,self.menu,self.rev))
	def getName(self):
		return self.name
	def getRating(self):
		return self.rating
	def getMenu(self):
		return self.menu
	def getReviews(self):
		return self.reviews
	def getAirlines(self):
		return self.airlines
class Rating(airlineInfo,user):
	def __init__(self):
		self.rating=[]
		self.avg_rating=0
	def setRating(self,airline_name,rate):
		self.airline_name=airline_name
		self.rating.append((airline_name,rate))
		self.total=0
		self.count=0
		for i in range(len(self.rating)):
			if self.airline_name==self.rating[i][0]:
				self.total+=self.rating[i][1]
				self.count+=1
		self.avg_rating=round(self.total/self.count,2)
		for i in range(len(airlineInfo.airlines)): #updating airline rating
			if airline_name in airlineInfo.airlines[i]:
				x=list(airlineInfo.airlines[i])
				x[1]=self.avg_rating
				airlineInfo.airlines[i]=tuple(x)
				print('Your rating has been recorded for',self.airline_name)
			
	def getRating(self):
		return self.avg_rating

class Feedback(user,airlineInfo):
	def getComments(self,airline_name,comment):
		self.comment=comment
		self.airline_name=airline_name
		for i in range(len(airlineInfo.airlines)): #updating airline reviews
			if airline_name in airlineInfo.airlines[i]:
				x=list(airlineInfo.airlines[i])
				x.append(self.comment)
				airlineInfo.airlines[i]=tuple(x)
				print('Your review for',self.airline_name,'has been recorded.')


class search(airlineInfo):
	def getAirlines(self,airline_name):
		self.airline_name=airline_name
		for i in range(len(airlineInfo.airlines)): 
			if airline_name in airlineInfo.airlines[i]:
				print('Airline Name:',airlineInfo.airlines[i][0],'\nRating:',airlineInfo.airlines[i][1],"\nToday's Menu:",airlineInfo.airlines[i][2])
				if len(airlineInfo.airlines[i])==4:
					print('Reviews: No reviews yet.')
					break
				else:
					print('Reviews: ',airlineInfo.airlines[i][4:])
					

class driver:
	def __init__(self):
		print('Welcome to Airline Rating System.\nHere are a list of commands you can use at the prompt.')
		print('1: Login\n2: CreateAccount\n3: Rate\n4: Review\n5: Search\n6: Exit')
		print('Here is the list of Airlines we have: (PIA, Etihad Airways, Thai Airlines, American Airlines, Turkish Airlines')
		self.airline_list=['PIA', 'Etihad Airways', 'Thai Airlines', 'American Airlines', 'Turkish Airlines']
		self.account=Account()
		self.a=airlineInfo() #Default Airlines
		self.a.addAirline('PIA','No ratings yet', 'Pizza','')
		self.a.addAirline('Etihad Airways', 'No ratings yet', 'Pasta', '')
		self.a.addAirline('Thai Airlines', 'No ratings yet', 'Thai soup', '')
		self.a.addAirline('American Airlines', 'No ratings yet', 'Lasagna', '')
		self.a.addAirline('Turkish Airlines', 'No ratings yet', 'Fish and Chips', '')
	def run(self):
		user=input()
		if user == 'Login':
			username=input('Enter Username:')
			password=input('Enter password:')
			self.account.Login(username,password)
			self.run()
		if user == 'CreateAccount':
			name=input('Enter Username:')
			password=input('Enter Password:')
			gender=input('Enter your Gender:')
			email=input('Enter your E-mail:')
			location=input('Enter your location:')
			number=input('Enter your phone number:')
			self.account.CreateAccount(name,password,gender,email,location,number)
			self.run()
		if user == 'Rate':
			if self.account.existing_account==False:
				print('Please Login to rate.')
				self.run()
			self.rating=Rating()
			airline_name=input('Enter the Airline name you wish to rate:')
			if airline_name not in self.airline_list:
				print('No such airline found in Database!.')
				self.run()
			rate=int(input('Rate the airline from 1-5:'))
			self.rating.setRating(airline_name,rate)
			self.run()
		if user == 'Review':
			self.feedback=Feedback()
			if self.account.existing_account==False:
				print('Please Login to review airline.')
				self.run()
			airline_name=input('Enter the Airline name you wish to add a review to:')
			if airline_name not in self.airline_list:
				print('No such airline found in Database!.')
				self.run()
			comment=input('Enter your review:')
			self.feedback.getComments(airline_name,comment)
			self.run()
		if user == 'Search':
			self.Search=search()
			airline_name=input('Enter the Airline name you want to search:')
			if airline_name not in self.airline_list:
				print('No such airline found in Database!.')
				self.run()
			self.Search.getAirlines(airline_name)
			self.run()
		if user == 'Exit':
			exit()
		else:
			print('Invalid Command')
			self.run()


A=driver()
A.run()


		
		


