from random import randint
num=randint(1,100)

print("****WELCOME TO THE GUESSING GAME CHALLANGE****")
print("There is the random number chossen by the system between 1 to 100, only thing you have to do is to guess the number.")
print("Now lets talk about the rules....")
print("1. On the player first turn, if the guess is within 10 of the number, 'WARM!' is returned. \n2. Guessed number,further away from 10 of the number then 'COLD!' is returned.")
print("3. On all subsequent turn, if the guess number is closer to the number than the previous guess 'WARMER!' is returned.")
print("4. Farther from the number than the previous guess, 'COLDER!' is returned.")
print("5. When the guessed number is equal to the random number then a message is diplayed 'GUESSED CORRECTLY!' and also shows the number of turns taken.")
print("6. If a player's guess is less than 1 or greater than 100 then it displays 'OUT OF BONDS'")

guesses = [0]
while True:
     # we can copy the code from above to take an input
        
    guess=int(input("I'm thinking the number between 1 to 100. \n What is your guess? "))
    if guess<1 or guess>100:
        print("OUT OF BONDS")
        continue
   
    if guess==num:
        print(f"GUESSED CORRECTLY and number of guesses taken is {len(guesses)}.")
        break
        
    guesses.append(guess)
    
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("WARMER!")
        else:
            print("COLDER!")
            
    else:
        if abs(num-guess)<=10:
            print("WARM!")
        else:
            print("COLD!")
