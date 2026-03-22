# i am write guessing number game in this game computer automatics genrate one number between 1 to 100 and 
# user choice a number between 1 to 100 when till computer genrate number = user number choices 
import random
attempts=0 #create a variable for count how much attempts to correct guess by user
guess_computer_number=random.randint(1,100) #genrate a random number between 1 to 100 by computer using the random modules 
while True:
   user_guess_number=int(input("guess the number between 1 to 100:")) #user choices number between 1 to 100 
   attempts+=1 
   if user_guess_number==guess_computer_number:
       print("congratulations! you guessed the correctnumber in",attempts,"attempts")
       break
   elif user_guess_number>guess_computer_number:
       print("too high! please try again")
      
   else:
       print("too low! please try again")
   