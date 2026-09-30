# Sales Report — CSV версия

Скрипт читает CSV-файл с продажами, считает выручку по дням, товарам 
и категориям, находит топ-5 товаров, сохраняет отчёт в Excel.

## Возможности
- Чтение CSV с продажами
- Расчёт выручки по дням, товарам, категориям
- Топ-5 товаров
- Экспорт отчёта в Excel (4 листа)

## Установка
pip install -r requirements.txt

## Использование
python main.py

Скрипт читает `data/sales.csv` и сохраняет отчёт в `output/report.xlsx`.

## Формат данных
CSV с колонками: `date`, `product`, `category`, `quantity`, `price`.

## Технологии
- Python 3.12
- pandas
- openpyxl