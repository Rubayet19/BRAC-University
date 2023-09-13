# Defining all the lists and functions used
email = []
web = []


# The main function
def checker(list):
    # checking if there is one "@"
    def oneAtTheRAte(string):
        if string.count("@") == 1:
            return True
        else:
            return False

    # checking if the string is an email address
    def checkEmail(string):
        # splitting the string at "@"
        parts = string.split("@")
        # checking if the string starts with a letter
        if string[0].isalpha() == True:
            # checking if the next keys are letters/digits/hyphen
            st = parts[0]
            for i in range(len(st)):
                if st[i].isalnum() == True or st[i] == "-" or st[i] == ".":
                    continue
                return False
            # checking the part after the "@"
            if parts[1].endswith(".") == False:
                # checking if there is any "." at all in second part
                if parts[1].count(".") > 0:
                    # splitting second part at "."
                    st2 = parts[1].split(".")
                    for s in st2:
                        for i in range(len(s)):
                            # checking if they are letters or hyphen
                            if s[i].isalpha() == True or s[i] == "-" or s[i] == " ":
                                continue
                            return False
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # checking if the string is a web address
    def checkWeb(string):
        # checking if the address starts with alphabet and doesn't end with a "."
        if string[0].isalpha() == True and string[-1] != ".":
            # checking if there is atleast one "."
            if string.count(".") > 0:
                # splitting at "."
                parts = string.split(".")
                for part in parts:
                    if part.isalnum() == True:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False

    # functions being called
    i = 1
    for item in inputList:
        if oneAtTheRAte(item) == True:
            if checkEmail(item) == True:
                email.append(i)

        elif checkWeb(item) == True:
            web.append(i)

        i = i + 1


# Function for printing the output
def output():
    print("\n")
    print("Email, ", end="")
    if not email:
        print("Invalid")
    else:
        for x in email: print(x, end=" ")
    print(" ")
    print("Web, ", end="")
    if not web:
        print("Invalid")
    else:
        for x in web: print(x, end=" ")


# working with the inputs
# Taking the inputs
n = int(input())
inputList = []
for i in range(n):
    inputList.append(str(input()))

# Calling the main function and output function
checker(inputList)
output()