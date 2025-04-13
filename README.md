# Bank Account Management
This application is a simple Bank Account Management developed in Python.
The user interface of this project has been implemented by tkinter.
No specific database is used in this project and the information is stored in a text file.

## Features:
- User Login
- Create New Account
- Update Account
- Increase Balance
- Decrease Balance
- Search in Account_ID and National_ID
- Sending SMS via SMS system web service 

![2](https://github.com/user-attachments/assets/0698f400-05fb-440f-a271-9df975cd44e6)

## Login Page
You can login with this username and password :
- username : admin
- password : 123

- ![1](https://github.com/user-attachments/assets/968c26c9-c208-4ac9-a6c8-b5339fa52e8e)

## Create New Account
To define a new account, click the New Account button to receive the National ID, First name, Last name, and Phone number. Click the Submit button to add a new account to the account list. 

![3](https://github.com/user-attachments/assets/9f21ad6d-0043-45ee-8cad-bace31a71fcd)

## Update Account
To update an account, select the desired account and click the Update Account button to open the edit form. 
It is possible to change the National ID, First name, Last name, and Phone number in this form. By selecting the Submit button, the changes are applied to the list.

![4](https://github.com/user-attachments/assets/94996162-eca2-4918-89fc-efb66df91001)

## Increase Balance
To increase the balance of an account, select the desired account and click the Increase Balance button to open the form. 
By selecting the Submit button, the balance increase is made and a balance increase SMS is sent to the account holder's mobile phone number.

![9](https://github.com/user-attachments/assets/84079d7a-e8b9-46ca-995e-ac7b6c7d1b0d)

A sample of the sent SMS is as follows:

![10](https://github.com/user-attachments/assets/36a4debc-ade3-4af9-9040-0d8c27c9d703)

## Decrease Balance
To decrease the balance of an account, select the desired account and click the Decrease Balance button to open the form. 
By selecting the Submit button, the balance decrease is made and a balance decrease SMS is sent to the account holder's mobile phone number.

![11](https://github.com/user-attachments/assets/b95c1c40-3b00-4822-b44e-4562222793ae)

## Search
To Search an account by Account_ID or National_ID, enter the term in search bar and click the Search button . The list of account be filtered.

![7](https://github.com/user-attachments/assets/df7831a0-5ec0-4504-ad7e-da4c96d976ab)

## Send SMS
When the balance increases or decreases, it is possible to send an SMS to the account holder's mobile phone number. 
It is necessary to enter URL، Line Number, API Key in script.

![8](https://github.com/user-attachments/assets/1453f44f-2be9-4ede-ad5e-bd00068f56d0)
