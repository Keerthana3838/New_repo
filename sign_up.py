def create_account(username,ph_no,password):

    
    if len(password) >= 8:
        if password.isalnum():
            print(password)
        else:
            print("The should contain alphanumeric (A-Z),(a,z) and (0,9)")
    else:
        print("The password should contain minimum 8 characters!")



username="Keerthana"
ph_no=9238644232
password="keer383838"
create_account(username,ph_no,password)    