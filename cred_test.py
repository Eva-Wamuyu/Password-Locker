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

  # def test_save_credential(self):
    

if __name__ == "__main__":
  unittest.main()