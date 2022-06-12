import os
import time
#Must Access this to continue.
def main():
    UserName = input ("Enter Username: ")
    attempts = 0
    while True:
        if UserName == 'Isabela':
            time.sleep(1)
            print ("Hello Isabela! The password is : W@12")
            logged()
            break

        elif attempts > 2:
            print ("You Have Entered the Maximum Amount of Tries! See You Later. ")
            break
        else:
            UserName = input ("You Entered The Wrong Name, Try Again: ")
            attempts += 1



def logged():                  
    time.sleep(1)
    print ("Welcome to Your Site")


main()

