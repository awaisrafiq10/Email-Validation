quit_key = "q"                                                          # Define the key to use for quitting the program

while True:                                                                                     # Start an infinite loop
    email = input("Please Enter Your Email (to quit press '"+ quit_key +"'): ")           # Prompt the user for their email address
    if email == quit_key:                                                                 # If the user entered the quit key, break out of the loop
        break
    j,k,l = 0,0,0
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if email[-10:] == "@gmail.com":
                    for i in email:
                        if i == i.isspace():
                            j = 1
                        elif i.isalpha():
                            if i == i.upper():
                                k = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            l = 1
                    if j == 1 or k == 1 or l == 1:
                        print("Wrong Email 5")
                    else:
                        print("Right Email.")
                else:
                    print("Wrong EMail 4")
            else:
                print("Wrong Email 3")
        else:
            print('Wrong Email 2')
    else:
        print("Wrong Email 1")