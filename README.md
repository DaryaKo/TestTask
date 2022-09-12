# TestTask

## Запуск API

```cmd
docker-compose build
docker-compose up -d
```

Свагер можно найти по адресу `http://127.0.0.1:8000/api/v1/docs`

## Запуск тестов

```cmd
docker-compose exec app pytest .
```