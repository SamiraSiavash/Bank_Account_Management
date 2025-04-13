from http import client
import json


class Account:
    def __init__(self, id, national_id, firstname, lastname, phone, balance):
        self.id = id
        self.national_id = national_id
        self.first_name = firstname
        self.last_name = lastname
        self.phone = phone
        self.balance = balance

    def update(self, new_national_id, new_firstname, new_lastname, new_phone):
        self.national_id = new_national_id
        self.first_name = new_firstname
        self.last_name = new_lastname
        self.phone = new_phone

    def increase(self, amount):
        self.balance = int(self.balance) + amount

    def decrease(self, amount):
        if amount <= int(self.balance):
            self.balance = int(self.balance) - amount

    def sms(self, url, line_number, api_key, phone, message):
        conn = client.HTTPSConnection(f"{url}")
        payload = json.dumps({
            "lineNumber": f"{line_number}",
            "messageText": f"{message}",
            "mobiles": [
                f"{phone}"
            ],
            "sendDateTime": None
        })
        headers = {
            'X-API-KEY': f"{api_key}",
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/v1/send/bulk", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
