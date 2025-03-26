def create_account():
    Full_name=input("Enter your name:")
    ph_no=int(input("Enter your ph_no:"))
    password=input("enter the password:")
    if len(password) >= 8:
        if password.isalnum():
            print(password)
        else:
            print("The should contain alphanumeric (A-Z),(a,z) and (0,9)")
    else:
        print("The password should contain minimum 8 characters!")

    confirm_password=input("enter the password")
    if password == confirm_password:
        print(confirm_password)
    else:
        print("Incorrect password")

create_account()    