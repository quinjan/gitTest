loggedin = False
for row in database:
            Username_File = row['username']
            Password_File = row['password']
            Fullname_File = row['fullname']
            if (Username_File == Username and
                Password_File == Password and
                    Fullname_File == Fullname):
                loggedin = True
                print('Succesfully logged in as a user.')
            elif loggedin is not True:
            print ('Failed to sign in, wrong username or password.')
