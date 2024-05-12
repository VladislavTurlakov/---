from dataVerification import admin_password
from getpass import getpass
import classes as c

def menu():
    """Функция меню программы"""
    print("\n1 - Admin\n2 - Client\n3 - Выход из программы")

def clientMenu():
    """Функция отображения меню для пользователя в роли Client"""
    pass

def clientActing():
    """Функция сущности Client"""
    client = c.Client()  # объект класса Client
    pass

# Функции роли Admin

def adminVerification():
    """Функция вхождения в роль Admin по паролю"""
    while True:
        print("\nЕсли хотите выйти в главное меню, введите quit")
        password = getpass(prompt="Введите пароль для входа: ")
        if password == "quit":  # выход из цикла
            return 1
        elif int(password) == int(admin_password):  # верный пароль
            return 0
        else:  # неверный пароль
            print("Неверный пароль. Попробуйте снова")

def adminMenu():
    """Функция отображения меню для пользователя в роли Admin"""
    print("\n0 - Выход в главное меню\n1 - Добавление компоненты\n2 - Удаление компоненты\n3 - Получение списка")
  
def adminActing():
    """Функция сущности Admin"""
    admin = c.Admin()  # объект класса Admin
    while True:
        adminMenu()
        action = int(input("\nВыберите действие: "))
        match action:
            case 0:  # выход в главное меню
                pass
                break
            case 1:  # добавление компоненты
                result = admin.addComponent()
                if result == True:  # добавление компоненты в базу данных прошло успешно
                    print("Добавление компоненты в базу данных прошло успешно")
                else:  # не удалось добавить компоненту в базу данных
                    print("Не удалось добавить компоненту в базу данных")
                break
            case 2:  # удаление компоненты
                result = admin.removeComponent()
                if result == True:  # удаление из базы данных прошло успешно
                    print("Удаление компоненты из базы данных прошло успешно")
                else:  # не удалось удалить компоненту из базы данных
                    print("Не удалось удалить компоненту из базы данных")
                break
            case 3:  # получение списка
                admin.showComponents
                break
    
