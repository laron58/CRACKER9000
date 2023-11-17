import sys
import hashlib
import bcrypt
found = False
run = True

def main(inMode = -1):
    global count
    global pwd
    global hashMode
    hashMode = 0

    print("~~~~~~~~~~~~~~~~~~~\n"\
          "~~~ CRACKER9000 ~~~\n"\
          "~~~~~~~~~~~~~~~~~~~")
    if inMode == -1:
        print("No mode given, using default setting...")
    else:
        print("Using mode " + str(inMode) + "...")
    pwd = input("Enter a password: ")

    while run:
        count = 0
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
            except ValueError:
                print("Please enter a valid mode!")
            except KeyboardInterrupt:
                print("Cracking interrupted!")
            
def dictCrack(pwd, hMode):
    global count
    passList = open("passList.txt", "r").read()
    list = passList.splitlines()
    for guess in list:
        count += 1
        if hMode == 5:
            if bcrypt.checkpw(guess.encode(), pwd):
                print("\nCracked password:", guess)
                print(count, "tries")
                return
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
        if hMode == 5:
            if bcrypt.checkpw(guess.encode(), pwd):
                #print(bcrypt.checkpw(guess.encode(), pwd))
                found = True
                print("\nCracked password:", guess)
                print(count, "tries")
                return
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
        if hMode > 2 and count % 3000000 == 0:
            print("Cracking...")
        elif count % 7500000 == 0:
            print("Cracking...")
    else:
        for char in range(32, 127):
            if found:
                return
            newGuess = guess + chr(char)
            bruteCrack(pwd, size - 1, hMode, newGuess)

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
        for x in range(1, 21):
            bruteCrack(pwd, x, hMode)  
    elif mode == 6:
        global run
        run = False
    elif 2 < mode < 6:
        hashMode = mode
        pwd = toHash(pwd, mode)
        print("\nHashed password:", pwd)
    else:
        print("Please enter a valid mode!")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    if len(sys.argv) == 2:
        try:
            if 0 < int(sys.argv[1]) < 6:
                main(int(sys.argv[1]))
            else:
                print("Please enter a valid mode!")
        except ValueError:
            print("Please enter a valid mode!")
    elif len(sys.argv) > 2:
        print("Please enter only one mode!")
