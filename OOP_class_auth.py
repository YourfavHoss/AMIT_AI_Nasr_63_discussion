import random


###################################################

###  This class is for the User Authentiction   ###

###################################################

class UserAuth:
    def __init__(self, username: str, password: str):
      self.username = username
      self.password = password
    
    def user_authentication(self, username_entered: str, password_entered: str) -> bool:
      return (self.username == username_entered) and (self.password == password_entered)

    def send_verification_code(self): # print the returned s code in the main.py to mimic the email inbox
        if self.user_authentication:
            self.s = random.randrange(10000, 1000000)
            return self.s
        
    
    def verify_recieved_code(self,entered_verification_code: str):
        return self.s == entered_verification_code
        
