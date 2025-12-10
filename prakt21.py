def logger(func):
    def wrap(*args,**kwargs):
        print(f"вызов функции {func.__name__} с аргументами {args} и {kwargs}")

        fun=func(*args,**kwargs)

        print(f"функция {func.__name__} вернула {fun}")
        return fun
    return wrap

@logger
def add(a,b):
    return a+b
#add=logger(add)

@logger
def div(a,b):
    if b==0:
        return "делить на ноль нельзя"
    return a/b
#div=logger(div)

@logger
def greet(name):
    return f"Здравствуй, {name}."

add(25,5)
print()
add(a=25,b=5)
print()
div(25,5)
print()
greet("Кот")