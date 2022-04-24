# Password-Locker
### By Eva Wamuyu

## Description
This is a python CLI project meant to help a user store their various account login details i.e One can add the account name eg Reddit, the username they use for the account eg @NavyBarb and the password they use eg 12345 or in place of adding a password, the program generates a random password for them.

## Setup Instructions
Clone the project in your local machine, navigate to the new created folder and run the code
The steps are as shown.
```
git clone https://github.com/Eva-Wamuyu/Password-Locker
cd Password-Locker
chmod +x pass_locker.py
./pass_locker.py


```
## Dependencies
* unittest
* PasswordGenerator module


## Technologies used

* Python

## BDD
| Behavior                                                               | Input Example                   | Output Example                                                                                                                                                                                      |
|------------------------------------------------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create Password Locker Account                                         | Username - Eva && Password 1234 | Welcome Eva password locker account created                                                                                                                                                         |
| Add an account which you as the user have a password                   | ac                              | prompt to add account name, username and password eg. Account: Tumblr , username: navyBarb, password 1234                                                                                                                                                  |
| Add an account which you do not have a password and  want it generated | cn                              | prompt to add account name and username. Password  is added by the program eg: Account name: Reddit, username : navyBarb                                                             |
| To view credentials in the locker                                      | vc                              | Authenticate first by logging into the password locker account if successful and there is already saved credentials, they are shown. If not successful one cannot view saved credentials            |
| To delete account saved in the locker                                  | del                             | Authenticate by logging into password locker. Prompt to add the account name to delete. eg Reddit If it is existent it is deleted. If authentication is not successful one cannot delete an account |
| To exit the program                                                    | any other key                   | Good bye and appreciation                                                                                                                                                                           |
## Author and Contacts

Eva Wamuyu
* Email: rutheve.eva@gmail.com
* Twitter: [@Ruth_Eva](https://twitter.com/Ruth_Eva_?t=_DEEkzJ3K0Qzr1npwZ7ggw&s=09)

## License
This projects has an MIT license.
You can view it [here](license)

