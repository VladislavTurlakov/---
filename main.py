import functions as f

while True:  # бесконеченый цикл
    f.menu()  # меню на экране
    answer = int(input("Выберите роль: "))
    match answer:
        case 1:  # роль администратора
            state = f.adminVerification()
            if state == 0:  # успешный вход как администратор
                print("Вход как Admin успешно завершен")
                f.adminActing()
                break
            else:  # выход в главное меню
                print("Выход в главное меню")
                continue
        case 2:  # роль клиента
            print("Вход как Client успешно завершен")
            f.clientActing()
            break
        case 3:  # выход из программы
            break
        case _:  # ввод неверной цифры
            print("Неверна выбрана роль")
