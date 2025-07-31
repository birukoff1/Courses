from functools import wraps

def func_show(func):
    
    @wraps(func)
    def inner_function(*args):
        
        return sum(func(*args)) 
    
    return inner_function


@func_show
def get_list(String):
    """Функция для формирования списка целых значений"""    
    
    return [int(x) for x in String.split(' ')]


print(get_list('1 2 3'))

