from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.ttk import Treeview
from Data.working_file import load_data, replace_data, login
from Entities.account_list import AccountList

login_form = Tk()
login_form.title("Login")

username_label = Label(login_form, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

username_entry = Entry(login_form, width=30)
username_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="e")

password_label = Label(login_form, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

password_entry = Entry(login_form, width=30)
password_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=(0, 10), sticky="e")

url = ''
line_number = ''
api_key = ''

def ok_button_clicked():
    username = username_entry.get()
    password = password_entry.get()
    user_list = login()

    for user in user_list:
        if username.upper() == user.username.upper() and password.upper() == user.password.upper():
            login_form.destroy()
            accept_login()
            break
    else:
        messagebox.showerror("Error", "Username or Password is incorrect. Try again.")


ok_button = Button(login_form, text="Ok", width=10, command=ok_button_clicked)
ok_button.grid(row=2, column=1, padx=(30, 0), pady=(0, 10), sticky="w")


def cancel_button_clicked():
    login_form.destroy()


cancel_button = Button(login_form, text="Cancel", width=10, command=cancel_button_clicked)
cancel_button.grid(row=2, column=2, padx=10, pady=(0, 10), sticky="e")


def accept_login():
    account_list = load_data()
    accountlist = AccountList(account_list)

    window = Tk()
    window.title("Bank Account Management")

    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)

    def show_account_form(account=None):
        account_form = Tk()

        if account:
            account_form.title("Update account")
        else:
            account_form.title("New account")

        national_id_label = Label(account_form, text="National ID")
        national_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        national_id_entry = Entry(account_form, width=50)
        national_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        firstname_label = Label(account_form, text="First name")
        firstname_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        firstname_entry = Entry(account_form, width=50)
        firstname_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="e")

        lastname_label = Label(account_form, text="Last name")
        lastname_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        lastname_entry = Entry(account_form, width=50)
        lastname_entry.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="e")

        phone_label = Label(account_form, text="Phone number")
        phone_label.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

        phone_entry = Entry(account_form, width=50)
        phone_entry.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="e")

        if account:
            national_id_entry.insert(0, account.national_id)
            firstname_entry.insert(0, account.first_name)
            lastname_entry.insert(0, account.last_name)
            phone_entry.insert(0, account.phone)

        def submit():
            national_id = national_id_entry.get()
            firstname = firstname_entry.get()
            lastname = lastname_entry.get()
            phone = phone_entry.get()

            if account:
                account.update(national_id, firstname, lastname, phone)
                accountlist.show_contact_list = accountlist.account_list.copy()
            else:
                accountlist.insert(national_id, firstname, lastname, phone)

            replace_data(accountlist.account_list)
            load_data_treeview()
            account_form.destroy()

        submit_button = Button(account_form, text="Submit", command=submit)
        submit_button.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")

        account_form.mainloop()

    insert_button = Button(window, text="New Account", command=show_account_form)
    insert_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def update_button_clicked():
        update_id = int(accountlist_treeview.selection()[0])
        update_account = accountlist.get_account(update_id)
        show_account_form(update_account)

    update_button = Button(window, text="Update Account", state="disabled", command=update_button_clicked)
    update_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def increase_button_clicked():
        balance_form = Tk()
        balance_form.title("Increase Balance")

        account_id_label = Label(balance_form, text="Account ID")
        account_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        account_id_entry = Entry(balance_form, width=50)
        account_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        current_balance_label = Label(balance_form, text="Current Balance")
        current_balance_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        current_balance_entry = Entry(balance_form, width=50)
        current_balance_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="e")

        increase_balance_label = Label(balance_form, text="Increase Balance")
        increase_balance_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        increase_balance_entry = Entry(balance_form, width=50)
        increase_balance_entry.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="e")

        account_id = int(accountlist_treeview.selection()[0])
        account = accountlist.get_account(account_id)

        account_id_entry.insert(0, account.id)
        current_balance_entry.insert(0, account.balance)

        account_id_entry.config(state="readonly")
        current_balance_entry.config(state="readonly")

        def submit():
            increase_balance = int(increase_balance_entry.get())
            account.increase(increase_balance)
            accountlist.show_contact_list = accountlist.account_list.copy()
            replace_data(accountlist.account_list)
            load_data_treeview()

            if url and line_number and api_key:
                account.sms(f"{url}",
                            f"{line_number}",
                            f"{api_key}",
                            f"{account.phone}",
                            f"account: {account.id}\namount: +{increase_balance}\nnew balance: {account.balance}")

            balance_form.destroy()

        submit_button = Button(balance_form, text="Submit", command=submit)
        submit_button.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

        balance_form.mainloop()

    increase_button = Button(window, text="Increase Balance", state="disabled", command=increase_button_clicked)
    increase_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    def decrease_button_clicked():
        balance_form = Tk()
        balance_form.title("Decrease Balance")

        account_id_label = Label(balance_form, text="Account ID")
        account_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        account_id_entry = Entry(balance_form, width=50)
        account_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        current_balance_label = Label(balance_form, text="Current Balance")
        current_balance_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        current_balance_entry = Entry(balance_form, width=50)
        current_balance_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="e")

        decrease_balance_label = Label(balance_form, text="Decrease Balance")
        decrease_balance_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        decrease_balance_entry = Entry(balance_form, width=50)
        decrease_balance_entry.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="e")

        account_id = int(accountlist_treeview.selection()[0])
        account = accountlist.get_account(account_id)

        account_id_entry.insert(0, account.id)
        current_balance_entry.insert(0, account.balance)

        account_id_entry.config(state="readonly")
        current_balance_entry.config(state="readonly")

        def submit():
            decrease_balance = int(decrease_balance_entry.get())
            if decrease_balance > int(account.balance):
                messagebox.showerror("Error", "The balance is not enough!")
            account.decrease(decrease_balance)
            accountlist.show_contact_list = accountlist.account_list.copy()
            replace_data(accountlist.account_list)
            load_data_treeview()

            if url and line_number and api_key:
                account.sms(f"{url}",
                            f"{line_number}",
                            f"{api_key}",
                            f"{account.phone}",
                            f"account: {account.id}\namount: -{decrease_balance}\nnew balance: {account.balance}")

            balance_form.destroy()

        submit_button = Button(balance_form, text="Submit", command=submit)
        submit_button.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

        balance_form.mainloop()

    decrease_button = Button(window, text="Decrease Balance", state="disabled", command=decrease_button_clicked)
    decrease_button.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

    search_entry = Entry(window)
    search_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="ew")

    def search_button_clicked():
        term = search_entry.get()
        accountlist.search(term)
        load_data_treeview()

    search_button = Button(window, text="Search", command=search_button_clicked)
    search_button.grid(row=1, column=3, padx=10, pady=(0, 10), sticky="ew")

    accountlist_treeview = Treeview(window, columns=("id", "national_id", "firstname", "lastname", "phone", "balance"))
    accountlist_treeview.grid(row=2, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="nsew")

    accountlist_treeview.heading("#0", text="NO")
    accountlist_treeview.heading("#1", text="Account_ID")
    accountlist_treeview.heading("#2", text="National_ID")
    accountlist_treeview.heading("#3", text="First_name")
    accountlist_treeview.heading("#4", text="Last_name")
    accountlist_treeview.heading("#5", text="Phone_number")
    accountlist_treeview.heading("#6", text="Account_Balance")

    accountlist_treeview.column("#0", width=50)
    accountlist_treeview.column("#1", width=150)
    accountlist_treeview.column("#2", width=150)
    accountlist_treeview.column("#3", width=150)
    accountlist_treeview.column("#4", width=150)
    accountlist_treeview.column("#5", width=150)
    accountlist_treeview.column("#6", width=150)

    row_list = []

    def load_data_treeview():
        for row in row_list:
            accountlist_treeview.delete(row)
        row_list.clear()

        account_data = accountlist.show_account_list
        row_number = 1

        for account in account_data:
            row = accountlist_treeview.insert("", "end", iid=account.id, text=str(row_number),
                                              values=(
                                                  account.id, account.national_id, account.first_name,
                                                  account.last_name,
                                                  account.phone, account.balance))
            row_list.append(row)
            row_number += 1

    def manage_buttons(event):
        select_count = len(accountlist_treeview.selection())
        if select_count == 1:
            update_button.config(state="normal")
            increase_button.config(state="normal")
            decrease_button.config(state="normal")
        elif select_count > 1:
            update_button.config(state="disabled")
            increase_button.config(state="disabled")
            decrease_button.config(state="disabled")
        else:
            update_button.config(state="disabled")
            increase_button.config(state="disabled")
            decrease_button.config(state="disabled")

    accountlist_treeview.bind("<<TreeviewSelect>>", manage_buttons)
    load_data_treeview()

    window.mainloop()


login_form.mainloop()
