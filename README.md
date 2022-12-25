<h1 align="center">
  <br>
  <img src="https://github.com/tonik350/img/blob/main/parse_logo.png?raw=true"></a>
  <br>
    Aсинхронный парсер PEP на базе фреймворка Scrapy
  <br>
</h1>

Парсер документов PEP на базе фреймворка Scrapy. Парсер создает два файла отчета: файл со списком PEP, включающим номер документа, название и статус, и файл суммарной статистики по количеству документов в разных статусах.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)

## Технологии
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)

## Использование
1. Клонировать репозиторий к себе на компьютер:

```bash
git@github.com:tonik350/scrapy_parser_pep.git
```
2. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
source venv/scripts/activate
```
3. Установить зависимости из файла requirements.txt, который лежит в корне проекта:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
___

## Запуск парсера:
```
scrapy crawl pep
```
___
## Результаты работы парсера:
Парсер выводит собранную информацию в два файла .csv:
- В первом файле (именован по маске `pep_ДатаВремя.csv`) - список всех PEP: номер, название и статус.
  

- Во втором файле (именован по маске `status_summary_ДатаВремя.csv`) содержится сводка по статусам PEP — 
  сколько найдено документов в каждом статусе (статус, количество) и общее количество всех документов.
