import pyperclip
class Credentials:
  '''
  Holding and creating instances of credentials
  Args:
  Account Usename and Password
  '''

  all_accounts = []

  def __init__ (self, account_name,account_username ,account_password):
    self.account_name = account_name;
    self.account_username = account_username;
    self.account_password = account_password;
  
  def add_credential(self):
    Credentials.all_accounts.append(self)
  
  @classmethod
  def show_all_accounts(cls):
    return cls.all_accounts;

  @classmethod
  def search_Acc(cls,acc):
    '''
    Search Func: to be used when deleting an account
    '''
    for cred in cls.all_accounts:
      if cred.account_name == acc:
        return cred;


  @classmethod
  def delete_credential(cls, the_name):
    '''
    Delete func, calls the search func and executes deletion
    '''
    get_acc_with_name = cls.search_Acc(the_name)
    if(get_acc_with_name):
     cls.all_accounts.remove(get_acc_with_name)
    else:
      return False





  