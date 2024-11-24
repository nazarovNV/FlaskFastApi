# BuyTown Flask api

### Моё api для выпускного проекта Android Kotlin: Приложение для продавцов на маркетплейсе

## Описание проекта
Это простое api для моего проекта. Тут есть простые методы для получения и доабвления товаров, авторизации, регистрации
# Получение товаров (нужен jwt токен)
curl --location --globoff '{{URL}}/products' \
--header 'Authorization: {{access_token}}' \
--data ''
# Добавление товаров
curl --location --globoff '{{URL}}/products' \
--header 'Authorization: {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "name": "Ноутбук EVE C4403 14 Celeron N4000 4Gb SSD128Gb W11",
  "price": 13979,
  "description": "Это тест",

  "image_url": "https://s.iimg.su/s/03/5rLrMmWJhJy1GD0iZtMMTw1zkLzuZyYP7D5WW7uu.png"
}'
# Регистрация
curl --location --globoff '{{URL}}/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "testuser23333521",
    "password": "5",
    "email": "521@mail.ru"
}'
# Логин
curl --location --globoff '{{URL}}/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "5",
    "email": "521@mail.ru"
}'

## Как запустить локально на своей машине?
1. Скопируйте репозиторий на свою машину
2. Скачаейте необходимые библиотеки командой pip3 install -r requirements.txt
3. Запустите сервер python3 app.py

## Полезные ссылки
Ссылка на само андройд приложение тут https://github.com/nazarovNV/buytown
