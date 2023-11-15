import sys
#count = 0
found = False
run = True

def main(inMode = -1):
    global count
    global found
    global pwd

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
            mode = int(input("Enter 0 to change password\n"\
                            "Enter 1 to use dictionary\n"\
                            "Enter 2 to brute force\n"\
                            "Enter 3 to quit\n"))
            checkMode(mode)
            
def dictCrack(pwd):
    global count
    passList = open("passList.txt", "r").read()
    list = passList.splitlines()

    for guess in list:
        #print(guess)
        count += 1
        if guess == pwd:
            print("\nCracked password: ", guess)
            print(count, "tries\n")
            break
    if count == 10000:
        print("\nDictionary failed :( \nMaybe try brute forcing?\n")

def bruteCrack(pwd, size, guess = ""):
    global count
    global found

    if size == 0:
        count += 1
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
            bruteCrack(pwd, size - 1, newGuess)
            
def checkMode(mode):
    global pwd

    if int(mode) == 0:
        pwd = input("\nEnter new password: ")
    elif int(mode) == 1:
        #count = 0
        dictCrack(pwd)
    elif int(mode) == 2:
        #count = 0
        global found
        found = False
        for x in range(1, 21):
            bruteCrack(pwd, x)  
    elif int(mode) == 3:
        global run
        run = False

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
