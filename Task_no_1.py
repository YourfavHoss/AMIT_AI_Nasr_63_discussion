
"""
Lessons revised:1- isinstance(input,type(s)) 
                2- ternary operator 
                3- .find() method for class str
                4- squared = map(lambda x: x ** 2, numbers) 
                5- isinstance bool method print(isinstance(1.0,(float,str)))

"""




                            ### TASK 1 MHH ###

input_mail = input('Please enter your E-mail') # string by default

### method for mail validation ###

def check_valid_mail(string_mail:str) -> bool:
    count_at_sign = string_mail.count('@')
    string_mail_trunc = string_mail[string_mail.find('@'):]
    count_dot = string_mail_trunc.count('.')
    flag_1 = True if count_at_sign == 1 else False
    flag_2 = True if count_dot != 0 else False
    
    return flag_1 and flag_2

#print(check_valid_mail(input_mail))


### method for username extraction ###

def extract_username(input_mail: str, mail_valid_status: bool) -> bool:
    pass

 





