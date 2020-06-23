import math

def debtfinder():
	while True:
		try:
			value = float(input('How much is the mortage debt? (£) '))
			#confirms input is right type
			if not isinstance(value, (float, int)):
				raise ValueError
		except ValueError:
			print ("Please enter numbers only!") 
		else:
			return value
			break


def promointr():
	while True:
		try:
			value = float(input('Is there a promotional interest? (%) If no, please enter "0" '))
			#confirms input is right type
			if not isinstance(value, (float, int)):
				raise ValueError
		except ValueError:
			print ("Please enter numbers only!")
		else:
			return value
			break 


def intfinder():
	while True:
		try:
			value = float(input('What is the interest on the morgage? (%) '))
			#confirms input is right type
			if not isinstance(value, (float, int)):
				raise ValueError
		except ValueError:
			print ("Please enter numbers only!")
		else:
			return value
			break  	

def recalc():
	while True:
		try:
			again = input('Would you like to recalculate? yes or no: ')
			if again.lower() not in ['yes','no']:
				raise ValueError
		except ValueError:
			print ('Please enter yes or no')
		else:
			break
	
	return again.lower().startswith('y')

def rerun():
	while True:
		try:
			again = input('Would you like to rerun the calculator? yes or no: ')
			if again.lower() not in ['yes','no']:
				raise ValueError
		except ValueError:
			print ('Please enter yes or no')
		else:
			break
	
	return again.lower().startswith('y')

