from Data.working_file import load_data
from Entities.account import Account


class AccountList:
    def __init__(self, account_list=None):
        if account_list:
            self.account_list = account_list
        else:
            self.account_list = []

        self.show_account_list = self.account_list.copy()

    def search(self, term):
        self.show_account_list.clear()
        for account in self.account_list:
            if term in str(account.id) or term in str(account.national_id):
                self.show_account_list.append(account)

    def insert(self, national_id, firstname, lastname, phone, balance=0):
        account_list = load_data()
        id_list = []
        for account in account_list:
            id_list.append(account.id)
        new_id = max(id_list) + 1
        new_account = Account(new_id, national_id, firstname, lastname, phone, balance)
        self.account_list.append(new_account)
        self.show_account_list.append(new_account)

    def delete(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                self.account_list.remove(account)

        self.show_account_list = self.account_list.copy()

    def get_account(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                return account
