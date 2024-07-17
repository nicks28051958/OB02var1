class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self._access_level = access_level
        else:
            raise ValueError("Недопустимый уровень доступа!")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        if not isinstance(user, User):
            raise ValueError("Можно добавить только пользователя User.")
        user_list.append(user)

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                break
        else:
            raise ValueError("UПользователь(User) с этим ID не найден!")


def main():
    # Список всех пользователей
    users = []

    while True:
        print("\n1. Добавить пользователя")
        print("2. Добавить администратора")
        print("3. Удалить пользователя (только админ)")
        print("4. Показать всех пользователей")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            user_id = input("Введите ID пользователя: ")
            name = input("Введите имя пользователя: ")
            users.append(User(user_id, name))
        elif choice == '2':
            user_id = input("Введите ID администратора: ")
            name = input("Введите имя администратора: ")
            admin = Admin(user_id, name)
            users.append(admin)
        elif choice == '3':
            if not any(user for user in users if isinstance(user, Admin)):
                print("Нет администраторов для выполнения этого действия.")
                continue
            user_id = input("Введите ID пользователя для удаления: ")
            admin_found = False
            for user in users:
                if isinstance(user, Admin):
                    admin = user
                    admin_found = True
                    try:
                        admin.remove_user(users, user_id)
                        print("Пользователь удален.")
                    except ValueError as e:
                        print(e)
                    break
            if not admin_found:
                print("Нет администратора в списке.")
        elif choice == '4':
            if not users:
                print("Список пользователей пуст.")
            for user in users:
                print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
