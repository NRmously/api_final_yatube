# API Yatube

## Информация о проекте:
API для Yatube.  
Для аутентификации использованы JWT-токены.  
У неаутентифицированного пользователя доступ к API только на чтение, эндпоинт /follow/ недоступен.  
Аутентифицированному пользователю разрешено изменение и удаление только своего контента.  
Добавление новых пользователей через API не требуется.

## Иcпользованные технологии:
Python, Pillow (PIL Fork), Django, Django REST framework, Djoser

## Инструкция по установке:
Клонирование репозитория:
```
git clone <https или SSH URL>
```

Создание виртуального окружения и его активация:
```
python -m venv venv
```
```
source venv/bin/activate
```

Обновление менеджера пакетов pip:
```
python -m pip install --upgrade pip
```

Установить зависимости:
```
pip install -r requirements.txt
```

Перейти в директорию с файлом manage.py и выполнить миграции:
```
cd yatube_api
```
```
python manage.py migrate
```

Создаём супер-пользователя:
```
python manage.py createsuperuser
```

Запуск сервера:
```
python manage.py runserver
```

### Эндпоинты:
`api/v1/jwt/create/` - (POST): передаём логин и пароль, получаем токен и рефреш-токен.

`api/v1/jwt/refresh/` - (POST): передаём рефреш-токен, получаем новый токен.

`api/v1/jwt/verify/` - (POST): передаём токен, получаем информацию о его валидности.

`api/v1/posts/` -  (GET, POST): получаем список всех постов или создаём новый пост.

`api/v1/posts/{id}/` - (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.

`api/v1/posts/{post_id}/comments/` - (GET, POST): Получаем все комментарии или добавляем комментарий к посту.

`api/v1/posts/{post_id}/comments/{id}/` - (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id.

`api/v1/groups/` - (GET): получаем список доступных сообществ.

`api/v1/groups/{id}/` - (GET): получение информации о сообществе по id.

`api/v1/follow/` - (GET): возвращает все подписки пользователя, сделавшего запрос.

`api/v1/follow/` - (POST): подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.

# Документация к API
После запуска сервера, по адресу  http://127.0.0.1:8000/redoc/ будет доступна полная документация для API Yatube.

## Примеры запросов и ответы:
Пример POST-запроса на получение токена авторизации:
`POST .../api/v1/jwt/create/`
```
{
    "username": "string",
    "password": "string"
}
```
Пример ответа:
```
{
  "refresh": "string",
  "access": "string"
}
```

Пример GET-запроса на получение списка публикаций 
`GET .../api/v1/posts/?limit=<число>&offset=<число>`

`limit` - Сколько выводить публикаций на страницу. Необязательный параметр.

`offset` - Номер страницы. Необязательный параметр.

Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Пример POST-запроса для создания комментария:  
`GET .../api/v1/posts/<post_id>/comments/`
Authorization: <Ваш токен>
```
{
  "text": "string"
}
```

Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```


# Автор:
Андрей Мирт  
https://github.com/NRmously
