import sys
import hashlib
#count = 0
found = False
run = True
#hMode = 0

def main(inMode = -1):
    global count
    global found
    global pwd
    global hashMode
    hashMode = 0

    print("~~~~CRACKERMACHINE 9000~~~~")
    if inMode == -1:
        print("No mode given, using default setting...")
    else:
        print("Using mode " + inMode + "...")
    pwd = input("Enter a password: ")
    while run:
        count = 0
        if int(inMode) > 0:
            checkMode(inMode)
            inMode = -1
        else:
            #print("hashMode =", hashMode)
            mode = int(input("Enter 0 to change password\n"\
                            "Enter 1 to use dictionary\n"\
                            "Enter 2 to brute force\n"\
                            "Enter 3 to convert to MD5\n"\
                            "Enter 4 to convert to SHA256\n"\
                            "Enter 5 to quit\n"))
            checkMode(mode, hashMode)
            
def dictCrack(pwd, hMode):
    global count
    passList = open("passList.txt", "r").read()
    list = passList.splitlines()
    for guess in list:
        count += 1
        if hMode > 2:
            hGuess = toHash(guess, hMode)
        else:
            hGuess = guess
        #print(hGuess)
        if hGuess == pwd:
            print("\nCracked password: ", guess)
            print(count, "tries\n")
            break
    if count == 10000:
        print("\nDictionary failed :( \nMaybe try brute forcing?\n")

def bruteCrack(pwd, size, hMode, guess = ""):
    global count
    global found
    if size == 0:
        count += 1
        if hMode > 2:
            guess = toHash(guess, hMode)
        #print(guess)
        if guess == pwd:
            print("\nCracked password: " + guess)
            print(count, "tries\n")
            found = True
            if found:
                return
    else:
        for char in range(32, 127):
            if found:
                return
            newGuess = guess + chr(char)
            bruteCrack(pwd, size - 1, hMode, newGuess)

def toHash(pwd, mode):
    global hashMode
    hashMode = mode
    if mode == 3:
        hash = hashlib.md5(pwd.encode()).hexdigest()
    elif mode == 4:
        hash = hashlib.sha256(pwd.encode()).hexdigest()
    return hash
    
            
def checkMode(mode, hMode = 0):
    global pwd
    #print("hMode =", hMode)
    if int(mode) == 0:
        global hashMode
        hashMode = 0
        pwd = input("\nEnter new password: ") 
    elif int(mode) == 1:
        #count = 0
        dictCrack(pwd, hMode)
    elif int(mode) == 2:
        #count = 0
        global found
        found = False
        for x in range(1, 21):
            bruteCrack(pwd, x, hMode)  
    elif int(mode) == 5:
        global run
        run = False
    else:
        pwd = toHash(pwd, mode)
        print("\nHashed password:", pwd)


if __name__ == '__main__':
    #print("~~~~CRACKERMACHINE 9000~~~~")
    #pwd = input("Enter a password: ")
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            #print(sys.argv[i])
            mode = sys.argv[i]
        main(mode)
    else:
        main()
