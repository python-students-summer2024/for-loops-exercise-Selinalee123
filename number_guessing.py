"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""
import random

def guess_number(low, high, num_attempts):  
    target_number = random.randint(low, high)  

    guess_count = 0  
      
    for _ in range(num_attempts):  
        try:  
            guess = int(input(f"Guess a number between {low} and {high} (you have {num_attempts - guess_count} attempts left): "))  
            guess_count += 1  
            if guess == target_number:  
                print(f"Congratulations! You guessed the number in {guess_count} attempts.")  
                return True  
            else:  
                print("Incorrect guess. Try again.")  
        except ValueError:  
            print("Invalid input. Please enter a number.")  
            guess_count += 1
             
    print(f"Sorry, you did not guess the number in {num_attempts} attempts.")
    return False  