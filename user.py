class User:
  '''
  User Class that will be used to manage users who create login accounts
  
  Arguments: username and password
  '''

  def __init__(self, user_name, user_password):
    self.user_name = user_name
    self.user_password = user_password
    