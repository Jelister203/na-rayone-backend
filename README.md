# Проект "На районе". Бэкэнд. Микросервис "Шаблон на FastAPI".![FastAPI-app Template Workflow Tests](https://github.com/Jelister203/na-rayone-backend/actions/workflows/na-rayone-backend-workflow.yml/badge.svg)

Данный микросервис отвечает за следующие эндпоинты:
- Смотри в [таблице](https://miro.com/app/board/uXjVN0ClXug=/). При желании, распиши.
# Дерево проекта
```
root
├───.github
│   └───workflows
│       └───na-rayone-backend-workflow.yml 
├───backend
│   ├───app
│   │   ├───api
│   │   │   ├───__init__.py
│   │   │   │
│   │   │   ├───db.py
│   │   │   │
│   │   │   ├───models.py
│   │   │   │
│   │   │   ├───routers.py
│   │   │   │
│   │   │   └───schemas.py
│   │   │
│   │   ├───__init__.py
│   │   │
│   │   └───main.py
│   │  
│   ├───Dockerfile
│   │
│   ├───pyproject.toml
│   │
│   └───poetry.lock
│
├───infras
│   ├───docker-compose.yml
│   │
│   └───nginx.conf
│
├───README.md
│
├───.gitignore
│
└───LICENSE
```
## Важно.
Для использования этого шаблона, необходимо сделать его форк, чтобы его копия появилась в твоём личном списке репозиториев. Не клонируйте этот репозиторий на свою локальную машину, если не хотите работать с ветками, pull request'ами больше, чем необходимо.

# Шпаргалки по технологиям.

Использование [Git](https://git-scm.com/book/ru/v2):
```
#  Клонирование репозитория на локальную машину по HTTPS.

git clone https://github.com/Jelister203/na-rayone-backend.git
```

- Клонировать репозиторий можно и по ssh, тут как умеешь. [Статья](https://stackoverflow.com/questions/11041729/git-clone-with-https-or-ssh-remote) по поводу разницы между HTTPS и SSH.

```
#  Пуши, стэши и коммиты.

git add . #  Фиксирует изменения во всех файлах и директориях, за исключением тех, что описаны в .gitignore.
git commit -m "My Awesome New Commit" #  Создает из зафиксированных изменений новый коммит с сообщением "My Awesome New Commit".
git push #  Пушит изменения 

git stash . #  Удаляет все изменения и "откатывает" проект до последнего pull'а или commit'а.
```

Использование [Poetry](https://habr.com/ru/articles/593529/):
```
poetry install #  Установить зависимости проекта.

poetry show --tree #  Отобразить дерево зависимостей.

poetry run python main.py #  Запуск проекта.
```

Использование [Ruff](https://pypi.org/project/ruff/):
```
ruff check . #  Проверка всех файлов во всех дирректориях.

ruff format . #  Исправление всех файлов во всех дирректориях.
```

Использование [Docker](https://habr.com/ru/articles/310460/):
- По скольку я все подготовил, работать придется только с командами docker compose, а дальше смотреть либо через Docker Desktop либо через команды в терминале;
- Выполнение команд происходит из дирректории файла docker-compose.yml.
```
#  Полный запуск. Запускает все, описанные в docker-compose.yml, контейнеры.

docker compose up -d --build

#  Полный стоп.

docker compose stop

#  Работа с контейнерами.

docker container ls #  Выводит список всех запущенных на данной машине контайнеров. Для обращения используется поле container id.
docker container logs CONTAINER_ID #  Выводит логи контейнера.
docker container pomogite #  Выводит список всех комманд. Отображается при любом некорректном вводе.
```
