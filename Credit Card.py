# The program that I will be writing will be called CreditCard. When the user enter the creditcard number the program should recognize this card comes from which company.
# Check whether it is a 15 or 16 digit credit card number
def is_digit(cc_num):
	a = str(cc_num)
	if len(a) == 15 or len(a) ==16:
		return cc_num

# This function checks if a credit card number is valid
def is_valid(cc_num):
	if(cc_num == is_digit(cc_num)):
		sum = 0
		a = str(cc_num)
		for i in range(0,len(a) + 1):
			if i % 2 == 0:
				i = cc_num % 10
			else:
				i = (cc_num % 10) * 2
				i = i % 10 + i // 10
			cc_num = cc_num // 10
			sum = sum + i
		if sum % 10 != 0:
			return False 
		return True
	   
# This function returns the type of credit card
def cc_type(n):
	if n // (10**13) == 34 or n // (10**13) == 37 or n // (10**14) == 34 or n // (10**14) == 37:
		return 'American Express'
	elif n //(10**12) == 6011 or n //(10**13) == 644 or n // (10**14) == 65:
		return 'Discover'
	elif n // (10**13) == 50 or n // (10**13) == 55 or n // (10**14) ==50 or n // (10**14) == 55:
		return 'MasterCard'
	elif n // (10**14) == 4 or n // (10**15) == 4:
		return 'Visa'
	else:
		return
# Test the card number is 15 or 16-digit and find out what type of the card is
def main():
	num = eval(input('Enter 15 or 16-digit credit card number:'))             
	if is_digit(num):
		if is_valid(num):
			if cc_type(num):
				print('Valid',cc_type(num),'credit card number')
			else:
				print('Valid credit card number')
		else:
			print('Invalid credit card number')
	else:
		print('Not a 15 or 16-digit number')
main()
