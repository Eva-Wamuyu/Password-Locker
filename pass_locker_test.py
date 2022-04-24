import unittest
from credentials import Credentials
from user import User

class UserTest(unittest.TestCase):
  '''
  UserTest class asserts the User Class
  Takes the unittest.TestCase argument

  '''
  
  def setUp(self):
    '''
    Setup method to run before each test case
    '''
    self.new_user = User("Wamuyu","A1234")

  def test_initializer(self):
    '''
    Assert that initialization is properly done
    '''
    self.assertEqual(self.new_user.user_name, "Wamuyu")
    self.assertEqual(self.new_user.user_password, "A1234")

  
  def test_add_user(self):
    '''
    Assert that a user and their credentials is added
    '''
    self.new_user.add_user()
    self.assertEqual(len(User.all_users),1)



if __name__ == '__main__':
  unittest.main()