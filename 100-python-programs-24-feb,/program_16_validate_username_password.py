import re

# Read username and password from standard input
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Username validation
if len(username) < 5 or not username.isalnum():
    print("Invalid Username")
else:
    # Password validation
    if len(password) < 8:
        print("Invalid Password: Too short")
    elif not re.search(r"[A-Z]", password):
        print("Invalid Password: Must contain uppercase letter")
    elif not re.search(r"[a-z]", password):
        print("Invalid Password: Must contain lowercase letter")
    elif not re.search(r"[0-9]", password):
        print("Invalid Password: Must contain digit")
    elif not re.search(r"[!@#$%^&*]", password):
        print("Invalid Password: Must contain special character")
    else:
        print("Username and Password are valid")import re

# Read username and password from standard input
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Username validation
if len(username) < 5 or not username.isalnum():
    print("Invalid Username")
else:
    # Password validation
    if len(password) < 8:
        print("Invalid Password: Too short")
    elif not re.search(r"[A-Z]", password):
        print("Invalid Password: Must contain uppercase letter")
    elif not re.search(r"[a-z]", password):
        print("Invalid Password: Must contain lowercase letter")
    elif not re.search(r"[0-9]", password):
        print("Invalid Password: Must contain digit")
    elif not re.search(r"[!@#$%^&*]", password):
        print("Invalid Password: Must contain special character")
    else:
        print("Username and Password are valid") 

    //  input : 
       Username: user123
       Password: Pass@123
    // output : 
       Username and Password are valid      


