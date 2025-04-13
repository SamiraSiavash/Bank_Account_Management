from Entities.account import Account
from Login.user import User


def load_data():
    account_list = []
    with open("Data\\AccountData.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line_splitted = line.split(",")
            account = Account(int(line_splitted[0]), line_splitted[1], line_splitted[2], line_splitted[3],
                              line_splitted[4], line_splitted[5])
            account_list.append(account)

    return account_list


def replace_data(account_list):
    data_text = ""
    last_account_item = account_list[-1]
    for account in account_list:
        data_text += f"{account.id},{account.national_id},{account.first_name},{account.last_name},{account.phone},{account.balance}"
        if account.id != last_account_item.id:
            data_text += "\n"

    with open("Data\\AccountData.txt", mode="w") as file:
        file.write(data_text)


def login():
    user_list = []
    with open("Login\\Users.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line_splitted = line.split(",")
            user = User(line_splitted[0], line_splitted[1])
            user_list.append(user)

    return user_list
