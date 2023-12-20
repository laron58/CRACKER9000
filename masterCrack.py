import sys
import hashlib
import bcrypt
found = False
run = True

# If no mode is passed from console, inMode == -1; no password -> inPwd = ""
def main(inMode = -1, inPwd = ""):
    global count
    global pwd
    global hashMode
    # Resets hashMode to 0 upon completion of hash crack
    hashMode = 0

    print("~~~~~~~~~~~~~~~~~~~\n"\
          "~~~ CRACKER9000 ~~~\n"\
          "~~~~~~~~~~~~~~~~~~~")
    if inMode != -1:
        print("Using mode " + str(inMode) + "...")
    if inPwd == "":
        pwd = input("Enter a password: ")
    else:
        pwd = inPwd
    
    # Constaly prompts for next mode while run true (false when quit)
    while run:
        count = 0
        # Passes console argument to checkMode and skips prompt
        if int(inMode) > 0:
            checkMode(inMode)
            inMode = -1
        else:
            try:
                mode = int(input("\nEnter 0 to change password\n"\
                                "Enter 1 to use dictionary\n"\
                                "Enter 2 to brute force\n"\
                                "Enter 3 to convert to MD5\n"\
                                "Enter 4 to convert to SHA256\n"\
                                "Enter 5 to convert to BCrypt\n"\
                                "Enter 6 to quit\n"))
                checkMode(mode, hashMode)
            # Entered modes that aren't numbers
            except ValueError:
                print("Please enter a valid mode!")
            # Catching keyboard interrupts
            except KeyboardInterrupt:
                print("Cracking interrupted!")
            
def dictCrack(pwd, hMode):
    global count
    # Imports and splits the dictionary file
    passList = open("passList.txt", "r").read()
    list = passList.splitlines()
    # Iterates through every item; hashes using hMode if necessary
    for guess in list:
        count += 1
        if hMode == 5:
            if bcrypt.checkpw(guess.encode(), pwd):
                print("\nCracked password:", guess)
                print(count, "tries")
                return
            # Loading message for every 10 BCrypt attempts
            if count % 10 == 0:
                print("Cracking...")
        elif hMode > 2:
            hGuess = toHash(guess, hMode)
        else:
            hGuess = guess
        #print(hGuess)
        if hMode != 5 and hGuess == pwd:
            print("\nCracked password:", guess)
            print(count, "tries")
            return
    if count == 10000:
        print("\nDictionary failed :( \nMaybe try brute forcing?")

def bruteCrack(pwd, size, hMode, guess = ""):
    global count
    global found
    if size == 0:
        count += 1
        # Hash cracking with hMode if applicable
        if hMode == 5:
            #print(bcrypt.checkpw(guess.encode(), pwd))
            if bcrypt.checkpw(guess.encode(), pwd):
                found = True
                print("\nCracked password:", guess)
                print(count, "tries")
                return
            # Loading message for every 10 BCrypt attempts
            if count % 10 == 0:
                print("Cracking...")
        elif hMode > 2:
            hGuess = toHash(guess, hMode)
        else:
            hGuess = guess
        #print(hGuess)
        if hMode != 5 and hGuess == pwd:
            found = True
            print("\nCracked password:", guess)
            print(count, "tries")
            return
        # Loading message for every 3m hashed attempts
        if hMode > 2 and count % 3000000 == 0:
            print("Cracking...")
        # Loading message for every 7.5m attempts
        elif count % 7500000 == 0:
            print("Cracking...")
    else:
        for char in range(32, 127):
            # Unraveling recursive function
            if found:
                return
            # Creates guesses for every ASCII character recursively based on size
            newGuess = guess + chr(char)
            bruteCrack(pwd, size - 1, hMode, newGuess)

# Hashes password based on mode
def toHash(pwd, mode):
    if mode == 3:
        hash = hashlib.md5(pwd.encode()).hexdigest()
    elif mode == 4:
        hash = hashlib.sha256(pwd.encode()).hexdigest()
    elif mode == 5:
        hash = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
    return hash
            
def checkMode(mode, hMode = 0):
    global pwd
    global hashMode
    if mode == 0:
        hashMode = 0
        pwd = input("\nEnter new password: ") 
    elif mode == 1:
        dictCrack(pwd, hMode)
    elif mode == 2:
        global found
        found = False
        # Tries combinations up to 21 characters long
        for x in range(1, 21):
            bruteCrack(pwd, x, hMode)  
    elif mode == 6:
        global run
        run = False
    elif 2 < mode < 6:
        hashMode = mode
        pwd = toHash(pwd, mode)
        print("\nHashed password:", pwd)
        if mode == 5:
            print("Warning: BCrypt cracking is VERY slow.")
    # Entered modes that aren't 0 to 6
    else:
        print("Please enter a valid mode!")

if __name__ == '__main__':
    # No arguments given
    if len(sys.argv) == 1:
        main()
    # Mode given
    elif len(sys.argv) == 2:
        try:
            if 0 < int(sys.argv[1]) < 6:
                main(int(sys.argv[1]))
            else:
                # Entered modes that aren't 0 to 6
                print("Please enter a valid mode!")
        # Entered modes that aren't numbers
        except ValueError:
            print("Please enter a valid mode!")
    # Mode and password given
    elif len(sys.argv) == 3:
        try:
            if 0 < int(sys.argv[1]) < 6:
                main(int(sys.argv[1]), sys.argv[2])
            else:
                # Entered modes that aren't 0 to 6
                print("Please enter a valid mode!")
        # Entered modes that aren't numbers
        except ValueError:
            print("Please enter a valid mode!")
    # Catching more than one console argument
    elif len(sys.argv) > 2:
        print("Please enter only one mode and a password!")
