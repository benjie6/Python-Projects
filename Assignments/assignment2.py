class user:
    #define the attributes of the class
    name = "no name provided"
    email = ""
    password = "1234asdf"
    account = 0


#employee and customer are child classes 

class employee(user):
    department ='genral'
    base_pay = 11.00



class customer(user):
    mailing_address = ''
    mailing_list = True
    
    
    
