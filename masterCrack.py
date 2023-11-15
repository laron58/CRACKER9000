import sys
pwd = ""
crack = ""
count = 0
mode = 0
digi = 99

def main(pwd = ""):
    crack = ""
    cnt = 0
    #print(pwd)
    #print("~~~~CRACKERMACHINE 4000~~~~")
    #pwd = input("Enter a password: ")
    mode = int(input("Enter 0 to change password\nEnter 1 to use dictionary\nEnter 2 to brute force\n"))
    modeCheck(mode, pwd)
    
def dictCrack(pwd):
    global cnt
    cnt = 0
    #print(pwd)
    passList = open("passList.txt", "r").read()
    list = passList.splitlines()

    for guess in list:
        #print(guess)
        cnt += 1
        if guess == pwd:
            #crack = guess
            print("\nCracked password: ", guess)
            print(cnt, "tries\n")
            main(pwd)
            exit()
    if cnt == 10000:
        print("Dictionary failed :( \nMaybe try brute forcing?\n")
    main(pwd)

def bruteCrack(pwd, size, cnt = 0, guess = ""):
    global count
    #global cnt
    #print(pwd, size, guess)
    if size == 0:
        count += 1
        #global digi
        print(count)
        print(guess)
        if guess == pwd:
            #crack = guess
            print("\nCracked password: " + guess)
            print(count, "tries\n")
            main(pwd)
            exit()
        #elif guess.count('~') == len(guess):
            #print("new digit!")
    else:
        for char in range(32, 127):
            #cnt += 1
            newGuess = guess + chr(char)
            bruteCrack(pwd, size - 1, cnt, newGuess)

def modeCheck(mode, pwd):
    if mode == 0:
        pwd = input("\nEnter new password: ")
        #print(pwd)
        main(pwd)
    elif mode == 1:
        dictCrack(pwd)
    elif mode == 2:
        for x in range(1, 21):
            global digi
            digi = x
            print("bigD", digi)
            bruteCrack(pwd, x, count)

if __name__ == '__main__':
    print("~~~~CRACKERMACHINE 4000~~~~")
    pwd = input("Enter a password: ")
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            print(sys.argv[i])
    else:
        main(pwd)

