import random
import string

def main():
    password = []

    while True:
        try:
            userChar = int(input("What is your desired CHAR length? "))
            break
        except ValueError:
            print("Please enter a valid CHAR.")

    while True:
        try:
            userNum = int(input("What is your desired INT length? "))
            break
        except ValueError:
            print("Please enter a valid INT.")

    password = createPassword(userNum, userChar,password)
    newPassword = ''.join(str(i) for i in password)
    
    scramble = ""
    while scramble.lower != "yes" or "no":
        try:
            scramble = input("Do you want to scramble your password?: Yes or No ")
            break
        except ValueError:
            print("Please type Yes or No")
    
    if scramble.lower == "yes":
        random.shuffle(password)
        newPassword = ''.join(str(i) for i in password)
        print(f' Your new password is: {newPassword}')

    else:
        newPassword = ''.join(str(i) for i in password)
        print(f' Your new password is: {newPassword}')
    
def createPassword(userNum, userChar,password):
    temp_char = randomChar(userChar)
    temp_num = randomNum(userNum)

    temp_passowrd = []
    temp_password = temp_char + temp_num

    return temp_password

def randomNum(userNum):
    num_list = list(string.digits)
    temp_num_list = []
    
    for i in range(userNum):
        ran_num = random.choice(num_list)
        temp_num_list.append(ran_num)

    return temp_num_list

def randomChar(userChar):
    char_list = list(string.ascii_letters)
    temp_char_list = []
    
    for i in range(userChar):
        ran_char = random.choice(char_list)
        temp_char_list.append(ran_char)

    return temp_char_list

main()

input("Press Enter to exit...")
