#declaring variables for stored username & password
storeduname = "joe"
storedpwd = "123"

#creating user input for username & password
username = input("enter your username: ")
password = input("enter your password: ")

#starting loop for conditions and creating amount of attempts to log in
count = 3
while count > 0:
    #condition for right username
    if username == storeduname and password == storedpwd:
        print("welcome " + username)
        break
    #condition for blank username and password
    elif count > 1 and username == ("") and password == (""):
        username = input("enter your username: ")
        password = input("enter your password: ")
        continue
    #condition for wrong username
    elif count > 1:
        count -= 1
        print ("you only have ", count, " tries left")
        username = input("enter your username: ")
        password = input("enter your password: ")
        continue
    #condition for no more tries left
    else:
        print ("you no longer have access")
        break