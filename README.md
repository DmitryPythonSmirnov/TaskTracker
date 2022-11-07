### TaskTracker_v1

Проект представляет из себя простое web-приложение на Django для ведения списка задач.
В версии v1 контроллеры написаны на функциях. Планируется версия v2 с контроллерами на классах и другими улучшениями.
Задачи делятся на "Открытые" и "Закрытые". Также можно посмотреть "Все задачи" (весь список).

Чтобы работать с задачами, необходимо зарегистрироваться в приложении.
Регистрация производится через web-интерфейс приложения.
При такой регистрации создаётся обычный пользователь (не суперпользователь).
Для создания суперпользователя необходимо выполнить команду

`python manage.py createsuperuser`

(см. инструкцию ниже).

Каждый пользователь видит только свои задачи. Суперпользователь через стандартную админку видит все задачи (задачи всех пользователей), также он может изменять пользователя, которому принадлежит задача.

Поле "Тема" при создании задачи задумывалось на будущее, для сортировок задач по темам.
Предполагается для задач на одну тему вводить один и тот же текст в этом поле.
Возможно, в будущем будет создан отдельный справочник тем, а поле "Тема" в создании задачи
будет в виде выпадающего списка - для выбора темы из списка.

Задачи сортируются по времени обновления в обратном порядке (задача с самым свежим обновлением выше всех в списке).

Количество задач на странице задаётся в переменной TASKS_PER_PAGE в файле tasktracker/mainapp/views.py.
В проекте установлено TASKS_PER_PAGE = 3.

При удалении задачи задача удаляется из базы.

Для хранения данных используется SQLite.

---

**Требования:**  
Python версии 3.6 и выше.  
Дополнительно необходимо установить Django 3.2 (см. инструкцию ниже).

---

**Инструкция по локальному запуску:**  
Инструкция приведена для ОС Windows с уже установленным Python требуемой версии.
На Windows автоматически устанавдиваются модули pip и venv.
Для других ОС шаги аналогичны, но нужно учитывать отличия конкретных ОС.
На Linux и Mac OS модули pip (pip3) и venv (или virtualvenv) скорее всего нужно установить отдельно.
На Linux и Mac OS вне виртуального окружения нужно запускать ptyhon как python3, а внутри виртуального окружения - просто python (возможно, внутри виртуального окружения python3 тоже работает).

1. Склонировать репозиторий на компьютер.  
Скачать ZIP-архив или склонировать через git (если он установлен):

`git clone https://github.com/DmitryPythonSmirnov/TaskTracker_v1.git`

Если скачали ZIP-архив, распакуйте его и переименуйте из "TaskTracker_v1-main" в "TaskTracker_v1".


2. Открыть терминал.  
Win+R -> cmd -> OK

3. Перейти в каталог с папкой "TaskTracker_v1".
Например, если папка "TaskTracker_v1" находится на Рабочем столе, то команда будет выглядеть так:

`cd %USERPROFILE%\Desktop\TaskTracker_v1`


4. Создать виртуальное окружение.  

`python -m venv .venv`

В текущем катлоге должен появиться каталог ".venv".

5. Активировать виртуальное окружение.

`.venv\Scripts\activate`

В командной строке должен появиться префикс **(.venv)**.

6. Проапгрейдить модуль pip.

`python -m pip install --upgrade pip`

7. Установить Django 3.2.

`pip install django==3.2`

8. Перейти в каталог "tasktracker".
Это главный каталог проекта, в нём находится файл "manage.py".
**Все последующие команды выполняются из этого каталога с активированным виртуальным окружением, то есть с префиксом (.venv) в командной строке.**

`cd tasktracker`

9. Создать миграции (подготовка скриптов для создания базы структуры базы данных):  
`python manage.py makemigrations`

```
python manage.py makemigrations
Migrations for 'authapp':
  authapp\migrations\0001_initial.py
    - Create model TaskUser
Migrations for 'mainapp':
  mainapp\migrations\0001_initial.py
    - Create model Task
```

10. Выполнить миграции:

`python manage.py migrate`

В текущем каталоге должен повиться файл "db.sqlite3".
```
python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, authapp, contenttypes, mainapp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying authapp.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying mainapp.0001_initial... OK
  Applying sessions.0001_initial... OK
```

11. Создать суперпользователя (адрес электронной почты можно не указывать):  
`python manage.py createsuperuser`

```
python manage.py createsuperuser
Имя пользователя: django
Адрес электронной почты:
Password:
Password (again):
Superuser created successfully.
```

12. Запустить локальный web-сервер.  
`python manage.py runserver`

13. Зайти на http://127.0.0.1:8000/

14. Залогиниться под пользователем, созданным в п.11, или зарегистрировать нового пользователя.  
После входа в меню появится допольнительная ссылка "Создать задачу" - можно начинать создавать задачи.

15. Стандартная админка Django (только для суперпользователей): http://127.0.0.1:8000/admin

16. Для остановки сервера нужно нажать Ctrl+C (или два раза Ctrl+C).

17. Для изменения пароля пользователя используйте команду  
(пример для пользователя django)  
`python manage.py changepassword django`

18. Деактивировать виртуальное окружение не обязательно, можно просто закрыть терминал или выйти из него.
