class User:
  '''
  User Class that will be used to manage user account
  
  Arguments: username and password
  '''
  all_users = []
  def __init__(self, user_name, user_password):
    self.user_name = user_name
    self.user_password = user_password

  
  def add_user(self):
    '''
    Add A user
    '''
    User.all_users.append(self)
