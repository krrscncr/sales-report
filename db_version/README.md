# Sales Report — MySQL версия

Скрипт читает данные о продажах из базы MySQL, считает выручку по дням, 
товарам и категориям, находит топ-5 товаров, сохраняет отчёт в Excel.

## Возможности
- Подключение к MySQL через SQLAlchemy
- Чтение данных SQL-запросом
- Расчёт выручки по дням, товарам, категориям
- Топ-5 товаров
- Экспорт отчёта в Excel (4 листа)

## Установка
pip install -r requirements.txt

## Подготовка базы
1. Создать базу данных `sales_db`
2. Создать таблицу `sales` с колонками: `date`, `product`, `category`, `quantity`, `price`
3. Залить данные:
   python import_csv_to_db.py

## Использование
python main.py

Отчёт сохраняется в `output/report.xlsx`.

## Технологии
- Python 3.12
- pandas
- SQLAlchemy
- mysql-connector-python
- openpyxl

## Что было изучено
- Подключение к MySQL из Python
- SQL-запросы через SQLAlchemy
- Разница между чтением файла и чтением базы данных