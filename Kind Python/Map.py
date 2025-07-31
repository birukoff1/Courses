from string import ascii_lowercase
chars = ascii_lowercase + '_' + '1234567890'

def check_email(email):
    global chars
    
    email = email.lower()
    if '@' in email:
        parts = email.split('@')
        
        for letter in parts[0]:
            if letter not in chars:
                return False
        
        if '.' not in parts[1]:
            return False
        else:
            for letter in parts[1].replace('.', ''):
                if letter not in chars:
                    return False
        
        return True
    else:
        return False
            
        

lst = 'abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com'

String = list(filter(check_email, lst.split()))


print(*String)