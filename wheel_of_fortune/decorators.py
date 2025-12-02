import time
from functools import wraps

def timer1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) 
        end_time = time.time() 
        
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.4f} секунд")
        
        return result
    return wrapper

import logging
from functools import wraps
from datetime import datetime

def log_errors(log_file='game.log'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_message = f"[{error_time}] ОШИБКА в функции '{func.__name__}': {str(e)}"
                
                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(error_message + '\n')
                
                print(f" Ошибка записана в лог: {log_file}")
                raise  
        return wrapper
    return decorator

def timee(x):
    mi = x//60
    sec = x%60
    return f'{mi} минут {sec} секунд'