import csv
import argparse
import os
os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument("username", help = "Input the Username")
parser.add_argument("password", help = "Input the Password")
args = parser.parse_args()
users = []

def read():
    with open("D:/MAPUA/2018-2019/COE125/login/accounts.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(dict(username=row['username'],
                                 password=row['password'],
                                 name=row['name']))
      
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
    
# ---- Main ---- #
read()
login()