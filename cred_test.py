import unittest
from credentials import Credentials
class testCreds(unittest.TestCase):
  '''
  Test credentials class
  '''

  def setUp(self):
      self.new_acc = Credentials("Reddit","@ev","a1234")
  
  def test_credential_init(self):
    self.assertEqual(self.new_acc.account_name, "Reddit")
    self.assertEqual(self.new_acc.account_username, "@ev")
    self.assertEqual(self.new_acc.account_password, "a1234")

  
  def tearDown(self):
      Credentials.all_accounts = []

  def test_save_credential(self):
    '''
    Func to test whether a new acc is added to the list
    '''
    
    self.new_acc.add_credential()
    another_acc = Credentials("Tumblr","eve","1234")
    another_acc.add_credential()
    self.assertEqual(len(Credentials.all_accounts),2)
    

if __name__ == "__main__":
  unittest.main()