def mortgagecalc():
	'''
	Program to calculate various things related to morgages 
	Number of options available:
	1. monthly repayment calculator for given interest rate 
	2. payback time for a given a monthly repayment 
	3. Each of the two options will allow the user to see an annual and/or monthly breakdown
	4. maybe for option 2, add overpayment option. 
	going to use this to practice OOP using classes. maybe
	'''
	#this is to clear the screen 
	print (' \n'*100)
	
	#welcoming statment
	print("Welcome to Nnamdi's mortgage calculator")

	#runs the calc
	calc = True 
	months = ["Jan", "Fab", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
	
	while calc: 
			
		#grabs user's name
		user = input('Hi, what is your name? ')

		#initial user inputs to obtain user's name and which calc wanted 1 or 2. 
		while True: 
			

			try:

				#grabs user's selection
				print (' \n'*100)
				print (f"Hi {user}")
				selector = input('Please enter the type of calculator you require, monthly repayment (MR) or payback time (PT) ')
				if selector.lower()[0] not in ['m','p']:
					raise ValueError

			except ValueError:
				print ('Please enter either "m" or "p"')

			else:
				#sets calc in right while loop
				if selector.lower().startswith('m'):
					MP = True 
					PT = False
				else:
					MP = False
					PT = True 
				break 

		while MP:
			print (' \n'*100)
			print (f"Hi {user}, you have selected the monthly repayment calculator")
			#need more user inputs. Debt, term, promotional interest, promotional term  
			
			debt = debtfinder()
			
			while True:
				try:
					term = int(input('How long is the mortage term? (years) '))
					#confirms input is right type
					if not isinstance(term, (int)):
						raise ValueError
					if term > 40:
						raise TypeError
				except ValueError:
					print ("Please enter (whole) numbers only!")
				except TypeError:
					print ('No lender is offering lending terms greater than 40 years. Please select appropriately')
				else:
					N = term * 12 
					break

			promoint = promointr()

			while promoint != 0:
				try:
					promoterm = int(input(f'Great, how long does {promoint}% last for? (months) '))
					#confirms input is right type
					if not isinstance(promoterm, (int)):
						raise ValueError
				except ValueError:
					print ("Please enter numbers only!")
				else: 
					break  

			rate = intfinder()
			
			Rdebt = debt
			promoyears = 0
			counter = 0
			rterm = term
			rpromoterm = 0
			print (' \n'*100)			

			if promoint > 0:
				print (f'For the promotional period of {promoterm} months {user}, see breakdown below: \n')
				print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Month",'Paid',"Int. Accrued","Remaining"))
				promorate = promoint / 12 / 100
				promoMP = promorate * (1 + promorate)**N * debt / ((1 + promorate)**N - 1)
				for i in range(promoterm):
					Intdue = Rdebt * promorate
					Rdebt = Rdebt * (1 + promorate) - promoMP
					print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format((months[counter]),(round(promoMP,2)),(round(Intdue,2)),(round(Rdebt,2))))					
					if counter == 11:
						counter = 0
					else:
						counter += 1

				if promoterm % 12 == 0:
					promoyears = int(promoterm / 12)
					rterm = term - promoyears
					N = rterm * 12
				else:
					extras = promoterm % 12
					rpromoterm = promoterm - extras 
					promoyears = int(promoterm / 12)
					rterm = term - promoyears 
					N = rterm * 12

			
			rate = rate / 12 / 100
			monthlypayment = rate * (1 + rate)**N * Rdebt / ((1 + rate)**N - 1)

			yr = 1

			print (f'{user}, after any promotional period, your monthly payments will be \t£{round(monthlypayment,2)}\n')

			Rdebt = debt
			
			if promoyears > 0:
				Intdue = 0
				print (f'Annual breakdown of promotional years is as follows:\n')
				print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Year",'Paid',"Int. Accrued","Remaining"))
				for i in range(promoyears):
					for i in range(12):
						Intdue = Intdue + Rdebt * promorate
						Rdebt = Rdebt * (1 + promorate) - promoMP
					print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format(yr,(round(promoMP*12,2)),(round(Intdue,2)),(round(Rdebt,2))))
					yr += 1

			if rpromoterm > 0:
				print (f'{user}, part way through year {yr}, transition from the promotional deal to the standard deal will occur')
				print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Year",'Paid',"Int. Accrued","Remaining"))
				Intdue = 0
				for i in range(rpromoterm):
					Intdue = Intdue + Rdebt * promorate
					Rdebt = Rdebt * (1 + promorate) - promoMP
				for i in range(12 - rpromoterm):
					Intdue = Intdue + Rdebt * rate
					Rdebt = Rdebt * (1 + rate) - monthlypayment
				print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format(yr,(round(promoMP * rpromoterm + monthlypayment * (12 - rpromoterm),2)),(round(Intdue,2)),(round(Rdebt,2))))
				yr += 1

			print (f'{user}, annual breakdown of non-promotional years is as follows \n')
			print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Year",'Paid',"Int. Accrued","Remaining"))
			for i in range(term - yr + 1):
				Intdue = 0
				for i in range(12):
					Intdue = Intdue + Rdebt * rate
					Rdebt = Rdebt * (1 + rate) - monthlypayment
				print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format(yr,(round(monthlypayment*12,2)),(round(Intdue,2)),(round(Rdebt,2))))
				yr += 1

			if not recalc():
				print ("Thank you for using Nnamdi's repayment calculator, hopefully it was helpful!")

				break  


		while PT:
			
			print (' \n'*100)
			
			print (f"Hi {user}, you have selected the payment term calculator")

			debt = debtfinder()

			promoint = promointr()
			
			while promoint != 0:
				try:
					promoterm = int(input(f'Great, how long does {promoint}% last for? (months) '))
					#confirms input is right type
					if not isinstance(promoterm, (int)):
						raise ValueError
				except ValueError:
					print ("Please enter numbers only!")
				else: 

					break  

			rate = intfinder()

			while True:
				try:
					c = input(f'{user}, how much can will you be paying per month? ')
					#confirms input is right type
					if not isinstance(debt, (float, int)):
						raise ValueError
				except ValueError:
					print ("Please enter numbers only!") 
				else:
					break

			c = float(c)

			rate = rate / 12 / 100

			Rdebt = debt
			promoyears = 0
			counter = 0
			print (' \n'*100)	

			if promoint > 0:

				promorate = promoint / 12 / 100

				a = 1 / (1 - promorate * debt / c)  

				N = round(math.log(a,(1 + rate)),0)

				rterm = round( N / 12,0)

				print (f'For the promotional period of {promoterm} months {user}, see breakdown below: \n')
				print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Month",'Paid',"Int. Accrued","Remaining"))
				for i in range(promoterm):
					Intdue = Rdebt * c
					Rdebt = Rdebt * (1 + promorate) - c
					print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format((months[counter]),(round(c,2)),(round(Intdue,2)),(round(Rdebt,2))))					
					if counter == 11:
						counter = 0
					else:
						counter += 1

				if promoterm % 12 == 0:
					promoyears = int(promoterm / 12)
					rpromoterm = 0			
				else:
					extras = promoterm % 12
					rpromoterm = promoterm - extras 
					promoyears = int(promoterm / 12)

			a = 1 / (1 - rate * Rdebt / c)  

			N = round(math.log(a,(1 + rate)),0)

			yr = 1

			Rdebt = debt
			
			if promoyears > 0:
				Intdue = 0
				print (f'Annual breakdown of promotional years is as follows:\n')
				print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Year",'Paid',"Int. Accrued","Remaining"))
				for i in range(promoyears):
					for i in range(12):
						Intdue = Intdue + Rdebt * promorate
						Rdebt = Rdebt * (1 + promorate) - c
					print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format(yr,(round(c*12,2)),(round(Intdue,2)),(round(Rdebt,2))))
					yr += 1

			if rpromoterm > 0:
				print (f'{user}, part way through year {yr}, transition from the promotional interest to the standard interest will occur')
				print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Year",'Paid',"Int. Accrued","Remaining"))
				Intdue = 0
				for i in range(rpromoterm):
					Intdue = Intdue + Rdebt * promorate
					Rdebt = Rdebt * (1 + promorate) - c
				for i in range(12 - rpromoterm):
					Intdue = Intdue + Rdebt * rate
					Rdebt = Rdebt * (1 + rate) - c
				print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format(yr,(round(c*12,2)),(round(Intdue,2)),(round(Rdebt,2))))
				yr += 1

			print (f'{user}, annual breakdown of non-promotional years is as follows \n')
			print ('{0:^8} | {1:^8} | {2:^8} | {3:^8}'.format("Year",'Paid',"Int. Accrued","Remaining"))
			while Rdebt > 0:
				Intdue = 0
				for i in range(12):
					Intdue = Intdue + Rdebt * rate
					Rdebt = Rdebt * (1 + rate) - c
				print ('{0:^8} | £{1:^8} | £{2:^8} | £{3:^8}'.format(yr,(round(c*12,2)),(round(Intdue,2)),(round(Rdebt,2))))
				yr += 1

			#print (f'{user}, finally in year {yr}')

			if not recalc():
				print ("Thank you for using Nnamdi's payback time calculator, hopefully it was helpful!")
				break
			
		#this stops the entire calc. 
		if not rerun():
			print ("Thank you for using Nnamdi's mortage calculator, hopefully it was helpful!")
			break



if __name__ == '__main__':
	mortgagecalc()