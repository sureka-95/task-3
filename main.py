import random
number= random.randint(1,100)
attempts=0

print("guess the number between 1 and 100!!!!")

while True:
      guess= int(input("enter your guess number:"))
      attempts += 1
      if guess > number:
            print("The number is too high, Try again")
      elif guess < number:
            print("The number is too low, Try again")
      else:
            print("Congratulation!!!, you guessed the correct number")
            break
