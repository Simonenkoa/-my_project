def require_role(allowed_roles):
    def require_dec(func):
        def wrap(name,role): #delete_database("Маша","admin") вызывается wrap("Маша","admin")
            if role in allowed_roles:
                return func(name,role) #роль разрешена вызваем оригинальную функцию
            else:
                print(f"доступ запрещён пользователю {name},{role}")
        return wrap
    return require_dec

@require_role(["admin"])
def delete_database(name,role):
    print(f"база данных удалена пользователем {name},{role}")
#temp = require_role(["admin"])
#temp теперь = require_dec (функция)
#delete_database = temp(delete_database)

@require_role(["admin","manager"])
def edit_database(name,role):
    print(f"были внесены изменения в базу данных пользователем {name},{role}")

delete_database("Маша","admin")
delete_database("Сережа","manager")
delete_database("Антон","user")
print()
edit_database("Алиса","admin")
edit_database("Кристина","manager")
edit_database("Валерий","user")