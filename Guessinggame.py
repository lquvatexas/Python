# In this program you will prompt the user to think of a number between 1 and 100. Your program will make a guess what the number is. The user will respond with:
1 if the guess is higher than the number thought
0 if the guess is the same as the number thought
-1 if the guess is less than the number thought
Depending on the user's response your program will make another guess.
If the user responds with 0, then you will print out "Thank you for playing the Guessing Game." and the program should terminate. Your program should correctly guess the number in seven attempts or less. If after seven tries the user still replies with either 1 or -1, you will print out "Either you guessed a number out of range or you had an incorrect entry." and the program should terminate.

Recognize that this is a binary search problem. You will have to adapt the binary search algorithm to suit this problem. You can create two variables lo and hi and initialize them to 1 and 100 respectively. You will be offering mid which is the average of lo and hi as your guess. The user will be doing the comparison and letting you know whether you have found the element, or whether your guess was too high or too low. And you will refine your search according to the response of the user.

If the user did guess a number between 1 and 100 you should find it in 7 attempts or less. Now the user may have entered 1 for -1 or vice versa. In such a case you will never be able to guess the right answer. If on the 7th guess the user enters a 1 or -1, then issue the following statement:

Either you guessed a number out of range or you had an incorrect entry.
Here is a sample session, where the program guesses correctly:
Guessing Game 

Think of a number between 1 and 100 inclusive.
And I will guess what it is in 7 tries or less.

Are you ready? (y/n): y

Guess  1 :  The number you thought was 50
Enter 1 if my guess was high, -1 if low, and 0 if correct: 1

Guess  2 :  The number you thought was 25
Enter 1 if my guess was high, -1 if low, and 0 if correct: -1

Guess  3 :  The number you thought was 37
Enter 1 if my guess was high, -1 if low, and 0 if correct: 0

If the user enters a y for the question Are you ready? then go through with the series of guesses. 
If he enters n print Bye and exit the program. 
On the other hand if the response is anything other than y or n then keep repeating the question. 
If the response regarding a guess is anything other than 1, 0, or -1, then keep repeating the guess.
def main():
	print('Guessing Game ')
	print()
	print('Think of a number between 1 and 100 inclusive.')
	print('And I will guess what it is in 7 tries or less.')
	print()
	is_ready = input('Are you ready? (y/n):')
	print()
	while(is_ready != 'y' and is_ready != 'n'):
		is_ready = input('Are you ready? (y/n):')
	#check response
		if (is_ready == 'y'):
			count = 0
			while count <= 8:
				lo = 1
				hi = 100
				while lo <= hi:
					if count == 8 and (reply =='1' or reply =='-1'):
						print('Either you guessed a number out of range or you had an incorrect entry.')
						exit()
					mid = (lo + hi) //2
					print('Guess',count +1,':  The number you thought was',mid)
					reply = input('Enter 1 if my guess was high, -1 if low, and 0 if correct:')
				#print('\n')	
					print('')		
					while reply !='1' and reply!='-1' and reply !='0':
						reply = input('Enter 1 if my guess was high, -1 if low, and 0 if correct:')
					if reply == '1':
						hi = mid - 1
						mid = (lo + hi)//2	
					elif reply =='-1':
						lo = mid + 1
						mid = (lo+hi)//2
					elif reply == '0':
						print('Thank you for playing the Guessing Game')
						exit()
		
					count+=1
		elif is_ready == 'n':
			print ('Bye')
main()
