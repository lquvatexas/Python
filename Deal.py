# In this programming assignment we are going to simulate the game show and demonstrate that indeed Marilyn vos Savant gave sensible advice. 
import random
def main():
 # prompt the user to enter the number of times he or she wants to play this game.
 times = eval(input('Enter number of times you want to play:'))
 # print the table line
 print('    Prize    Guess    View    New Guess    ')
 #create a variable to keep track of the number of times the contestant wins by switching
 winswitch = 0
 for i in range(times):
   prize = random.randint(1,3)
   guess = random.randint(1,3)
   view = random.randint(1,3)
 #From those two numbers, compute a number that does not conceal the prize nor is it the contestant's guess. This is the door that is opened by Monty Hall and we shall call it view.
   while (view == prize or view == guess):
    view = random.randint(1,3)
 # a newGuess that is not the original guess nor is it the view.
   newguess = random.randint(1,3)
   while (newguess == guess or newguess == view):
    newguess = random.randint(1,3)
 # Compare the newguess and prize
   if newguess == prize:
     winswitch += 1
   print('    ',prize,'      ',guess,'        ',view,'          ',newguess,'    ')  
 # print the result
 print('Probability of winning if you switch =',round(winswitch / times,2))
 print('Probability of winning if you do not switch =',round(1 - (winswitch / times),2))
main()
