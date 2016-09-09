## [потенциально опасная операция]
def add(x, y):
    return x + y
    
## [перехват исключения]
def add(x, y):
    try:
        return x + y
    except:
        return "Ошибка вычисления"

## [ввод с приведением типа]

x = int(input("Введите число :"))
        
## [перехват исключений заданного типа]

try:
    x = int(input("Введите число: "))
except ValueError:
    print("Вы должны ввести число.")
except KeyboardInterrupt:
    print("Вы отменили операцию.")

## [перехват исключений заданного типа в одном блоке exception]

try:
    x = int(input("Введите число: "))
except (ValueError, KeyboardInterrupt):
    print("Произошла ошибка")
    
## [блок else]

try:
    x = int(input("Введите число: "))
except ValueError:
    print("Вы должны ввести число.")
except KeyboardInterrupt:
    print("Вы отменили операцию.")
else:
    print("Вы ввели число", x)

## [блок finally]

try:
    x = int(input("Введите число: "))
except ValueError:
    print("Вы должны ввести число.")
except KeyboardInterrupt:
    print("Вы отменили операцию.")
else:
    print("Вы ввели число", x)
finally:
    print("Работа программы завершена")

## [блок else и finally]

try:
    x = int(input("Введите число: "))
except ValueError as ex:
    print("Произошла ошибка: " + ex)
except KeyboardInterrupt as ex:
    print("Вы отменили операцию: " + ex)
else: 
    print("Вы ввели число", x)
finally:
    print("Работа программы завершена")
            
## [порождение исключений]

try:
    raise Exception("Happened something wrong")
    print ("Some text")
except Exception as ex:
    print("Catch Exception:", ex)

## [перечень стандартных исключений]
    
import builtins # импорт всех встроенных типов
import inspect  # для исследования данных
for type_name in dir(builtins):
    _type = getattr(builtins, type_name)    
    if inspect.isclass(_type):
        try:
            if isinstance(_type(), BaseException):
                print(type_name)
        except:
            pass
        
## [перехват исключений вне функции]

def add(a, b):    
    return int(a) + int(b)
	
try:
    x = input("x: ")
    y = input("y: ")
    z = add(x, y)
    print(z)
except TypeError:
    print("Ошибка вычисления")
except ValueError as ex:
    print("Ошибка ValueError", ex)
except KeyboardInterrupt:
    print ("Пользователь прервал ввод данных")

## [порождение стандартных исключений]

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("деление на нуль")
    return a/b
try:
    div(10, 0)
except ZeroDivisionError as err:
    print("Ошибка",err)




