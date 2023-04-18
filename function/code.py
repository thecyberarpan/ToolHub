import os
import time
from function.logo import *

# Funtion for clear the screen 
def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")






#Code Run again
def run_again():
    option = input("Are you want to run again?(Y?N): ")
    if option.lower()== "y":
        clear_screen()
        os.system("python3 main.py")

    elif option.lower() == "n":
        print("Thanks for using our tool....!")
        os.system ("exit")

    else:
        print("Invalid option....!")
        time.sleep(0.9)
        run_again()