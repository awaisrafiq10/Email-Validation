import re

email_criteria = "^[a-z]+[\._]?[a-z0-9]+(@gmail.com)$"              # Define a regular expression pattern for matching a Gmail email address | ([@]gmail[.]com)$
quit_key = "q"                                                          # Define the key to use for quitting the program

while True:                                                                                     # Start an infinite loop
    email_input = input("Please Enter Your Email (to quit press '"+ quit_key +"'): ")           # Prompt the user for their email address
    if email_input == quit_key:                                                                 # If the user entered the quit key, break out of the loop
        break
    if re.search(email_criteria, email_input):                                                  # Check if the email address matches the email pattern
        print("Your Email is Right.")
    else:
        print("Your Email is Wrong.")
