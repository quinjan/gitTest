     
def login():
    username = args.username
    password = args.password
    for user in users:
        if user['username'] == username and user['password'] == password:
            print('You are logged in.')
            break
        else:
            print('Wrong input. Try Again')
            break
