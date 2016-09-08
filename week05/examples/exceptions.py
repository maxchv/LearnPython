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
    
import builtins
import inspect
for type_name in dir(builtins):
    _type = getattr(builtins, type_name)    
    if inspect.isclass(_type):
        try:
            if isinstance(_type(), Exception):
                print(type_name)
        except:
            pass
            
## [subcode]

try:
    raise NameError("Hi")
except NameError as ex:
    print("Catch NameError" + ex)


        
