def read():
    with open("D:/MAPUA/2018-2019/COE125/login/accounts.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(dict(username=row['username'],
                                 password=row['password'],
                                 name=row['name']))
