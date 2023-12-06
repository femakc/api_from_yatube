### Описание проекта:

Проект **API Yatube** предназначен для взаимодействия с сервисом **Yatub** через 
программный интерфейс по схеме **REST API**. Сделан при помощи [**Django Rest Framework**](https://www.django-rest-framework.org/)

С помощью проекта **API Yatube** возможно отправлять Http - запросы к сервису, для получения или изменения информации от сервиса **Yatube**

В проекте реализована возможность аутентификации по **JWT Token**

Настроена документация эндпойнтов через Redoc 
```
.../redoc/
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```Bash
git clone git@github.com:femakc/api_fina.git
```

```Bash
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```Bash
python3 -m venv venv
```

```Bash
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```Bash
python3 -m pip install --upgrade pip
```

```Bash
pip install -r requirements.txt
```

Выполнить миграции:

```Bash
python manage.py migrate
```

Запустить проект:

```Bash
python manage.py runserver
```

### Примеры запросов к API Yatube:

**GET** ``http://127.0.0.1:8000/api/v1/posts/`` 
```json
[
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
]
```
Доступна пагинация через параметры **limit** и **offset**
**GET** ``hhttp://127.0.0.1:8000/api/v1/posts/?offset=2&limit=2`` 
```json
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 3,
            "author": "admin",
            "text": "Text 3",
            "pub_date": "2022-08-06T14:16:18.468407Z",
            "image": null,
            "group": null
        },
        {
            "id": 4,
            "author": "admin",
            "text": "Text 4",
            "pub_date": "2022-08-06T14:16:24.010753Z",
            "image": null,
            "group": null
        }
    ]
}
```

**GET** ``http://127.0.0.1:8000/api/v1/posts/{id}/``
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
**POST** ``http://127.0.0.1:8000/api/v1/posts/``
```json
body
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

**GET** `` http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/``
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
