# from dis import dis
from password_generator import PasswordGenerator
from user import User
from credentials import Credentials

Random_password = PasswordGenerator()

def create_user_acc(their_name, their_pass):
  '''
  Creating a new User:
  '''
  new_user = User(their_name,their_pass)
  return new_user;

def add_media(acc_name,acc_user,acc_pass):
  '''
  Creating  a new Credential and pushing it to the list
  '''
  new_account = Credentials(acc_name,acc_user,acc_pass)
  Credentials.add_credential(new_account)
def display():
  '''
  Display accounts saved amd their passwords
  '''
  return Credentials.show_all_accounts()

def deleteAccount(accname):
  return Credentials.delete_credential(accname)


  

def main():
    print("\tWelcome to Password Locker.\n\tCreate an Account to Continue")

    userName = input("Username:\t")
    password = input("Password:\t")
    create_user_acc(userName,password)
    def authenticate():
       '''
       Func to ask for user login details into password locker
       '''
       confirmUserName = input("\tPassword Locker UserName: \t");
       confirmPass = input("\tPassword Locker Password:\t");
       if confirmPass != password or confirmUserName != userName:
           return False
       else:
           return True

  
    print(f"Hello {userName} PasswordLocker Account created successfully")

    while(True):
      print("What do You Want to do today?")
      print("Use the Shortcodes Below to navigate:")
      print("\tvc to view credentials, \n\tac to add an account\n\tcn to add an account and have password generated \n\t del to delete an account\n Any other to Exit.")

      short_code = input(" Code>>>\t").lower()
      if short_code == "vc":
        print("To view Credentials You have to sign into your password locker account")
        if authenticate():
         if display():
            print("Your accounts and their credentials:")
            for cred in Credentials.show_all_accounts():
              print("--"*10)
              print(f'ACCOUNT-NAME {cred.account_name}\n User-Name {cred.account_username}\n Password {cred.account_password}')
         else:
            print("No Existing accounts Found")
            print("*"*10)
        else:
          print("Invalid Password Locker Login Details")
          print("You cannot view saved credentials")
      elif short_code == "ac":
        print("Add An Account")
        acc_name = input("\tAccount Name")
        acc_user = input("\tUser_name")
        acc_pass = input("\tPassword")
        print(f"\t{acc_name} Added Successfully")
        
          
      
      elif short_code == "cn":
        print("Add an Account and Have a password generated for you")
        acc_name = input("\tAccount Name:\t")
        acc_user = input("\tUsername:\t")
        acc_pass = Random_password.generate()
        add_media(acc_name,acc_user,acc_pass)

      elif short_code == "del":
        print("To Delete, Authentication to password locker is needed")
        if authenticate():
          acc_to_delete = input("\tAccount to delete\t:")
          deleteAccount(acc_to_delete)
        else:
          print("Woops! Login Details don't match\n Access to delete Denied")
        

      else:
        print("\tBye")
        print("\tIt was nice having you")
        break

main()


