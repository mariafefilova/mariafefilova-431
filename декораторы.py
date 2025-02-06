#1
def log_function_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Функция '{func.__name__}' вызвана с аргументами: {args} {kwargs}")
        print(f"Вернуло: {result}")
        return result
    return wrapper

# Пример использования:
@log_function_calls
def multiply_numbers(x, y):
    return x * y
result = multiply_numbers(2, 5)# Вызов декорированной функции


#2
import time
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

@measure_execution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
    return tot
result = calculate_multiply([1, 2, 3, 4, 5])
print('result', result)

#3
class CacheResult:
    def __init__(self, func):
        self.func = func
        self.cache = {} #словарь для результатов 
    def __call__(self, *args, **kwargs):
        key = (args, tuple(kwargs.items()))  # создаем ключ для кеша из аргумента
        
        # Если результат уже в кэше, извлекаем его
        if key in self.cache:
            print("Retrieving result from cache...")
            return self.cache[key]
        
        # Если нет в кэше, выполняем вычисления
        print("Calculating the product of two numbers...")
        result = self.func(*args, **kwargs)
        
        # Сохраняем результат в кэше
        self.cache[key] = result
        return result

@CacheResult
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y

# Несколько вызовов декорированной функции
print(calculate_multiply(4, 5))  # Вычисление выполняется
print(calculate_multiply(4, 5))  # Результат извлекается из кэша
print(calculate_multiply(5, 7))  # Вычисление выполняется
print(calculate_multiply(5, 7))  # Результат извлекается из кэша
print(calculate_multiply(-3, 7))  # Вычисление выполняется
print(calculate_multiply(-3, 7))  # Результат извлекается из кэша


#4
import time
class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls #макс кол-во вызовов
        self.period = period #период времени в секундах
        self.calls = [] #список для хранения времени вызова

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time() 
            # Удаляем вызовы, которые произошли до периода отсечения
            self.calls = [call for call in self.calls if current_time - call < self.period]

            if len(self.calls) < self.max_calls: #не превышено ли макс кол-во вызовов
                self.calls.append(current_time)
                return func(*args, **kwargs)
            else:
                raise Exception("Rate limit exceeded. Please try again later.")# если лимит превышен 
        return wrapper

@RateLimiter(max_calls=6, period=10)
def api_call():
    print("API call executed successfully...")

# Выполнить вызовы API
for _ in range(8): #для нескольких вызовов 
    try: #пытаемся вызвать ф-ую
        api_call()
    except Exception as e: 
        print(f"Error occurred: {e}")

time.sleep(1)
api_call()


    



