## Wheel of Fortune

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Size](https://img.shields.io/badge/Size-8.1_MB-orange)

</div>

Поле Чудес - игра на угадывание словю

- 3 уровня сложности (7, 5 или 3 жизни)
- Угадывание букв или слов целиком
- Сохранение рекордов в файл
- Статистика игры после завершения
- Автоматическая генерация слов из словаря
- Готовый исполняемый файл для Windows

## Установка и запуск

### Способ 1: Готовый EXE 
1. Скачайте [wheel_of_fortune.exe](dist/wheel_of_fortune.exe)
2. Запустите файл двойным кликом



## Как играть

1. Выберите уровень сложности:
- Легкий: 7 жизней
- Средний: 5 жизней  
- Сложный: 3 жизни

2. Угадывайте:
- Вводите буквы по одной
- Или слово целиком
- Избегайте повторения букв

3. Статистика:
- После игры увидите количество угаданных слов
- Время игры
- Новый рекорд (если побили)

## Структура проекта
        wheel-of-fortune-game/
        ├── dist/
        │ └── wheel_of_fortune.exe
        ├── data/
        │ ├── words.txt
        │ └── record.txt 
        ├── __main__.py 
        ├── game.py 
        ├── file_handler.py 
        ├── utils.py 
        └── README.md


## Сборка из исходного кода

Если вы хотите собрать EXE самостоятельно:

Установите PyInstaller

        pip install pyinstaller

Соберите EXE

        pyinstaller --onefile --console --add-data "data/*;data" --paths=. __main__.py

EXE появится в папке dist/

## Версии

- Размер EXE: 8.1 МБ
- Язык: Python 3.13
- Сборщик: PyInstaller 6.16.0
