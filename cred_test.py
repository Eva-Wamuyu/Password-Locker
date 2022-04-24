
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

  def test_remove(self):
    '''
    Func to test the delete functionality
    '''
    another_acc = Credentials("Tumblr","eve","1234")
    another_acc.add_credential()
    Credentials.delete_credential('Tumblr')
    self.assertEqual(len(Credentials.all_accounts),0)
  
  def test_search(self):
    '''
    Func to test the search function
    '''
    another_acc = Credentials("Tumblr","eve","1234")
    another_acc.add_credential()
    found_credential = Credentials.search_Acc("Tumblr")
    self.assertEqual(another_acc, found_credential)
    
    

if __name__ == "__main__":
  unittest.main()