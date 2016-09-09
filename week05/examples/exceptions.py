## [subcode]
def add(x, y):
    return x + y
    
## [subcode]
def add(x, y):
    try:
        return x + y
    except:
        return "Ошибка вычисления"

## [subcode]

x = int(input("Введите число :"))
        
## [subcode]

try:
    x = int(input("Введите число: "))
except ValueError:
    print("Вы должны ввести число.")
except KeyboardInterrupt:
    print("Вы отменили операцию.")

## [subcode]

try:
    x = int(input("Введите число: "))
except (ValueError, KeyboardInterrupt):
    print("Произошла ошибка")
    
## [subcode]

try:
    x = int(input("Введите число: "))
except ValueError:
    print("Вы должны ввести число.")
except KeyboardInterrupt:
    print("Вы отменили операцию.")
else:
    print("Вы ввели число", x)

## [subcode]

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

## [subcode]

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
            
## [subcode]

try:
    raise Exception("Happened something wrong")
    print ("Some text")
except Exception as ex:
    print("Catch Exception:", ex)

## [subcode]
    
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
        
## [subcode]

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

## [subcode]

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("деление на нуль")
    return a/b
try:
    div(10, 0)
except ZeroDivisionError as err:
    print("Ошибка",err)




