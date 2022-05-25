# Резюме

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Django](https://img.shields.io/badge/django-3.2-brightgreen)

## Создай резюме под себя
> Всего за пару кликов вы сможете создать резюме под свой стиль и получите доступ для просмотра и редактирования из любой точки вселенной


## Использование

1. Необходимо скачать проект с этого репозитория
    ```
    git clone https://github.com/YandexLyceumPP/Resume
    ```
2. Создаём виртуальное окружение и активируем его
    ```
    python3 -m venv venv && source venv/bin/activate
    ```
3. Устанавливаем зависимости
    ```
    pip install -r requirements.txt
    ```
4. Создаем файл `.env`, для production режима `DEBUG` меняем на `False`
    ```dotenv
    DEBUG=True
    SECRET_KEY=MySuperSecretKey
    ```
   При использовании PostgresSQL необходимо дополнительно указать параметры подключения к базе данных
    ```dotenv
   DATABASE_USER=postgres
   DATABASE_PASSWORD=231860Aa
   DATABASE_HOST=localhost
   PORT=5432
    ```
5. Настраиваем конфигурацию проекта в `resume/settings` (При необходимости)
6. Генерируем статику (Опционально, при `DEBUG=False`)
    ```
    python manage.py collectstatic
    ```
8. Запускаем приложение
    ```
    python manage.py runserver
    ```

## Требования
- Windows / MacOS / Linux
- Python 3.10+
- PostgresSQL (при необходимости)
