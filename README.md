🚀 FastAPI Backend Example

Пример быстрого старта для разработки бэкенда на FastAPI с разбивкой на модули.

📦 Структура проекта

fastapi_example/
│
├── main.py                 # Точка входа в приложение
├── requirements.txt        # Список зависимостей
│
└── src/
    ├── __init__.py         # Создание приложения, подключение роутеров, инициализация БД
    ├── config.py           # Загрузка конфигурации из .env
    ├── errors.py           # Кастомные ошибки
    │
    ├── routes/             # Папка с роутами (эндпоинтами)
    │   └── user.py         # Роуты для пользователя
    │
    ├── schemas/            # Схемы данных (Pydantic)
    │   └── user.py         # Схема пользователя
    │
    ├── db/                 # Работа с базой данных
    │   ├── database.py     # Подключение к БД
    │   └── models.py       # SQLAlchemy-модели
    │
    └── handlers/
        └── user_repository.py  # CRUD-операции с пользователями
🛠️ Установка и запуск

1. Клонируйте репозиторий
git clone https://github.com/chinazes532/fastapi_example.git
cd fastapi_example
2. Создайте виртуальное окружение
<details> <summary>MacOS / Linux</summary>
python3 -m venv .venv
source .venv/bin/activate
</details> <details> <summary>Windows</summary>
python -m venv .venv
.venv\Scripts\activate
</details>
3. Установите зависимости
pip install -r requirements.txt
4. Создайте файл .env
Создайте файл .env в корне проекта и добавьте туда свои переменные окружения, например:

DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
DEBUG=True
Важно: Названия переменных должны соответствовать тем, что используются в config.py.
5. Запуск приложения
python3 main.py
Приложение будет доступно по адресу: http://127.0.0.1:8000

Документация Swagger будет доступна по адресу:
http://127.0.0.1:8000/docs
