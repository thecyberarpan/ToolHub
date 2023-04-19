import os
from function.code import *

brand_logo =(f"""

_________ _______  _______  _        _______                      ______  
\__   __/(  ___  )(  ___  )( \      (  ____ \  |\     /||\     /|(  ___ \ 
   ) (   | (   ) || (   ) || (      | (    \/  | )   ( || )   ( || (   ) )
   | |   | |   | || |   | || |      | (_____   | (___) || |   | || (__/ / 
   | |   | |   | || |   | || |      (_____  )  |  ___  || |   | ||  __ (  
   | |   | |   | || |   | || |            ) |  | (   ) || |   | || (  \ \ 
   | |   | (___) || (___) || (____/\/\____) |  | )   ( || (___) || )___) )
   )_(   (_______)(_______)(_______/\_______)  |/     \|(_______)|/ \___/ 
                                                                          
""")

def logo_output():
    print(brand_logo)


def option ():
    print (f"""
    1. zPhisher
    2. Camphisher
    3. Beef
    4. Beef Over WAN
    """)


def askThe_option():
    try:
        ask = int(input("Select an Option: "))

        if (ask ==1):
             confirmation = input("Are you want to install zphisher? (y/n): ")
             if confirmation == "y":
                 os.system("apt update -y && apt upgrade -y && apt install python3")
             elif confirmation == "n":
                print("It's okey.....")
                os.system("exit")
             else:
                 print("Choose a invalid option....!")
                 askThe_option()
        
        
        elif (ask ==2):
            print("Run Camphisher")

        elif (ask == 3):
            print("Run Beef")

        elif (ask == 4):
            print("Run beeef over WAN")
        
        else:
            print ("Invalid Option.....!")
    
    except ValueError:
        print("Choose a valid option")
        askThe_option()